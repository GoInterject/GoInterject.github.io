# BUILDS A YAML FILE OF THE FRONT MATTER OF ALL DOC PAGES
# ---------------------------------------------------------------
# Outputs JSON file to gointerject.github.io/OUTPUT_FOLDER/OUTPUT_FILENAME
# This script will iterate through all the pages and extract the front matter into an external file

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import os
import yaml  # for parsing YAML front matter and saving the result
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.doc_page_folder_list import PageDirectories
from utils.utilities import convert_filepath_to_url, extract_front_matter_from_file
from config import ROOT_FOLDER, METADATA_FOLDER

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = METADATA_FOLDER
OUTPUT_FILENAME = 'front_matter.yaml'

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_front_matter_from_all_pages():
    front_matter = {}

    for folder in PageDirectories:
        dir_path = os.path.join(ROOT_FOLDER, folder.value)
        if not os.path.exists(dir_path):
            continue

        for file_name in os.listdir(dir_path):
            filepath = os.path.join(dir_path, file_name)
            if not file_name.endswith(".md"):
                continue

            with open(filepath, "r", encoding="utf-8") as file_handle:
                file_front_matter = extract_front_matter_from_file(filepath)
                web_url = convert_filepath_to_url(filepath)
                front_matter[web_url] = file_front_matter
    
    return front_matter
    
# ---------------------------------------------------------------
def save_front_matter_to_file(output_file, front_matter_dict):
    """Save front matter dictionary to an external YAML file."""
    try:
        with open(output_file, "w", encoding="utf-8") as yaml_file:
            yaml.dump(front_matter_dict, yaml_file, allow_unicode=True)
    except IOError as e:
        print(f"Error saving front matter to file: {str(e)}")

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    front_matter = extract_front_matter_from_all_pages()

    # Ensure the output folder exists
    output_folder_path = os.path.join(ROOT_FOLDER, OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)

    # Define the output file path for saving the front matter
    full_output_filepath = os.path.join(ROOT_FOLDER, OUTPUT_FOLDER, OUTPUT_FILENAME)

    # Save the global front matter dictionary to an external YAML file
    save_front_matter_to_file(full_output_filepath, front_matter)
    print(f"  Front matter saved to {full_output_filepath}")

if __name__ == "__main__":
    main()
