# ADDS IMAGE DIRECTORY TO FRONT MATTER

# Run this script when updating documentation image directories

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Deletes the image_dir entry in the Jekyll front matter if currently present
# Extracts the name of the directory used for images (root folder + sub folder if present)
# Makes en entry of image_dir in the Jekyll front matter after the links entry

import os
import re

def extract_image_directory(file_content):
    # Regular expression pattern to find image references in the format ![anytext](/images/folder/filename)
    pattern = re.compile(r'!\[([^\]]*)\]\(/images/([^/]+/|)([^)]+)\)')
    images = pattern.findall(file_content)

    if images:
        return merge_root_and_sub_folder(images[0])
    else:
        return None

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

def process_md_file(file_path):
    print(f"Finding image_dir in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
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

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(front_matter)

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

    # Replace with the path to the folder containing .md files
    folder_path = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"

    # Process all .md files in subfolders
    process_folder(folder_path)

    print("Image directory extracted and update completed for all .md files.")
