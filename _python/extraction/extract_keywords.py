# Run 'extract_front_matter.py' and 'extract_keywords_txt.py' first
# Creates a json file of all keywords in the documentation site
# Each keyword will have a list of URLs that it is found in

# ---------------------------------------------------------------
import yaml
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.root_directory import get_root_dir

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
# All folders are relative to gointerject.github.io folder
OUTPUT_FOLDER = "_metadata"
OUTPUT_FILENAME = 'index.json'
FRONT_MATTER_FILEPATH = './_metadata/front_matter.yaml'
KEYWORDS_FILEPATH = './_metadata/keywords.txt'

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
    root_folder = get_root_dir(3)

    # Ensure the output folder exists
    output_folder_path = os.path.join(root_folder, OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)

    # Define the output file path for saving the front matter
    full_output_filepath = os.path.join(root_folder, OUTPUT_FOLDER, OUTPUT_FILENAME)

    output_filepath = "./" + OUTPUT_FOLDER + "/" + OUTPUT_FILENAME
    create_index(FRONT_MATTER_FILEPATH, KEYWORDS_FILEPATH, output_filepath)
    print(f"  Index created and saved to {full_output_filepath}")

if __name__ == "__main__":
    main()
    