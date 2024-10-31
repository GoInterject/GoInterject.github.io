# UPDATES ALL IMAGES ENTRY IN FRONT MATTER TO MATCH THE FILENAMES AND TYPES IN THE PAGE

# Run this script when updating image filenames and/or types (i.e. png or jpg)

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Finds all image references in the file (as indicated by '![](/images/...))
# Changes the existing images entry in the front matter to match the filenames and types found in the page
# If number of images in page and entries in images do not match, does not update
# If no images are found in page, sets the image_dir: "" and images: [] in the front matter

import os
import re
import yaml
import copy
import json

# If true: if the count between the images in the front matter is different from the number of images found in the document:
# will remove front matter image entry and insert a new image entry
INSERT_NEW_ENTRY = True
# Replace with the path to the folder containing .md files
FOLDER_PATH = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"

def insert_new_content(file_path, content, regex_pattern, new_insert):
    # Find the position of the regex_pattern
    match = re.search(regex_pattern, content, re.MULTILINE | re.DOTALL)
    
    if match:
        # Insert the new content after the matched entry 
        front_matter = content[:match.end()] + f'\n{new_insert}' + content[match.end():]
    else:
        # If matched entry is not found, insert make image_dir and new images entry at the beginning
        front_matter = f'---\nimage_dir: ""{new_insert}' + content[3:]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(front_matter)
    pass

def delete_image_dir_from_frontmatter(file_content):
    # Delete existing image_dir entry in the front matter, if present
    content = re.sub(r'(^.*\bimage_dir\b:.*$\n*)', '', file_content, count=1, flags=re.MULTILINE)
    return content

def delete_images_from_frontmatter0(file_content):
    # Delete existing images entry in the front matter, if present
    content = re.sub(r'(^.*\bimages\b:.*$\n*)', '', file_content, count=1, flags=re.MULTILINE)
    return content

def extract_front_matter(file_str):
    """Extract front matter from a file content string."""
    if file_str.startswith("---"):
        end_idx = file_str.find("---", 3)  # Find the second occurrence of '---'
        if end_idx != -1:
            front_matter_str = file_str[3:end_idx]
            # Replace tabs with spaces to prevent YAML parsing errors
            front_matter_str = front_matter_str.replace("\t", "    ")  # Replace with 4 spaces (adjust as needed)
            try:
                return yaml.safe_load(front_matter_str)
            except yaml.YAMLError as e:
                print(f"PARSE: Error parsing YAML front matter: {str(e)}")
    return {}

def delete_images_from_frontmatter1(file_content):
    # Regex pattern to match 'images' entry in various formats
    pattern = r'^\s*images:\s*(\[\s*\]|\[\s*.*?\s*\]|(?:\n\s*[-*]\s*.*?)*\n?)'
    
    # Delete existing images entry in the front matter, if present
    content = re.sub(pattern, '', file_content, count=1, flags=re.MULTILINE)
    return content

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

def extract_image_filenames(file_content):
    pattern = re.compile(r'!\[([^\]]*)\]\(/images/([^/]+/|)([^)]+)\)')
    matches = pattern.findall(file_content)
    return matches

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

def process_md_file(file_path):
    print(f"Finding images in {file_path}")
    global id
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    # front_matter_text = extract_front_matter(raw_content)
    # images_in_front_matter = front_matter_text.get("images", [])

    # Extract title and image filenames from the Markdown content
    images_from_front_matter = extract_images_from_frontmatter(raw_content)
    images_from_front_matter_original = copy.deepcopy(images_from_front_matter)
    image_filenames_list = extract_image_filenames(raw_content)

    # No images found in file or front matter
    if len(images_from_front_matter) == 0 and len(image_filenames_list) == 0:
        pass
    # No images found in file
    elif len(image_filenames_list) == 0:
        content = delete_image_dir_from_frontmatter(raw_content)
        content = delete_images_from_frontmatter(content)

        # Find the position of the links entry
        match = re.search(r'^links:\s*\[.*?\]', content, re.MULTILINE | re.DOTALL)
        
        if match:
            # Insert the new content after the matched entry 
            front_matter = content[:match.end()] + f'\nimage_dir: ""\nimages: []' + content[match.end():]
        else:
            # If matched entry is not found, insert make image_dir and new images entry at the beginning
            front_matter = f'---\nlinks: []\nimage_dir: ""\nimages: []' + content[3:]

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(front_matter)

    # Number of images found in front matter is equal to the number found in the file
    elif len(images_from_front_matter) == len(image_filenames_list):
        updated_images = []

        # Builds a list of updated image key for front matter
        # Updates the file and type of the image entry in the front matter
        # Iterate through images and filenames simultaneously
        for image, filename in zip(images_from_front_matter, image_filenames_list):
            s = filename[2].split(".") # extract type from filename extension
            image['file'] = '.'.join(s[:-1]) # updates the file value in the image entry of the front matter
            image['type'] = s[-1] # updates the type value in the image entry of the front matter
            # print("image = ", image)
            updated_images.append(image)

        # Only need to change the entry if there is a difference
        if images_from_front_matter != images_from_front_matter_original:
            # Convert the list of dictionaries to a string without quotes around keys and double quotes around values
            formatted_string = '[' + ', '.join(['{' + ', '.join([f"{key}: \"{value}\"" for key, value in item.items()]) + '}' for item in updated_images]) + ']'
            # Each entry in images should be on a separate newline and start with a tab character
            formatted_string = formatted_string.replace("{", "\n\t{").replace("]", "\n\t]")

            # Returns the file contents without the images entry in the front matter
            content = delete_images_from_frontmatter(raw_content)

            # Find the position of the image_dir entry
            match = re.search(r'image_dir:\s*("([^"]*)"|)', content, re.MULTILINE | re.DOTALL)
            
            if match:
                # Insert the new content after the matched entry 
                front_matter = content[:match.end()] + f'\nimages: {formatted_string}' + content[match.end():]
            else:
                # If matched entry is not found, insert make image_dir and new images entry at the beginning
                front_matter = f'---\nimage_dir: ""\nimages: {formatted_string}' + content[3:]

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(front_matter)

    # Images found in file and the count does not match the number of images in front matter
    # Flag is set to replace current images entry in front matter with new entries
    elif INSERT_NEW_ENTRY:
        updated_images = []
        
        for filename in image_filenames_list:
            s = filename[2].split(".")
            new_image = create_new_image()
            new_image['file'] = '.'.join(s[:-1])
            new_image['type'] = s[-1]
            updated_images.append(new_image)

        # Convert the list of dictionaries to a string without quotes around keys and double quotes around values
        formatted_string = '[\n\t' + ',\n\t'.join(['{' + ', '.join([f"{key}: \"{value}\"" for key, value in item.items()]) + '}' for item in updated_images]) + '\n]'

        content = delete_images_from_frontmatter(raw_content)

        # Find the position of the image_dir entry
        match = re.search(r'image_dir:\s*("([^"]*)"|)', content, re.MULTILINE | re.DOTALL)
        
        if match:
            # Insert the new content after the matched entry 
            front_matter = content[:match.end()] + f'\nimages: {formatted_string}' + content[match.end():]
        else:
            # If matched entry is not found, insert make image_dir and new images entry at the beginning
            front_matter = f'---\nimage_dir: ""\nimages: {formatted_string}' + content[3:]

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(front_matter)

    # Images found in file and the count does not match the number of images in front matter
    # Do not update the file
    else:
        print(f"ERROR: File {file_path} not updated: images in front matter ({len(images_from_front_matter)}) and in file ({len(image_filenames_list)}) are not equal") 

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if "_site" in dirs:
            dirs.remove("_site")  # Exclude the "_site" subfolder
        for file_name in files:
            # print(root, dirs, file_name)
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_md_file(file_path)

if __name__ == "__main__":
    # Process all .md files in subfolders and write to the output file
    process_folder(FOLDER_PATH)
    print(f"Images extracted and update completed for all .md files.")
