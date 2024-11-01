# ADDS FILENAME TO FRONT MATTER

# Run this script when updating documentation filenames

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Deletes the filenames entry in the Jekyll front matter if currently present
# Extracts the name of the file
# Makes en entry of filename in the Jekyll front matter after the title entry

# ---------------------------------------------------------------
import os
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER
from utils.doc_page_folder_list import PageDirectories
from utils.file_processor import process_folder

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def process_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    # Delete existing filename entry in the front matter, if present
    content = re.sub(r'(^.*\bfilename\b:.*$\n*)', '', raw_content, count=1, flags=re.MULTILINE)

    # Find the position of the title entry
    match = re.search(r'title: (.+?)(?:\n|$)', content, re.MULTILINE | re.DOTALL)

    filename = os.path.basename(file_path)

    if match:
        # Insert the filename entry after the title entry without extra spaces and comma
        front_matter = content[:match.end()] + f'filename: "{filename}"\n' + content[match.end():]
    else:
        # If title entry is not found, insert title and filename entry at the beginning
        front_matter = f'---\ntitle: []\nfilename: "{filename}"' + content[3:]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(front_matter)

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
if __name__ == "__main__":
    process_folder(ROOT_FOLDER, PageDirectories, process_md_file)
    print("  Update filenames in front matter for all md files.")
