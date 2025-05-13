import code
import sys
import os # Needed for path manipulation

# --- Path Hack Start ---
# Get the directory containing this file (repl.py)
_repl_dir = os.path.dirname(__file__)
# Explicitly add this directory to sys.path
# This shouldn't be needed for a proper package install, but helps diagnose import issues.
if _repl_dir not in sys.path:
    sys.path.insert(0, _repl_dir)
# --- Path Hack End ---

# Need to import the translator from the main module
from sutralang.sanskrit import translate_sanskrit, activate_import_hook

BANNER = """
🕉️ Welcome to the SutraLang Interactive Console! 🕉️
(Based on Python {})
Type SutraLang code (using Sanskrit keywords) and press Enter.
Type help() for help on Python objects, or exit() to exit.
""".format(sys.version.split()[0])

class SutraLangConsole(code.InteractiveConsole):
    """A subclass of InteractiveConsole that translates Sanskrit input."""
    def __init__(self, locals=None, filename="<console>"):
        super().__init__(locals=locals, filename=filename)
        # Ensure the .skt import hook is active for the console session
        activate_import_hook()
        # You might want to pre-populate the locals with common functions
        # or leave it standard.

    def runsource(self, source, filename="<input>", symbol="single"):
        """Compile and run source code fragment, translating it first."""
        # First, try to translate the source
        translated_source = translate_sanskrit(source)

        if translated_source is None:
            # If translation fails (e.g., syntax error in keywords),
            # display an error. InteractiveConsole doesn't handle this well.
            # We can potentially improve error reporting here later.
            self.showsyntaxerror(filename)
            return False # Indicate error

        # If translation succeeded, run the *translated* code using the
        # standard InteractiveConsole mechanism.
        # This handles multi-line input buffering, code compilation, execution,
        # and error display (for runtime Python errors).
        return super().runsource(translated_source, filename, symbol)

def start_repl():
    """Starts the SutraLang REPL."""
    console = SutraLangConsole()
    console.interact(banner=BANNER)

# Entry point for direct execution (though typically run via CLI script)
if __name__ == "__main__":
    start_repl() 