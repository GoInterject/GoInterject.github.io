# BUILDS A JSON FILE OF ALL KEYWORDS AND ALL URLS THAT KEYWORD IS FOUND IN THE FRONT MATTER FOR ALL DOC PAGES
# ---------------------------------------------------------------
# Run 'extract_front_matter.py' and 'extract_keywords_txt.py' first
# Creates a json file of all keywords in the documentation site
# Each keyword will have a list of URLs that it is found in
# Outputs JSON file to gointerject.github.io/OUTPUT_FOLDER/OUTPUT_FILENAME

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import yaml
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER, METADATA_FOLDER

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = METADATA_FOLDER
OUTPUT_FILENAME = 'index.json'
FRONT_MATTER_FILEPATH = './' + METADATA_FOLDER + '/front_matter.yaml'
KEYWORDS_FILEPATH = './' + METADATA_FOLDER + '/keywords.txt'

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def create_index(yaml_file, keywords_file, output_file):
    # Load the keywords from unique_keywords.txt
    with open(keywords_file, 'r') as file:
        keywords = [line.strip() for line in file if line.strip()]

    # Initialize the index dictionary with each keyword having an empty list
    index = {keyword: [] for keyword in keywords}

    # Load the YAML file
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Populate the index with URLs associated with each keyword
    for url, content in data.items():
        for keyword in content.get('keywords', []):
            if keyword in index:
                index[keyword].append(url)

    # Write the index dictionary to index.json
    with open(output_file, 'w') as file:
        json.dump(index, file, indent=4)

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    # Ensure the output folder exists
    output_folder_path = os.path.join(ROOT_FOLDER, OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)

    # Define the output file path for saving the front matter
    full_output_filepath = os.path.join(ROOT_FOLDER, OUTPUT_FOLDER, OUTPUT_FILENAME)

    output_filepath = "./" + OUTPUT_FOLDER + "/" + OUTPUT_FILENAME
    create_index(FRONT_MATTER_FILEPATH, KEYWORDS_FILEPATH, output_filepath)
    print(f"  Index created and saved to {full_output_filepath}")

if __name__ == "__main__":
    main()
    