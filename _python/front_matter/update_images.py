# UPDATES ALL IMAGES ENTRY IN FRONT MATTER TO MATCH THE FILENAMES AND TYPES IN THE PAGE
# ---------------------------------------------------------------
# This script will search md files in all folders in the `doc_page_folder_list.py`
# For each page:
# Finds all image references in the file (as indicated by '![](/images/...))
# Changes the existing images entry in the front matter to match the filenames and types found in the page
# If number of images in page and entries in images do not match, does not update
# If no images are found in page, sets the image_dir: "" and images: [] in the front matter

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import re
import yaml
import copy
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import ROOT_FOLDER
from utils.doc_page_folder_list import PageDirectories
from utils.utilities import process_folder

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def insert_new_content(filepath, content, regex_pattern, new_insert):
    # Find the position of the regex_pattern
    match = re.search(regex_pattern, content, re.MULTILINE | re.DOTALL)
    
    if match:
        # Insert the new content after the matched entry 
        front_matter = content[:match.end()] + f'\n{new_insert}' + content[match.end():]
    else:
        # If matched entry is not found, insert make image_dir and new images entry at the beginning
        front_matter = f'---\nimage_dir: ""{new_insert}' + content[3:]

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(front_matter)
    pass

# ---------------------------------------------------------------
def delete_image_dir_from_frontmatter(file_content):
    # Delete existing image_dir entry in the front matter, if present
    content = re.sub(r'(^.*\bimage_dir\b:.*$\n*)', '', file_content, count=1, flags=re.MULTILINE)
    return content

# ---------------------------------------------------------------
def delete_images_from_frontmatter(file_content):
    # Regex pattern to match 'images' entry in the front matter, including multi-line arrays
    pattern = r'^\s*images:\s*\[.*?\]\s*\n'  # Match the 'images' list (empty or filled) in a single line
    pattern_multiline = r'^\s*images:\s*\[(.|\n)*?\]\s*\n'  # Match the 'images' list spanning multiple lines

    # First, try to match and remove multi-line arrays
    content = re.sub(pattern_multiline, '', file_content, count=1, flags=re.MULTILINE)

    # If no match for multi-line, try the single-line version
    if content == file_content:
        content = re.sub(pattern, '', file_content, count=1, flags=re.MULTILINE)

    return content

# ---------------------------------------------------------------
def extract_images_from_frontmatter(file_content):
    # Define the regex pattern to extract front matter
    front_matter_pattern = r'^---\n(.*?\n)---'

    # Use regex to find the front matter section
    match = re.match(front_matter_pattern, file_content, re.DOTALL)
    
    if match:
        front_matter_content = match.group(1)
        front_matter_content = front_matter_content.replace("\t", "    ")
        front_matter_data = yaml.safe_load(front_matter_content)

        # Extract "images" from the front matter
        images = front_matter_data.get('images', [])
        return images

    return []

# ---------------------------------------------------------------
def extract_image_filenames(file_content):
    pattern = re.compile(r'!\[([^\]]*)\]\(/images/([^/]+/|)([^)]+)\)')
    matches = pattern.findall(file_content)
    return matches

# ---------------------------------------------------------------
def create_new_image():
    return {
        'file': '',
        'type': '',
        'site': '',
        'cat': '',
        'sub': '',
        'report': '',
        'ribbon': '',
        'config': ''
    }

# ---------------------------------------------------------------
def format_images(images):
    """
    Format the images list into a string for the front matter.
    """
    formatted = '[\n\t' + ',\n\t'.join([
        '{' + ', '.join([f"{key}: \"{value}\"" for key, value in image.items()]) + '}'
        for image in images
    ]) + '\n]'
    return formatted

# ---------------------------------------------------------------
def update_front_matter(content, images_string, image_dir="\"\""):
    """
    Update the front matter with the provided images string and image directory.
    """
    content = delete_images_from_frontmatter(content)

    # Find the position of the image_dir entry
    match = re.search(r'image_dir:\s*("([^"]*)"|)', content, re.MULTILINE | re.DOTALL)

    if match:
        return content[:match.end()] + f'\nimages: {images_string}' + content[match.end():]
    else:
        return f'---\nimage_dir: {image_dir}\nimages: {images_string}' + content[3:]

# ---------------------------------------------------------------
def write_to_file(filepath, content):
    """
    Write the updated content back to the file.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# ---------------------------------------------------------------
def process_md_file(filepath):
    global id
    with open(filepath, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    images_from_front_matter = extract_images_from_frontmatter(raw_content)
    images_from_front_matter_original = copy.deepcopy(images_from_front_matter)
    image_filenames_list = extract_image_filenames(raw_content)

    # Case 1: No images in file or front matter
    if not images_from_front_matter and not image_filenames_list:
        return

    # Case 2: No images in file: Delete image entry from front matter
    elif not image_filenames_list:
        content = delete_image_dir_from_frontmatter(raw_content)
        content = delete_images_from_frontmatter(content)
        updated_content = update_front_matter(content, images_string="[]")
        write_to_file(filepath, updated_content)

    # Case 3: Matching number of images: update filenames and types in front matter
    elif len(images_from_front_matter) == len(image_filenames_list):
        for image, (_, _, filename) in zip(images_from_front_matter, image_filenames_list):
            parts = filename.split(".")
            image['file'] = '.'.join(parts[:-1])  # Update the file value
            image['type'] = parts[-1]  # Update the type value

        if images_from_front_matter != images_from_front_matter_original:
            images_string = format_images(images_from_front_matter)
            updated_content = update_front_matter(raw_content, images_string)
            write_to_file(filepath, updated_content)

    # Case 4: Mismatched number of images: add/remove images to match images found in file
    else:
        updated_images = []
        front_matter_files = {item['file']: item for item in images_from_front_matter}

        for _, _, filename in image_filenames_list:
            file = filename.split('.')[0]
            if file in front_matter_files:
                updated_images.append(front_matter_files[file])
            else:
                updated_images.append({
                    'file': file,
                    'type': '',
                    'site': '',
                    'cat': '',
                    'sub': '',
                    'report': '',
                    'ribbon': '',
                    'config': ''
                })

        images_string = format_images(updated_images)
        updated_content = update_front_matter(raw_content, images_string)
        write_to_file(filepath, updated_content)

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
if __name__ == "__main__":
    process_folder(ROOT_FOLDER, PageDirectories, process_md_file)
    print(f"  Updated all images in front matter for all md files.")
