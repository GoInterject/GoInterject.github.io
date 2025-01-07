# BUILDS A JSON FILE OF ALL KEYWORDS AND ALL URLS THAT KEYWORD IS FOUND IN THE FRONT MATTER FOR ALL DOC PAGES
# ---------------------------------------------------------------
# Run 'extract_front_matter.py' and 'extract_keywords_txt.py' first
# Creates a json file of all keywords in the documentation site
# Each keyword will have a list of URLs that it is found in
# Outputs JSON file to gointerject.github.io/OUTPUT_FOLDER/OUTPUT_FILENAME

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.doc_page_folder_list import PageDirectories
from utils.utilities import convert_filepath_to_url, extract_front_matter_from_file
from config import ROOT_FOLDER, METADATA_FOLDER
import re
import unicodedata

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = Path(METADATA_FOLDER)
OUTPUT_FILENAME = 'page_topics.json'
FRONT_MATTER_FILEPATH = OUTPUT_FOLDER / 'front_matter.yaml'
KEYWORDS_FILEPATH = OUTPUT_FOLDER / 'keywords.txt'

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def heading_to_anchor(heading):
    """
    Converts a heading string into a URL-friendly anchor following Jekyll's conventions.

    Args:
        heading (str): The heading text to be converted.

    Returns:
        str: The generated anchor string.
    """
    # Normalize the string to remove special characters
    normalized_heading = unicodedata.normalize('NFKD', heading)
    
    # Convert to lowercase
    normalized_heading = normalized_heading.lower()
    
    # Remove punctuation and non-alphanumeric characters (except spaces)
    normalized_heading = re.sub(r'[^\w\s-]', '', normalized_heading)
    
    # Replace spaces with hyphens
    normalized_heading = re.sub(r'[\s]+', '-', normalized_heading)
    
    # Remove leading and trailing hyphens
    normalized_heading = normalized_heading.strip('-')
    
    return normalized_heading

# ---------------------------------------------------------------
def extract_headings_from_all_pages(output_file):
    topics = {}

    for folder in PageDirectories:
        dir_path = Path(ROOT_FOLDER) / folder.value
        if not dir_path.exists():
            continue

        for file_path in dir_path.iterdir():
            if not file_path.suffix == ".md":
                continue

            with file_path.open("r", encoding="utf-8") as file_handle:
                # Extract the front matter and content of the file
                front_matter = extract_front_matter_from_file(file_path)
                web_url = convert_filepath_to_url(str(file_path))

                # Extract title, skipping "Overview"
                title = front_matter.get("title")
                if title and title != "Overview":
                    if title not in topics:
                        topics[title] = []
                    topics[title].append(web_url)

                # Extract headings, skipping "Overview"
                headings = front_matter.get("headings", [])
                for heading in headings:
                    if heading != "Overview":
                        if heading not in topics:
                            topics[heading] = []
                        full_url = f"{web_url}#{heading_to_anchor(heading)}"
                        topics[heading].append(full_url)

    with output_file.open('w', encoding='utf-8') as json_file:
        json.dump({"topics": topics}, json_file, indent=2)
    
# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    # Ensure the output folder exists
    output_folder_path = Path(ROOT_FOLDER) / OUTPUT_FOLDER
    output_folder_path.mkdir(parents=True, exist_ok=True)

    # Define the output file path for saving the front matter
    full_output_filepath = output_folder_path / OUTPUT_FILENAME

    extract_headings_from_all_pages(full_output_filepath)

    print(f"  Headings extracted and saved to {full_output_filepath}")

if __name__ == "__main__":
    main()
    