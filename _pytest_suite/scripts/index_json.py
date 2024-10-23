import os
import json

# BUILDS A JSON LIST OF INDEX WORD : URLS
# ---------------------------------------------------------------
# searches folder/subfolder `folder_to_search`
# excludes folders in `folders_to_exclude`
# for files ending in `file_ext`
# searches for index strings defined in `index_input_file` (separated by newline)
# outputs as json file to support_assistant\data\output_filename
# replaces strings in output file from `old_strings` to `new_strings`
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
folder_to_search = "D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io"
file_ext = ".md" # searches for files ending in this extension
folders_to_exclude = [
    "bApps"
]
output_filename = "index_urls.json"

# the input file of keywords to search for
index_input_filename = "index.csv"

# replace words in the result json list
old_strings = [
    "D:\\\\Users\\\\samuelr\\\\Documents\\\\GitHub\\\\GoInterject.github.io\\\\"
    ,"\\\\"
    ,".md"
]

new_strings = [
    "https://docs.gointerject.com/"
    ,"/"
    ,".html"
]

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def search_files_for_keywords(folder_path, keywords, excluded_folders):
    result = {}

    def search_in_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()  # Convert to lowercase for case-insensitive matching

            for keyword in keywords:
                if keyword.lower() in content:
                    result.setdefault(keyword, []).append(file_path)

    for root, dirs, files in os.walk(folder_path):
        # Exclude folders in the 'excluded_folders' list
        dirs[:] = [d for d in dirs if d not in excluded_folders]

        for file in files:
            if file.endswith(file_ext):
                file_path = os.path.join(root, file)
                search_in_file(file_path)

    return result

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
def extract_words(file_path):
    words = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words.append(line.strip())

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return words

# ---------------------------------------------------------------
def sort_json_file(file_path):
    # Read the JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Sort the dictionary by keys
    sorted_data = dict(sorted(data.items()))

    # Write the sorted dictionary back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(sorted_data, json_file, indent=2)

# ---------------------------------------------------------------
# SCRIPT
# ---------------------------------------------------------------
# Get full path of the output file
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
data_folder = os.path.join(parent_directory, os.pardir, 'data')
output = os.path.join(data_folder, output_filename)
keyword_path = os.path.join(script_directory, index_input_filename)

# Get the list of keywords
keywords_to_search = extract_words(keyword_path)

# Get search results
search_result = search_files_for_keywords(folder_to_search, keywords_to_search, folders_to_exclude)

# Save the result to a JSON file
with open(output, "w") as json_file:
    json.dump(search_result, json_file, indent=2)

# Replace strings in the file
for i in range(len(old_strings)):
    replace_string_in_file(output, old_strings[i], new_strings[i])

# Sort json file by keys
sort_json_file(output)