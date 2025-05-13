<h1 align="center">ℹ️ About SutraLang ℹ️</h1>

<p align="center">
    <em>A concise guide to the SutraLang project for collaborators and AI assistants.</em>
</p>

## 🎯 Project Goal

SutraLang enables writing Python code using Devanagari script with intuitive Sanskrit keywords. The project transpiles custom `.skt` files, which use this Sanskrit-based syntax, into standard, executable Python code. The aim is to provide an alternative way to express Python logic, potentially making it more accessible or engaging for those familiar with Sanskrit.

## 🔑 Key Features

*   **Sanskrit-based Syntax:** Python logic expressed using Sanskrit keywords and function names.
*   **Transpilation to Python:** `.skt` files are converted into runnable `.py` files.
*   **Direct Execution:** Run `.skt` files directly using a command-line tool.
*   **Interactive REPL:** An interactive console for live coding with Sanskrit keywords.
*   **Modular Design:** Supports importing standard Python modules and other `.skt` modules (including wrapped standard libraries).
*   **Custom Import Hook:** Allows seamless importing of `.skt` files.

## 📂 Project Structure

```
.
├── ABOUT.md                # This file: Project overview for collaborators/AI.
├── Docs/
│   ├── DOCUMENTATION.md    # Detailed mappings of Sanskrit to Python keywords/functions.
│   └── FUTURE_PLANS.md     # Ideas for future development.
├── examples/               # Example .skt scripts showcasing various features.
│   ├── devanagari_example.skt
│   ├── greeting_example.skt
│   ├── math_example.skt
│   ├── random_example.skt
│   └── time_example.skt
├── घटकः/                   # "Components" - Directory for wrapped .skt modules.
│   ├── गणित.skt            # Wrapper for Python's math module.
│   ├── नियोग_देवनागरीलिपौ_सञ्चिका.skt # Devanagari script validator.
│   ├── समय.skt             # Wrapper for Python's datetime module.
│   └── यादृच्छिक.skt         # Wrapper for Python's random module.
├── LICENSE                 # MIT License file.
├── pyproject.toml          # Project metadata, dependencies, and script entry points.
├── README.md               # Main README for users.
├── sutralang/              # Main package directory for SutraLang.
│   ├── __init__.py         # Makes sutralang a Python package.
│   ├── mappings.py         # Core Sanskrit-to-Python keyword/function dictionary.
│   ├── repl.py             # Implements the interactive REPL (sutralang-console).
│   └── sanskrit.py         # Core transpiler logic, import hook, and CLI runners.
└── .gitignore              # Specifies intentionally untracked files for Git.
```

## 🛠️ Core Components & How It Works

1.  **`sutralang/mappings.py`:**
    *   This is the heart of the translation, containing a Python dictionary (`sanskrit_keywords`) that maps Sanskrit terms to their Python equivalents (e.g., `"यदि": "if"`, `"छापय": "print"`).

2.  **`sutralang/sanskrit.py`:**
    *   `translate_sanskrit(code_string)`: This function takes a string of SutraLang code (from a `.skt` file or REPL input).
        *   It first handles the custom `मानम्` assignment keyword (e.g., `मानम् x = 10` becomes `x = 10`) through string manipulation to preserve indentation.
        *   Then, it tokenizes the (potentially modified) code and iterates through tokens, replacing known Sanskrit keywords/identifiers from `mappings.py` with their Python counterparts.
        *   The translated tokens are untokenized back into a Python code string.
        *   `parse_syntax(translated_code)`: This function attempts to parse the translated code using `ast.parse()` to validate its Python syntax. If it fails, it indicates an error in the translated code.
    *   `sktLoader` & `sktFinder`: These classes implement a custom Python import hook.
        *   `sktFinder` is added to `sys.meta_path` and looks for `.skt` files when an import statement is encountered.
        *   If a `.skt` file is found, `sktLoader` reads its content, passes it to `translate_sanskrit`, and then the Python interpreter executes the translated Python code.
        *   This allows `import घटकः.गणित` or even `import your_module` (if `your_module.skt` exists).
    *   `main_cli()`: Entry point for `sutralang-run` command. Reads a `.skt` file, translates it, and executes it.
    *   `transpile_cli()`: Entry point for `sutralang-transpile` command. Reads a `.skt` file, translates it, and saves the result to a `.py` file.

3.  **`sutralang/repl.py`:**
    *   `SutraLangConsole`: A subclass of `code.InteractiveConsole`.
    *   It overrides `runsource` to pass the user's input (Sanskrit code) through `translate_sanskrit` before executing it.
    *   `start_repl()`: Entry point for the `sutralang-console` command.

4.  **`घटकः/` (Components Directory):**
    *   This directory, located at the project root, holds `.skt` files that act as wrappers around standard Python libraries (e.g., `घटकः/गणित.skt` for `math`).
    *   These modules typically import the corresponding Python module using an alias (e.g., `आयात math नाम्ना _गणित`) and then define Sanskrit functions/constants that call the aliased Python module's features.
    *   They are imported in other `.skt` files or the REPL using, for example, `यतः घटकः.गणित आयात पाई`.

5.  **`pyproject.toml`:**
    *   Defines the project name as "SutraLang".
    *   Sets up the command-line scripts:
        *   `sutralang-run`: Executes `.skt` files.
        *   `sutralang-transpile`: Converts `.skt` to `.py`.
        *   `sutralang-console`: Starts the interactive REPL.

## 📜 Workflow Example

1.  User creates `my_program.skt`:
    ```sanskrit
    मानम् संख्या = 10
    यदि संख्या > 5 च संख्या < 15:
        छापय("संख्या योग्यमस्ति।")  # "Number is valid."
    अथ:
        छापय("संख्या अयोग्यमस्ति।") # "Number is invalid."
    ```
2.  User runs: `sutralang-run my_program.skt`
3.  `sanskrit.py:main_cli` is invoked.
4.  The import hook is activated.
5.  `my_program.skt` is read.
6.  `translate_sanskrit` converts the code to:
    ```python
    संख्या = 10
    if संख्या > 5 and संख्या < 15:
        print("संख्या योग्यमस्ति।")
    else:
        print("संख्या अयोग्यमस्ति।")
    ```
7.  The translated Python code is executed.

## 💡 Key Design Choices & Notes

*   **`मानम्` Keyword:** Handled via string manipulation before tokenization to correctly manage indentation and the assignment structure.
*   **Import Hook (`sktFinder`/`sktLoader`):** Crucial for allowing `.skt` files to be imported like regular Python modules and for enabling the wrapped modules in `घटकः/`.
*   **Filename Encoding:** While `.skt` files can contain Devanagari, script files intended to be directly executed by the `sutralang-run` command (or as entry points) are more reliably named using ASCII characters due to potential terminal/OS encoding issues (e.g., `math_example.skt` instead of `गणित_उदाहरण.skt`). File *content* always supports Devanagari.
*   **Project Name Evolution:** The project was formerly known as "SutraPy" and was renamed to "SutraLang" to better reflect its nature as a distinct way of expressing code, similar to other "Lang" projects (e.g., Bhai Lang).

This `ABOUT.md` should help in quickly getting up to speed with the SutraLang project. 
