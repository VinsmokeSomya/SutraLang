<h1 align="center">🚀 SutraLang: Future Plans 🚀</h1>

<p align="center">
    <strong>
        This document outlines potential future features, enhancements, and ideas for the SutraLang project.
    </strong>
</p>

## 📖 Table of Contents

*   [💡 Core Language Features & Transpiler Enhancements](#core-language-features--transpiler-enhancements)
*   [📚 More Standard Library Wrappers](#more-standard-library-wrappers)
*   [🛠️ Tooling & Developer Experience](#tooling--developer-experience)
*   [🌐 Community & Ecosystem](#community--ecosystem)
*   [🧪 Experimental Ideas](#experimental-ideas)

---

## 💡 Core Language Features & Transpiler Enhancements

*   **Advanced Data Structures:**
    *   Sanskrit keywords for advanced collection types (e.g., `collections.deque`, `collections.OrderedDict`).
    *   Consideration for list comprehensions, dictionary comprehensions with Sanskrit syntax.
*   **Object-Oriented Programming (OOP) Enhancements:**
    *   More idiomatic Sanskrit terms for class inheritance, super(), decorators (`@staticmethod`, `@classmethod`, `@property`).
    *   Metaclasses with Sanskrit syntax.
*   **Asynchronous Programming:**
    *   Refine keywords for `async` and `await` if needed.
    *   Wrappers for `asyncio` module features.
*   **Error Reporting:**
    *   More detailed error messages from the transpiler, pinpointing issues in the original `.skt` file and suggesting Sanskrit-based corrections.
    *   Source mapping to allow debuggers to step through `.skt` code.
*   **Performance:**
    *   Optimization of the translation process.
*   **Type Hinting:**
    *   A system for type hinting using Sanskrit terms, compatible with Python's type hinting.

## 📚 More Standard Library Wrappers

Expand the `घटकः` (components) or create new top-level wrapped modules for:

*   **File System Operations:** (`os`, `pathlib`) - e.g., `सञ्चिका_प्रणाली` (File System)
    *   Keywords for reading, writing, deleting files and directories.
    *   Path manipulation.
*   **Networking:** (`socket`, `http.client` or `requests` if added as a dependency) - e.g., `अन्तर्जालम्` (Internet)
*   **String Manipulation & Regex:** (`re`, `string`) - e.g., `अक्षरसमूह_प्रक्रिया` (String Processing)
*   **JSON/XML Processing:** (`json`, `xml.etree.ElementTree`) - e.g., `दत्तांश_विनिमयः` (Data Exchange)
*   **Multithreading/Multiprocessing:** (`threading`, `multiprocessing`) - e.g., `बहुकार्यम्` (Multitasking)
*   **Logging:** (`logging`) - e.g., `विवरणिका` (Log/Chronicle)
*   **Unit Testing:** (`unittest`, `pytest` if integrated) - e.g., `परीक्षणम्` (Testing)
*   **Argument Parsing:** (`argparse`) for CLI tools - e.g., `तर्क_विश्लेषणम्` (Argument Analysis)
*   **GUI Development:** (e.g., a wrapper for parts of `tkinter` or suggestions for using with other GUI libs) - e.g., `चित्रफलकम्` (Canvas/Screen)

## 🛠️ Tooling & Developer Experience

*   **Linter/Formatter for `.skt` files:** A tool to check `.skt` code for style and potential issues before transpilation.
*   **Syntax Highlighting:**
    *   Develop and distribute syntax highlighting extensions for popular code editors (VS Code, Sublime Text, etc.).
*   **Debugger Integration:** Better integration with Python debuggers to show `.skt` source code.
*   **Interactive SutraLang Shell (REPL):**
    *   Further enhancements to the existing `sutralang-console`.
    *   Auto-completion of Sanskrit keywords.
    *   History.
*   **Package Management:** Clear guidelines on how to structure larger SutraLang projects and manage dependencies.
*   **Documentation Generation:** Tools to auto-generate documentation from `.skt` files (e.g., docstrings in Sanskrit).

## 🌐 Community & Ecosystem

*   **Website/Wiki:** A dedicated place for documentation, tutorials, and community resources.
*   **Example Repository:** A collection of more complex examples and small projects written in SutraLang.
*   **Contribution Guidelines:** Clear guidelines for community contributions.
*   **Outreach:** Promoting SutraLang in relevant communities (Sanskrit enthusiasts, programming language hobbyists).

## 🧪 Experimental Ideas

*   **Domain-Specific Extensions:**
    *   SutraLang for specific domains like Ayurveda, Yoga philosophy, or Vedic studies, with specialized keywords and libraries.
*   **Direct Devanagari Input for Identifiers:**
    *   Explore robust ways to allow Devanagari script for variable and function names beyond simple keyword translation if Python's own capabilities evolve or if a pre-processing step can reliably handle it.
*   **Interoperability with other Indic languages:** Explore concepts for extending the idea to other related languages.

---

*This list is a starting point and will evolve. Feel free to suggest more ideas!* 