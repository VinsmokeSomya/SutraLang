<h1 align="center" id="top">🕉️ SutraLang: Write Python in Sanskrit! 🚩</h1>

<p align="center">
    <em>
        (Sūtra [सूत्र]: A Sanskrit term meaning "string" or "thread," referring to an aphorism or a collection of concise rules.)
    </em>
</p>

[![GitHub license](https://img.shields.io/github/license/VinsmokeSomya/SutraLang)](https://github.com/VinsmokeSomya/SutraLang/blob/main/LICENSE)

SutraLang allows you to write Python code using Devanagari script with intuitive Sanskrit keyword mappings. This project translates `.skt` files containing this Sanskrit-based syntax into standard Python code, which can then be executed or saved.

---

## ✨ Features

*   **Sanskrit Syntax:** Write Python logic using familiar Sanskrit terms.
*   **Seamless Integration:** Import standard Python modules or other `.skt` modules.
*   **Compatibility:** Uses standard Python execution environments.
*   **Transpilation:** Option to convert `.skt` files directly into standard `.py` files.
*   **Interactive Console (REPL):** Experiment with SutraLang code interactively.

---

## 📂 Project Structure

```
.
│
├── Docs/
│   ├── DOCUMENTATION.md        # Detailed mappings of Sanskrit to Python keywords/functions.
│   ├── ABOUT.md                # Project overview for collaborators/AI.
│   └── FUTURE_PLANS.md         # Ideas for future development.
├── examples/                   # Example .skt scripts showcasing various features.
│   ├── devanagari_example.skt
│   ├── greeting_example.skt
│   ├── math_example.skt
│   ├── random_example.skt
│   └── time_example.skt
├── घटकः/                       # "Components" - Directory for wrapped .skt modules.
│   ├── गणित.skt                # Wrapper for Python's math module.
│   ├── नियोग_देवनागरीलिपौ_सञ्चिका.skt # Devanagari script validator.
│   ├── समय.skt                 # Wrapper for Python's datetime module.
│   └── यादृच्छिक.skt             # Wrapper for Python's random module.
├── LICENSE                     # MIT License file.
├── pyproject.toml              # Project metadata, dependencies, and script entry points.
├── README.md                   # Main README for users (this file).
├── sutralang/                  # Main package directory for SutraLang.
│   ├── __init__.py             # Makes sutralang a Python package.
│   ├── mappings.py             # Core Sanskrit-to-Python keyword/function dictionary.
│   ├── repl.py                 # Implements the interactive REPL (sutralang-console).
│   └── sanskrit.py             # Core transpiler logic, import hook, and CLI runners.
└── .gitignore                  # Specifies intentionally untracked files for Git.
```

---

## 💾 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/VinsmokeSomya/SutraLang.git
    cd SutraLang
    ```
2.  Install the package in editable mode:
    ```bash
    pip install -e .
    ```

---

## 🚀 Usage

1.  Write your code using Sanskrit keywords (see [Full Documentation](Docs/DOCUMENTATION.md) for mappings).
2.  Save the file with a `.skt` extension (e.g., `कार्यक्रमः.skt`).
3.  **Run a file directly:**
    ```bash
    sutralang-run कार्यक्रमः.skt
    ```
4.  **Transpile to a standard Python file:**
    ```bash
    sutralang-transpile कार्यक्रमः.skt output.py
    ```
5.  **Launch the Interactive Console (REPL):**
    ```bash
    sutralang-console
    ```

---

## 📖 Documentation

For a complete list of Sanskrit keyword and function mappings, please see:

➡️ **[DOCUMENTATION.md](Docs/DOCUMENTATION.md)**

---

## 🙌 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/VinsmokeSomya/SutraLang/issues).

---

## 📜 License

Copyright © 2025 Vinsmoke Somya.
This project is [MIT](LICENSE) licensed.
