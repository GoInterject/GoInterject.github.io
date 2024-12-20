# ADDS HEADINGS TO FRONT MATTER FOR ALL DOC PAGES
# ---------------------------------------------------------------
# This script will search md files in all folders in the `doc_page_folder_list.py`
# For each page:
# Deletes the headings entry in the Jekyll front matter if currently present
# Finds all headings in the file (as indicated by '##' or '###' or '####')
# Makes en entry of headings in the Jekyll front matter after the keywords entry

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import re
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import ROOT_FOLDER
from utils.doc_page_folder_list import PageDirectories
from utils.utilities import process_folder

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_headings(file_content):
    # Use regex to find headings (lines starting with ##, ###, ####)
    headings = re.findall(r'^##\s*(.*?)$|^###\s*(.*?)$|^####\s*(.*?)$', file_content, re.MULTILINE)
    return [re.sub(r'^\s*#*\s*', '', heading.strip()) for heading in sum(headings, ()) if heading]

# ---------------------------------------------------------------
def process_md_file(filepath):
    # Read the content of the Markdown file
    with open(filepath, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    # Extract headings from the content
    headings = extract_headings(raw_content)

    # Delete existing headings entry in the front matter, if present
    content = re.sub(r'(headings:\s*\[.*?\])\n*', '', raw_content, count=1, flags=re.MULTILINE | re.DOTALL)

    if headings:
        # Extract text in brackets for headings of the form "### [ReportRange](/wIndex/ReportRange.html)"
        headings = [re.search(r'\[(.*?)\]', heading).group(1) if re.search(r'\[(.*?)\]', heading) else heading for heading in headings]
        
        # Use double quotes around each heading
        headings_str = ', '.join([f'"{heading}"' for heading in headings])
        # Wrap the headings in brackets
        headings_str = f'[{headings_str}]'
    else:
        # If there are no headings, set an empty list
        headings_str = '[]'

    # Find the position of the keywords entry
    match = re.search(r'^keywords:\s*\[.*?\]', content, re.MULTILINE | re.DOTALL)
    
    if match:
        # Insert the headings entry after the keywords entry without extra spaces and comma
        front_matter = content[:match.end()] + f'\nheadings: {headings_str}' + content[match.end():]
    else:
        # If keywords entry is not found, insert keywords and headings entry at the beginning
        front_matter = f'---\nkeywords: []\nheadings: {headings_str}' + content[3:]

    # Write the updated content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(front_matter)

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
if __name__ == "__main__":
    process_folder(ROOT_FOLDER, PageDirectories, process_md_file)
    print("  Update headings in front matter for all md files.")
