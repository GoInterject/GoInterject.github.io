# BUILDS A JSON LIST OF TITLE, URL, CONTENT
# ---------------------------------------------------------------
# Be sure to first build the doc site with 'bundle exec jekyll build' to update the _site
# Searches the gointerject.github.io/_site folder and subfolders for html files
# Extracts the title, url, and content
# Outputs as json file to gointerject.github.io/OUTPUT_FOLDER/OUTPUT_FILENAME
# Replaces strings in output file from OLD_STRINGS to NEW_STRINGS
# This script will iterate through all the pages and extract the front matter into an external file

# ---------------------------------------------------------------
import os
import yaml  # for parsing YAML front matter and saving the result
from page_directories import PageDirectories
from root_directory import get_root_dir

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = "_metadata" # relative to gointerject.github.io folder
OUTPUT_FILENAME = 'front_matter.yaml'

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_front_matter(file_path):
    """Extract front matter from a file content string."""

    with open(file_path, "r", encoding="utf-8") as file_handle:
        file_str = file_handle.read()

        if file_str.startswith("---"):
            end_idx = file_str.find("---", 3)  # Find the second occurrence of '---'
            if end_idx != -1:
                front_matter_str = file_str[3:end_idx]
                # Replace tabs with spaces to prevent YAML parsing errors
                front_matter_str = front_matter_str.replace("\t", "    ")  # Replace with 4 spaces (adjust as needed)
                try:
                    return yaml.safe_load(front_matter_str)
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML front matter in {file_path}:\n{str(e)}")
    return {}

# ---------------------------------------------------------------
def save_front_matter_to_file(output_file, front_matter_dict):
    """Save front matter dictionary to an external YAML file."""
    try:
        with open(output_file, "w", encoding="utf-8") as yaml_file:
            yaml.dump(front_matter_dict, yaml_file, allow_unicode=True)
    except IOError as e:
        print(f"Error saving front matter to file: {str(e)}")

# ---------------------------------------------------------------
def convert_to_url(file_path, root_folder):
    """Convert a local file path to a www.gointerject.com URL with .html extension."""
    relative_path = os.path.relpath(file_path, root_folder)  # Get relative path from root_folder
    web_url = os.path.join("www.docs.gointerject.com", relative_path)  # Prepend the base URL
    web_url = web_url.replace("\\", "/")  # Convert backslashes to forward slashes for URLs
    web_url = web_url.replace(".md", ".html")  # Change .md extension to .html
    return web_url

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    global_front_matter = {}
    root_folder = get_root_dir(4)

    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)
        if not os.path.exists(dir_path):
            continue

        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            if not file_name.endswith(".md"):
                continue

            with open(file_path, "r", encoding="utf-8") as file_handle:
                front_matter = extract_front_matter(file_path)
                web_url = convert_to_url(file_path, root_folder)
                global_front_matter[web_url] = front_matter

    # Ensure the output folder exists
    output_folder_path = os.path.join(root_folder, OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)

    # Define the output file path for saving the front matter
    output_file = os.path.join(root_folder, OUTPUT_FOLDER, OUTPUT_FILENAME)

    # Save the global front matter dictionary to an external YAML file
    save_front_matter_to_file(output_file, global_front_matter)
    print(f"  Front matter saved to {output_file}")

if __name__ == "__main__":
    main()
