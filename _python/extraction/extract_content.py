# BUILDS A JSON LIST OF TITLE, URL, CONTENT OF ALL DOC PAGES
# ---------------------------------------------------------------
# Be sure to first build the doc site with 'bundle exec jekyll build' to update the _site
# Searches the gointerject.github.io/_site folder and subfolders for html files
# Extracts the title, URL, and content
# Outputs as json file to gointerject.github.io/OUTPUT_FOLDER/OUTPUT_FILENAME

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import os
from bs4 import BeautifulSoup
import json
import html2text
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.doc_page_folder_list import PageDirectories
from utils.utilities import convert_filepath_to_url
from config import ROOT_FOLDER, SITE_FOLDER, METADATA_FOLDER

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = METADATA_FOLDER
OUTPUT_FILENAME = 'content.json'

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_page_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        text_maker = html2text.HTML2Text()
        text_maker.ignore_tables = True
        stripped = text_maker.handle(content)

        soup = BeautifulSoup(content, 'html.parser')

        # Extract page title
        title = soup.title.text if soup.title else None

        # Convert the filepath to a page URL
        url = convert_filepath_to_url(filepath)

        return {'title': title, 'url': url, 'content': stripped}

# ---------------------------------------------------------------
def extract_content_from_pages(root_folder, output_file):
    page_data_list = []

    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)
        if not os.path.exists(dir_path):
            continue

        for file_name in os.listdir(dir_path):
            filepath = os.path.join(dir_path, file_name)
            if not file_name.endswith(".html"):
                continue

            page_data = extract_page_data(filepath)
            if page_data:
                page_data_list.append(page_data)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(page_data_list, json_file, indent=2)

# ---------------------------------------------------------------
def replace_strings_in_file(filepath, old_string, new_string):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        modified_content = content.replace(old_string, new_string)

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(modified_content)

    except Exception as e:
        print(f"Error replacing string in {filepath}: {e}")

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    # The root directory of the documentation repo (i.e. gointerject.github.io)
    folder_to_search = os.path.join(ROOT_FOLDER, SITE_FOLDER)

    # Ensure the output folder exists
    output_folder_path = os.path.join(ROOT_FOLDER, OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)

    # Define the output file path for saving the front matter
    full_output_filepath = os.path.join(ROOT_FOLDER, OUTPUT_FOLDER, OUTPUT_FILENAME)

    extract_content_from_pages(folder_to_search, full_output_filepath)

    replace_strings_in_file(full_output_filepath, "/_site", "")
    
    print(f"  Index created and saved to {full_output_filepath}")

if __name__ == "__main__":
    main()
