import os
import html
import webbrowser
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import sys


def get_script_directory():
    """Returns the directory where the script or the executable is located."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


def create_code_bundle():
    """
    Asks for project info, bundles all source code into an HTML file,
    and opens it in the browser for printing to PDF.
    """
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo(
        "Step 1 of 3",
        "First, please select the root folder where all your projects are stored (e.g., D:\\Projects).",
    )
    base_path = filedialog.askdirectory(title="Select your projects' root folder")

    if not base_path:
        messagebox.showinfo("Cancelled", "Operation cancelled.")
        return

    project_folder_name = simpledialog.askstring(
        "Step 2 of 3", "Enter the project's FOLDER name (e.g., petcare_project):"
    )
    if not project_folder_name:
        messagebox.showinfo("Cancelled", "Operation cancelled.")
        return

    project_name = simpledialog.askstring(
        "Step 3 of 3", "Enter the project's display name for the title (e.g., PetCare):"
    )
    if not project_name:
        messagebox.showinfo("Cancelled", "Operation cancelled.")
        return

    project_path = os.path.join(base_path, project_folder_name)
    output_filename_html = f"{project_folder_name}_source_code.html"
    output_filepath_html = os.path.join(get_script_directory(), output_filename_html)
    project_title = f"{project_name} - Complete Source Code"

    if not os.path.isdir(project_path):
        messagebox.showerror(
            "Error", f"The project folder '{project_path}' was not found!"
        )
        return

    try:
        with open(output_filepath_html, "w", encoding="utf-8") as outfile:
            outfile.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
            outfile.write('<meta charset="UTF-8">\n')
            outfile.write(f"<title>{html.escape(project_title)}</title>\n")
            outfile.write(
                "<style>body { font-family: sans-serif; } h1, h2 { border-bottom: 2px solid #ccc; padding-bottom: 5px; margin-top: 2em;} pre { background-color: #f4f4f4; padding: 10px; border: 1px solid #ddd; white-space: pre-wrap; word-wrap: break-word; }</style>\n"
            )
            outfile.write("</head>\n<body>\n")
            outfile.write(f"<h1>{html.escape(project_title)}</h1>\n")

            include_extensions = [
                ".py",
                ".html",
                ".css",
                ".js",
                ".yml",
                ".conf",
                ".sh",
                "Dockerfile",
                ".toml",
                ".ini",
                ".md",
            ]
            exclude_folders = [
                "__pycache__",
                ".venv",
                "venv",
                ".git",
                "staticfiles",
                "media",
                "dist",
                "build",
            ]

            for root_dir, dirs, files in os.walk(project_path):
                dirs[:] = [d for d in dirs if d not in exclude_folders]
                for filename in sorted(files):
                    if (
                        any(filename.endswith(ext) for ext in include_extensions)
                        or filename == "Dockerfile"
                    ):
                        file_path = os.path.join(root_dir, filename)
                        relative_path = os.path.relpath(file_path, project_path)
                        outfile.write(
                            f"<h2>--- FILE: {html.escape(relative_path)} ---</h2>\n"
                        )
                        outfile.write("<pre>\n")
                        try:
                            with open(
                                file_path, "r", encoding="utf-8", errors="ignore"
                            ) as infile:
                                content = infile.read()
                                outfile.write(html.escape(content))
                        except Exception as e:
                            outfile.write(f"Error reading file: {e}")
                        outfile.write("</pre>\n")

            outfile.write("</body>\n</html>")

        webbrowser.open(f"file://{os.path.realpath(output_filepath_html)}")

        messagebox.showinfo(
            "Success!",
            "The HTML file has been generated and opened in your browser.\n\n"
            "Now, please press 'Ctrl + P' and choose 'Save as PDF'.",
        )

    except Exception as e:
        messagebox.showerror(
            "Unexpected Error", f"An error occurred while generating the file:\n\n{e}"
        )


if __name__ == "__main__":
    create_code_bundle()
