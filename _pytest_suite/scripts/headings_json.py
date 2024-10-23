import os
import json
from bs4 import BeautifulSoup

# BUILDS A JSON LIST OF URL : HEADINGS
# ---------------------------------------------------------------
# searches folder/subfolder `folder_to_search`
# excludes folders in `folders_to_exclude`
# for files ending in `file_ext`
# extracts the text tagged with html `tags_to_search`
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
]
tags_to_search = ['h1', 'h2', 'h3', 'h4']
output_filename = "url_headings.json"

# replace words in the result json list
old_strings = [
    "D:\\\\Users\\\\samuelr\\\\Documents\\\\GitHub\\\\GoInterject.github.io\\\\_site\\\\"
    ,"\\\\"
]

new_strings = [
    "https://docs.gointerject.com/"
    ,"/"
]

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_subjects_from_html(html_content):
    subjects = []
    soup = BeautifulSoup(html_content, 'html.parser')

    for heading in soup.find_all(tags_to_search):
        subject = heading.text.strip()
        subjects.append(subject)

    return subjects

# ---------------------------------------------------------------
def generate_json_list(base_path, excluded_folders):
    json_list = {"topics": []}

    for root, dirs, files in os.walk(base_path):

        for root, dirs, files in os.walk(base_path):
            # Exclude folders in the 'excluded_folders' list
            dirs[:] = [d for d in dirs if d not in excluded_folders]

        for file in files:
            if file.endswith(file_ext): 
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    html_content = file_content.read()
                    subjects = extract_subjects_from_html(html_content)

                    if subjects:
                        #category = os.path.abspath(file_path).replace(os.path.sep, '/')
                        category = os.path.join(root,file)
                        json_list["topics"].append({
                            "name": category,
                            "subjects": subjects
                        })

    return json_list

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
generated_json_list = generate_json_list(folder_to_search, folders_to_exclude)

# Get full path of the output file
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
data_folder = os.path.join(parent_directory, os.pardir, 'data')
output = os.path.join(data_folder, output_filename)

# Save the generated JSON list
with open(output, "w") as json_file:
    json.dump(generated_json_list, json_file, indent=2)

# Replace strings in the file
for i in range(len(old_strings)):
    replace_string_in_file(output, old_strings[i], new_strings[i])
