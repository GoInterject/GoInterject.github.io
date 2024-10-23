import os

# BUILDS A LIST OF KEYWORDS
# ---------------------------------------------------------------
# searches folder/subfolder `folder_to_search`
# excludes folders in `folders_to_exclude`
# for files ending in `file_ext`
# retrieves list of keywords in file (list of words that are labeled as keywords in Jekyll front matter)
# removes dups, strips, sorts, lower case
# outputs as text file to `output_path`
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
folder_to_search = "D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io"
file_ext = ".md" # searches for files ending in this extension
folders_to_exclude = [
    "bApps"
]
output_filename = "keywords.txt"

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def search_files_for_keywords(folder_path, excluded_folders):
    result = []

    for root, dirs, files in os.walk(folder_path):
        # Exclude folders in the 'excluded_folders' list
        dirs[:] = [d for d in dirs if d not in excluded_folders]

        for file in files:
            if file.endswith(file_ext):
                file_path = os.path.join(root, file)
                keywords = extract_keywords(file_path)
                if keywords is not None:
                    result.extend(keywords)
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
        else:
            print("'keywords: ' not found in the file " + file_path)

# ---------------------------------------------------------------
# SCRIPT
# ---------------------------------------------------------------
# Get full path of the output file
script_directory = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(script_directory, output_filename)

# Get search results
search_result = search_files_for_keywords(folder_to_search, folders_to_exclude)
search_result = list(set(search_result)) # remove duplicates
search_result = [word.strip() for word in search_result] # strip leading and trailing white space
search_result = [word.lower() for word in search_result] # convert to lower case
search_result.sort()

# Open the file in write mode and write each word to a new line
with open(output, 'w') as file:
    for word in search_result:
        file.write(word + '\n')