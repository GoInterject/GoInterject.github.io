# Traverses through the folder directories in doc_page_folder_list
# For each md file in these folders, runs the process_md_file method

import os

# ---------------------------------------------------------------
def process_folder(root_folder, PageDirectories, process_md_file):
    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)
        if not os.path.exists(dir_path):
            continue

        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            if not file_name.endswith(".md"):
                continue

            with open(file_path, "r", encoding="utf-8") as file_handle:
                process_md_file(file_path)

# ---------------------------------------------------------------
# Converts a local file path to the url equivalent
# e.g.:
# root_folder: D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io
# file_path: D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io\\wAbout\\Basics-of-Report-Formulas.md
# www.gointerject.github.io/wAbout/Basics-of-Report-Formulas.html
def convert_filepath_to_url(file_path, root_folder):
    """Convert a local file path to a www.gointerject.com URL with .html extension."""
    relative_path = os.path.relpath(file_path, root_folder)  # Get relative path from root_folder
    web_url = os.path.join("www.docs.gointerject.com", relative_path)  # Prepend the base URL
    web_url = web_url.replace("\\", "/")  # Convert backslashes to forward slashes for URLs
    web_url = web_url.replace(".md", ".html")  # Change .md extension to .html
    return web_url

# ---------------------------------------------------------------
def convert_url_to_file_path(url, root_folder):
    """Convert a www.gointerject.com URL with .html extension to a local file path."""
    # Remove base URL and convert slashes for file path
    relative_path = url.replace("www.docs.gointerject.com/", "").replace("/", os.sep)
    # Change .html extension back to .md
    relative_path = relative_path.replace(".html", ".md")
    # Combine with root folder to get full file path
    file_path = os.path.join(root_folder, relative_path)
    return file_path
