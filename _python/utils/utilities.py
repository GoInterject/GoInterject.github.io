# COMMON FUNCTIONS USED BY EXTRACTION AND UPDATE SCRIPTS
# ---------------------------------------------------------------
import yaml
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import ROOT_FOLDER

# ---------------------------------------------------------------
# Traverses through the folder directories in doc_page_folder_list
# For each md file in these folders, runs the process_md_file method
def process_folder(root_folder, PageDirectories, process_md_file):
    for folder in PageDirectories:
        dir_path = Path(root_folder) / folder.value
        if not dir_path.exists():
            continue

        for file_path in dir_path.iterdir():
            if not file_path.suffix == ".md":
                continue

            with file_path.open("r", encoding="utf-8") as file_handle:
                process_md_file(file_path)

# ---------------------------------------------------------------
# Converts a local file path to the url equivalent
# e.g.:
# root_folder: D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io
# file_path: D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io\\wAbout\\Basics-of-Report-Formulas.md
# url: www.gointerject.github.io/wAbout/Basics-of-Report-Formulas.html
def convert_filepath_to_url(file_path):
    """Convert a local file path to a www.gointerject.com URL with .html extension."""
    relative_path = Path(file_path).relative_to(ROOT_FOLDER)  # Get relative path from root_folder
    web_url = Path("https://docs.gointerject.com") / relative_path  # Prepend the base URL
    web_url = str(web_url).replace("\\", "/")  # Convert backslashes to forward slashes for URLs
    web_url = web_url.replace(".md", ".html")  # Change .md extension to .html
    return web_url

# ---------------------------------------------------------------
# Converts a url to local file path equivalent
# e.g.:
# root_folder: D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io
# url: www.gointerject.github.io/wAbout/Basics-of-Report-Formulas.html
# file_path: D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io\\wAbout\\Basics-of-Report-Formulas.md
def convert_url_to_file_path(url):
    """Convert a www.gointerject.com URL with .html extension to a local file path."""
    # Remove base URL and convert slashes for file path
    relative_path = url.replace("https://docs.gointerject.com/", "").replace("/", Path().sep)
    # Change .html extension back to .md
    relative_path = relative_path.replace(".html", ".md")
    # Combine with root folder to get full file path
    file_path = Path(ROOT_FOLDER) / relative_path
    return file_path

# ---------------------------------------------------------------
def extract_front_matter(file_str):
    """Extract front matter from a file content string."""
    if file_str.startswith("---"):
        end_idx = file_str.find("---", 3)  # Find the second occurrence of '---'
        if end_idx != -1:
            front_matter_str = file_str[3:end_idx]
            # Replace tabs with spaces to prevent YAML parsing errors
            front_matter_str = front_matter_str.replace("\t", "    ")  # Replace with 4 spaces (adjust as needed)
            try:
                return yaml.safe_load(front_matter_str)
            except yaml.YAMLError as e:
                print(f"PARSE: Error parsing YAML front matter: {str(e)}")
    return {}

# ---------------------------------------------------------------
def extract_front_matter_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file_handle:
        file_str = file_handle.read()

    return extract_front_matter(file_str)
