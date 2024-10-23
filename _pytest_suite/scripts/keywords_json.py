import os
import json

# BUILDS A JSON LIST OF URL : KEYWORDS
# ---------------------------------------------------------------
# searches folder/subfolder `folder_to_search`
# excludes folders in `folders_to_exclude`
# for files ending in `file_ext`
# retrieves list of keywords in file (list of words that are labeled as keywords in Jekyll front matter)
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
output_filename = "url_keywords.json"

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
def search_files_for_keywords(folder_path, excluded_folders):
    result = {}

    for root, dirs, files in os.walk(folder_path):
        # Exclude folders in the 'excluded_folders' list
        dirs[:] = [d for d in dirs if d not in excluded_folders]

        for file in files:
            if file.endswith(file_ext):
                file_path = os.path.join(root, file)
                keywords = extract_keywords(file_path)
                if keywords is not None:
                    result[file_path] = keywords
                # print(keywords)

    return result

# ---------------------------------------------------------------
def extract_keywords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # Find the index of the first occurrence of "keywords: "
        keywords_index = content.find("keywords: ")

        if keywords_index != -1:
            # Extract characters after "keywords: " up to the first newline
            start_index = keywords_index + len("keywords: ")
            end_index = content.find('\n', start_index)

            if end_index != -1:
                keywords = content[start_index:end_index].strip('[]').split(', ')
                return keywords
            else:
                print("No newline found after 'keywords: '")
                return [""]
        else:
            print("'keywords: ' not found in the file " + file_path)
            return [""]

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
                # Split each line into words
                line_words = line.split()
                # Extend the list of words with the words from the current line
                words.extend(line_words)

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return words

# ---------------------------------------------------------------
# SCRIPT
# ---------------------------------------------------------------
# Get full path of the output file
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
data_folder = os.path.join(parent_directory, os.pardir, 'data')
output = os.path.join(data_folder, output_filename)

# Get search results
search_result = search_files_for_keywords(folder_to_search, folders_to_exclude)

# Save the result to a JSON file
with open(output, "w") as json_file:
    json.dump(search_result, json_file, indent=2)

# Replace strings in the file
for i in range(len(old_strings)):
    replace_string_in_file(output, old_strings[i], new_strings[i])
