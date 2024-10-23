import os
import json
from bs4 import BeautifulSoup

# BUILDS A JSON LIST OF URL : TITLE
# ---------------------------------------------------------------
# searches folder/subfolder `folder_to_search`
# excludes folders in `folders_to_exclude`
# for files ending in `file_ext`
# retrieves titles from the html pages
# outputs as json file to support_assistant\data\output_filename
# replaces strings in output file from `old_strings` to `new_strings`
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
folder_to_search = "D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io\\_site"
file_ext = ".html" # searches for files ending in this extension
folders_to_exclude = [
    "bApps"
    ,"fonts"
    ,"schemas"
]
output_filename = "titles_url.json"

# replace words in the result json list
old_strings = [
    "D:\\\\Users\\\\samuelr\\\\Documents\\\\GitHub\\\\GoInterject.github.io\\\\_site\\\\"
    ,"\\\\"
    ," | Interject Documentation Site"
]

new_strings = [
    "https://docs.gointerject.com/"
    ,"/"
    ,""
]

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_title_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        title_tag = soup.find('title')

        if title_tag:
            return title_tag.text.strip()

    except Exception as e:
        print(f"Error extracting title from {file_path}: {e}")

    return None

# ---------------------------------------------------------------
def traverse_and_extract_titles(base_path, excluded_folders):
    title_list = {}

    for root, dirs, files in os.walk(base_path):

        # Exclude folders in the 'excluded_folders' list
        dirs[:] = [d for d in dirs if d not in excluded_folders]
        excluded_folders_found = set(excluded_folders) & set(dirs)
        for excluded_folder in excluded_folders_found:
            dirs.remove(excluded_folder)

        for file in files:
            if file.endswith(".html"):  # Adjust based on your file extensions
                file_path = os.path.join(root, file)
                title = extract_title_from_file(file_path)

                if title:
                    title_list[title] = file_path

    return title_list

# ---------------------------------------------------------------
def replace_string_in_file(file_path, old_string, new_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        modified_content = content.replace(old_string, new_string)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Replacement successful in {file_path}")

    except Exception as e:
        print(f"Error replacing string in {file_path}: {e}")

# ---------------------------------------------------------------
# SCRIPT
# ---------------------------------------------------------------
# Get full path of the output file
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
data_folder = os.path.join(parent_directory, os.pardir, 'data')
output = os.path.join(data_folder, output_filename)

titles_and_files = traverse_and_extract_titles(folder_to_search, folders_to_exclude)

# Save the JSON list
with open(output, "w") as json_file:
    json.dump(titles_and_files, json_file, indent=2)

# Replace strings in the file
for i in range(len(old_strings)):
    replace_string_in_file(output, old_strings[i], new_strings[i])
