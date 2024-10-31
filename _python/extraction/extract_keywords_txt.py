# Extracts all keywords from the front_matter.yaml file
# Eliminates duplicates
# Saves all keywords to OUTPUT_FOLDER/OUTPUT_FILENAME

# ---------------------------------------------------------------
import yaml
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
# All folders are relative to gointerject.github.io folder
OUTPUT_FOLDER = "_metadata"
OUTPUT_FILENAME = 'keywords.txt'
FRONT_MATTER_FILEPATH = './_metadata/front_matter.yaml'

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_keywords(yaml_file):
    # Load the YAML file
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Set to store unique keywords
    unique_keywords = set()

    # Extract keywords from each entry
    for item in data.values():
        keywords = item.get('keywords', [])
        unique_keywords.update(keywords)

    return unique_keywords

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
    unique_keywords = extract_keywords(FRONT_MATTER_FILEPATH)

    with open(output_filepath, 'w') as file:
        for keyword in sorted(unique_keywords):
            file.write(f"{keyword}\n")

    print(f"  Keywords extracted and saved to {full_output_filepath}")

if __name__ == "__main__":
    main()
