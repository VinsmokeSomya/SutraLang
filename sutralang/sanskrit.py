import sys
import importlib.abc
import importlib.util
from pathlib import Path

import ast
import tokenize
from tokenize import TokenInfo
import io
import re # Import re module

# Import the mappings from the dedicated file
from .mappings import sanskrit_keywords


def parse_syntax(translated_code):
    # print("--- Translated Code Before AST Parse ---")
    # print(translated_code)
    # print("---------------------------------------")
    try:
        ast.parse(translated_code)
        return translated_code  # Valid Python code
    except SyntaxError as e:
        print(f"Syntax error in translated code: {e}") # This is what we see
        # When this error happens, the above print would have shown the problematic code.
        return None  # Return None to indicate invalid code

def translate_sanskrit(code: str) -> str:
    # 1. Handle 'मानम्' assignment with string manipulation
    processed_lines = []
    for line in code.splitlines():
        stripped_line = line.lstrip()
        if stripped_line.startswith('मानम् '):
            # Calculate original indentation
            indentation = line[:-len(stripped_line)]
            
            # Process the line without its original indentation
            parts = stripped_line.split('=', 1)
            if len(parts) == 2:
                variable_part = parts[0].replace('मानम्', '').strip()
                value_part = parts[1].strip()
                # Reconstruct the line with original indentation
                new_line = f'{indentation}{variable_part} = {value_part}'
            else:
                new_line = line # Fallback
        else:
            new_line = line # Non-'मानम्' lines are preserved as is
        processed_lines.append(new_line)
    code_after_manam = "\n".join(processed_lines)

    # 2. Tokenize and translate other keywords
    result_tokens = []
    bytes_io = io.BytesIO(code_after_manam.encode('utf-8'))
    tokens = tokenize.tokenize(bytes_io.readline)
    
    prev_tok_string = "" # For checking attribute access (.something)

    for tok in tokens:
        # If it's a NAME token, in our keywords dict, and not preceded by '.'
        if tok.type == tokenize.NAME and tok.string in sanskrit_keywords and prev_tok_string != '.':
            result_tokens.append(TokenInfo(tok.type, sanskrit_keywords[tok.string], tok.start, tok.end, tok.line))
        else:
            result_tokens.append(tok) # Keep original token
        
        # Update prev_tok_string for the next iteration's attribute check
        # Consider only significant tokens, not whitespace/comments for this logic
        if tok.type not in [tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT, tokenize.COMMENT]:
            prev_tok_string = tok.string
        else: 
            # If it is a non-significant token like newline, reset prev_tok_string 
            # so that a new line doesn't mistakenly think it's an attribute.
            # However, for strict `.` checking, only `.` matters. Let's stick to original for now.
            pass # prev_tok_string remains to see if `.` was just before this newline

    # print(f"--- Result Tokens before untokenize (for file being processed) ---")
    # for rt in result_tokens:
    #     print(rt)
    # print(f"------------------------------------------------------------------")

    translated_code = tokenize.untokenize(result_tokens).decode('utf-8')

    # print(f"--- Code for AST Parse (from translate_sanskrit, for file being processed) ---")
    # print(translated_code) # Use the variable name as it is in the original code
    # print(f"--------------------------------------------------------------------------------")

    return parse_syntax(translated_code) # Use the variable name as it is


# Custom import loader and finder
class sktLoader(importlib.abc.SourceLoader):
    def __init__(self, path):
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            sanskrit_code = f.read()
        translated_python_code = translate_sanskrit(sanskrit_code)
        if translated_python_code is None:
            raise ImportError(f"Failed to translate Sanskrit module: {path}")
        return translated_python_code.encode('utf-8')

class sktFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        # fullname: The full name of the module being imported (e.g., "गणित", "sutralang.गणित", "घटकः.गणित")
        # path: A list of locations to search for the module (often the parent package's __path__ e.g. ['.../sutralang'])
        # target: Module object, usually None

        # Construct potential file path relative to current dir or provided paths
        module_file_name = fullname.split('.')[-1] + ".skt" # e.g., "गणित.skt"

        # 1. Check relative to the current working directory (for top-level script imports)
        # This handles `import mymodule` when mymodule.skt is in the same dir as the running script
        top_level_path = Path(module_file_name)
        if top_level_path.exists():
             # Check if we are actually running the module itself, avoids self-import loop
             # This might need refinement depending on exact execution context needs
             # For now, assume top-level skt files shouldn't be imported by name like this
             # pass # Let other finders handle it or decide specific logic
             # Let's allow top-level for now, might need adjustment later
             return importlib.util.spec_from_loader(fullname, sktLoader(str(top_level_path)))

        # 2. Check within the standard package structure using `path`
        # path is typically ['.../sutralang'] when importing something from within sutralang
        if path:
            for search_path in path:
                potential_path = Path(search_path) / module_file_name
                if potential_path.exists():
                    return importlib.util.spec_from_loader(fullname, sktLoader(str(potential_path)))

        # 3. Check specifically within the 'sutralang' directory if path is not informative
        # This helps when importing from a script outside the package
        # (like running math_example.skt from the project root)
        # NOTE: This uses the directory of the current file (sanskrit.py) as the package directory.
        sutralang_package_dir = Path(__file__).parent # Directory of sanskrit.py
        potential_path_in_sutralang = sutralang_package_dir / module_file_name
        if potential_path_in_sutralang.exists():
             return importlib.util.spec_from_loader(fullname, sktLoader(str(potential_path_in_sutralang)))

        # 4. Handle potential imports like `import sutralang.गणित` or `घटकः.गणित`
        if '.' in fullname:
             relative_path = Path(fullname.replace(".", "/") + ".skt")
             # Check relative to sutralang package dir (most common case for intra-package)
             full_path_in_sutralang = sutralang_package_dir.parent / relative_path # Go up one level from sanskrit.py
             if full_path_in_sutralang.exists():
                  return importlib.util.spec_from_loader(fullname, sktLoader(str(full_path_in_sutralang)))
             # Check relative to CWD (less common for package modules)
             if relative_path.exists():
                  return importlib.util.spec_from_loader(fullname, sktLoader(str(relative_path)))   

        return None # Module not found by this finder

# Activate the import hook globally
def activate_import_hook():
    # print("[DEBUG] activate_import_hook: Called")
    if not any(isinstance(finder, sktFinder) for finder in sys.meta_path):
        sys.meta_path.insert(0, sktFinder())
        # print("[DEBUG] activate_import_hook: sktFinder added to sys.meta_path")
    # else:
        # print("[DEBUG] activate_import_hook: sktFinder already in sys.meta_path")

# activate_import_hook() # Keep commented out

# Script runner
def run_sanskrit_file(file_path: str):
    # print("[PY_DEBUG] run_sanskrit_file: ENTERED") # Python native print
    # print(f"[DEBUG] run_sanskrit_file: Starting for {file_path}")
    activate_import_hook()

    module_name_to_clear = "गणित" 
    if module_name_to_clear in sys.modules:
        # print(f"--- Clearing '{module_name_to_clear}' from sys.modules cache ---")
        del sys.modules[module_name_to_clear]

    try:
        # print(f"[DEBUG] run_sanskrit_file: Reading code from {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            sanskrit_code = f.read()
        # print(f"[DEBUG] run_sanskrit_file: Translating code from {file_path}")
        translated_code = translate_sanskrit(sanskrit_code)
        
        if translated_code is None:
            # print(f"[DEBUG] run_sanskrit_file: Translation failed for {file_path}")
            print(f"Translation failed for {file_path}. Check syntax errors.")
            sys.exit(1) 
        
        # print(f"[DEBUG] run_sanskrit_file: Executing translated code from {file_path}")
        exec_globals = {
            "__name__": "__main__",
            "__file__": file_path, 
        }
        exec(compile(translated_code, file_path, "exec"), exec_globals)
        # print(f"[DEBUG] run_sanskrit_file: Finished execution for {file_path}")
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error during execution of {file_path}:\n{e}")
        # Potentially print traceback here for more detailed debugging
        # import traceback
        # traceback.print_exc()
        sys.exit(1)

# CLI entrypoint function
def main_cli():
    # print("[PY_DEBUG] main_cli: ENTERED") # Python native print
    # print("[DEBUG] main_cli: Called")
    activate_import_hook()
    # print(f"[DEBUG] main_cli: sys.argv = {sys.argv}") # RE-COMMENT THIS LINE
    if len(sys.argv) != 2:
        # print(f"[DEBUG] main_cli: Incorrect number of arguments.")
        print(f"Usage: {Path(sys.argv[0]).name} <file.skt>") 
        sys.exit(1) 
    else:
        file_to_run = sys.argv[1]
        # print(f"[DEBUG] main_cli: Calling run_sanskrit_file with {file_to_run}")
        run_sanskrit_file(file_to_run)

# Keep the traditional entry point for direct execution (optional but good practice)
if __name__ == "__main__":
    # print("[PY_DEBUG] __main__: ENTERED") # Python native print
    # print("[DEBUG] __main__: Block entered")
    main_cli()

# --- Transpiler Functionality ---

def transpile_sanskrit_file(input_path: str, output_path: str):
    """Translates a Sanskrit (.skt) file to a Python (.py) file."""
    activate_import_hook() # Ensure hook is active for potential imports during translation?
                           # Maybe not strictly needed for transpiling only, but harmless.
    try:
        with open(input_path, "r", encoding="utf-8") as infile:
            sanskrit_code = infile.read()
        
        translated_code = translate_sanskrit(sanskrit_code)
        
        if translated_code is None:
            print(f"Error: Translation failed for {input_path}. Cannot transpile.")
            sys.exit(1)

        # Ensure output directory exists (optional, but helpful)
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write(f"# -*- coding: utf-8 -*-\n" # Ensure UTF-8 for Python 2 compatibility (good practice)
                            f"# Transpiled from: {Path(input_path).name}\n\n")
            outfile.write(translated_code)
        
        print(f"Successfully transpiled '{input_path}' to '{output_path}'")

    except FileNotFoundError:
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error writing to output file {output_path}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during transpilation: {e}")
        sys.exit(1)

# CLI entrypoint function for transpiling
def transpile_cli():
    """Handles command-line arguments for the transpile command."""
    if len(sys.argv) != 3:
        # sys.argv[0] is the script name (e.g., 'sanskrit-transpile')
        # sys.argv[1] should be the input file
        # sys.argv[2] should be the output file
        print(f"Usage: {Path(sys.argv[0]).name} <input_file.skt> <output_file.py>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Basic validation of file extensions (optional)
    if not input_file.endswith(".skt"):
        print(f"Warning: Input file '{input_file}' does not end with .skt")
    if not output_file.endswith(".py"):
        print(f"Warning: Output file '{output_file}' does not end with .py")
        
    transpile_sanskrit_file(input_file, output_file) 