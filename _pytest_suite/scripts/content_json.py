import os
from bs4 import BeautifulSoup
import json
import html2text

# BUILDS A JSON LIST OF TITLE, URL, CONTENT
# ---------------------------------------------------------------
# searches folder/subfolder `folder_to_search` for html files
# extracts the title, url, and content
# outputs as json file to support_assistant\data\output_filename
# replaces strings in output file from `old_strings` to `new_strings`
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
folder_to_search = "D:\\Users\\samuelr\\Documents\\GitHub\\GoInterject.github.io\\_site"
output_filename = 'content.json'

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
def extract_page_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        text_maker = html2text.HTML2Text()
        text_maker.ignore_tables = True
        stripped = text_maker.handle(content)

        soup = BeautifulSoup(content, 'html.parser')

        # Extract page title
        title = soup.title.text if soup.title else None

        # Construct page URL using file path
        url = f'{os.path.abspath(file_path)}'

        return {'title': title, 'url': url, 'content': stripped}

# ---------------------------------------------------------------
def search_folder_for_html(folder_path, output_file):
    page_data_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                page_data = extract_page_data(file_path)
                if page_data:
                    page_data_list.append(page_data)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(page_data_list, json_file, indent=2)

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

search_folder_for_html(folder_to_search, output)

# Replace strings in the file
for i in range(len(old_strings)):
    replace_string_in_file(output, old_strings[i], new_strings[i])
