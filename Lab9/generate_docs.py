import os
import pydoc

def generate_docs():
    """Generate HTML documentation for the project."""
    docs_dir = "docs"
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                module_name = os.path.join(root, file)[2:-3].replace("/", ".")
                html_file = os.path.join(docs_dir, *module_name.split(".")) + ".html"
                with open(html_file, "w", encoding="utf-8") as f:
                    pydoc.writedoc(module_name, f)
                print(f"Documentation generated for: {module_name}")

if __name__ == "__main__":
    generate_docs()