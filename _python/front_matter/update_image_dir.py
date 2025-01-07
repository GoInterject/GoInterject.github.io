# ADDS IMAGE DIRECTORY TO FRONT MATTER FOR ALL DOC PAGES
# ---------------------------------------------------------------
# This script will search md files in all folders in the `doc_page_folder_list.py`
# For each page:
# Deletes the image_dir entry in the Jekyll front matter if currently present
# Extracts the name of the directory used for images (uses the first occurrence of an image link)
# Makes en entry of image_dir in the Jekyll front matter after the links entry

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
def extract_image_directory(file_content):
    # Regular expression pattern to find image references in the format ![anytext](/images/folder/filename)
    pattern = re.compile(r'!\[([^\]]*)\]\(/images/([^/]+/|)([^)]+)\)')
    images = pattern.findall(file_content)

    if images:
        return merge_root_and_sub_folder(images[0])
    else:
        return None

# ---------------------------------------------------------------
def merge_root_and_sub_folder(image):
    alt_text, sub_folder, filename = image
    root_folder = sub_folder.split('/')[0] if sub_folder else ""  # Extract root folder from subfolder
    sub_folder = sub_folder.split('/')[1] if '/' in sub_folder else ""  # Extract subfolder if present
    if '/' in filename:
        sub_folder = filename.split('/')[0]
        filename = filename.split('/')[1]

    if sub_folder != "":
        return root_folder + '/' + sub_folder
    else:
        return root_folder

# ---------------------------------------------------------------
def process_md_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    # Delete existing image_dir entry in the front matter, if present
    content = re.sub(r'(^.*\bimage_dir\b:.*$\n*)', '', raw_content, count=1, flags=re.MULTILINE)

    # Extract image directory from the Markdown content
    image_dir = extract_image_directory(content)

    if not image_dir:
        image_dir = ""

    # Find the position of the links entry
    match = re.search(r'^links:\s*\[.*?\]', content, re.MULTILINE | re.DOTALL)
    
    if match:
        # Insert the image_dir entry after the links entry without extra spaces and comma
        front_matter = content[:match.end()] + f'\nimage_dir: "{image_dir}"' + content[match.end():]
    else:
        # If links entry is not found, insert links and image_dir entry at the beginning
        front_matter = f'---\nlinks: []\nimage_dir: "{image_dir}"' + content[3:]

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(front_matter)

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
if __name__ == "__main__":
    process_folder(ROOT_FOLDER, PageDirectories, process_md_file)
    print("  Updated image_dir in front matter for all md files.")
