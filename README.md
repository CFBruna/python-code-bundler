# Python Code Bundler

A simple Python utility that bundles all source code files from a project into a single, clean HTML file. This makes it easy to analyze, share, or print the entire codebase to a PDF.

## Motivation

This tool was created to solve a common workflow challenge: gathering all source code from a project for analysis or review. Specifically, it's designed to streamline the process of feeding an entire codebase into Large Language Models (LLMs) like Google's NotebookLM for in-depth study, refactoring, or documentation generation.

## How to Use

### 1. Using the Executable (Windows)

This is the easiest method and does not require a Python installation.

1.  Download the `code_bundler.exe` file from the repository.
2.  Double-click the file to run it.
3.  Follow the on-screen dialogs:
    * First, select the root folder where your projects are located (e.g., `D:\Projects`).
    * Next, type the specific folder name of the project you want to bundle.
    * Finally, provide a display name for the project title.
4.  The script will generate an `.html` file in the same directory as the executable and open it in your default web browser.
5.  In the browser, press `Ctrl + P` and select "Save as PDF".

### 2. Running the Python Script

Requires Python 3 to be installed.

1.  Clone this repository.
2.  Navigate to the project's directory in your terminal.
3.  Run the command: `python code_bundler.py`
4.  Follow the on-screen instructions.

## Development

To generate the executable from the source code, `PyInstaller` is required.

```bash
pip install pyinstaller

pyinstaller --onefile --noconsole code_bundler.py
```

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
