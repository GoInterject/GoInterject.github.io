# BUILDS A JSON LIST OF TITLE, URL, CONTENT
# ---------------------------------------------------------------
# Be sure to first build the doc site with 'bundle exec jekyll build' to update the _site
# Searches the gointerject.github.io/_site folder and subfolders for html files
# Extracts the title, url, and content
# Outputs as json file to gointerject.github.io/OUTPUT_FOLDER/OUTPUT_FILENAME
# Replaces strings in output file from OLD_STRINGS to NEW_STRINGS

# ---------------------------------------------------------------
import os
from bs4 import BeautifulSoup
import json
import html2text
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.page_directories import PageDirectories
from utils.root_directory import get_root_dir

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = "_metadata" # relative to gointerject.github.io folder
OUTPUT_FILENAME = 'content.json'

# Replace words in the result json list
OLD_STRINGS = [
    "D:\\\\Users\\\\samuelr\\\\Documents\\\\GitHub\\\\GoInterject.github.io\\\\_site\\\\"
    ,"\\\\"
]

NEW_STRINGS = [
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
def extract_content_from_pages(root_folder, output_file):
    page_data_list = []

    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)
        if not os.path.exists(dir_path):
            continue

        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            if not file_name.endswith(".html"):
                continue

            # with open(file_path, "r", encoding="utf-8") as file_handle:
            page_data = extract_page_data(file_path)
            if page_data:
                page_data_list.append(page_data)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(page_data_list, json_file, indent=2)

# ---------------------------------------------------------------
def replace_strings_in_file(file_path, old_string, new_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        modified_content = content.replace(old_string, new_string)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

    except Exception as e:
        print(f"Error replacing string in {file_path}: {e}")

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    # The root directory of the documentation repo (i.e. gointerject.github.io)
    root_folder = get_root_dir(4)
    folder_to_search = os.path.join(root_folder, "_site")

    # Define the output file path for saving the front matter
    full_output_filepath = os.path.join(root_folder, OUTPUT_FOLDER, OUTPUT_FILENAME)

    extract_content_from_pages(folder_to_search, full_output_filepath)

    # Replace strings in the file
    for i in range(len(OLD_STRINGS)):
        replace_strings_in_file(full_output_filepath, OLD_STRINGS[i], NEW_STRINGS[i])

    print(f"  Index created and saved to {full_output_filepath}")

if __name__ == "__main__":
    main()
