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
import json

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

def delete_images_from_frontmatter(file_content):
    # Delete existing images entry in the front matter, if present
    content = re.sub(r'(^.*\bimages\b:.*$\n*)', '', file_content, count=1, flags=re.MULTILINE)
    return content

def extract_images_from_frontmatter(file_content):
    # Define the regex pattern to extract front matter
    front_matter_pattern = r'^---\n(.*?\n)---'

    # Use regex to find the front matter section
    match = re.match(front_matter_pattern, file_content, re.DOTALL)
    
    if match:
        front_matter_content = match.group(1)
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

def process_md_file(file_path, insert_new_entry):
    global id
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    # Extract title and image filenames from the Markdown content
    images = extract_images_from_frontmatter(raw_content)
    filenames = extract_image_filenames(raw_content)

    # There are images in the file:
    if len(filenames) > 0:
        if len(images) == len(filenames):
            updated_images = []

            # Iterate through images and filenames simultaneously
            for image, filename in zip(images, filenames):
                s = filename[2].split(".")
                image['file'] = '.'.join(s[:-1])
                image['type'] = s[-1]
                # print("image = ", image)
                updated_images.append(image)

            # Convert the list of dictionaries to a string without quotes around keys and double quotes around values
            formatted_string = '[' + ', '.join(['{' + ', '.join([f"{key}: \"{value}\"" for key, value in item.items()]) + '}' for item in updated_images]) + ']'

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

        else:
            if insert_new_entry:
                updated_images = []
                
                for filename in filenames:
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

            else:
                print("ERROR: File", file_path, "not updated: 'images' and 'filenames' count is not equal") 

    # No images in file:
    else:
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


def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if "_site" in dirs:
            dirs.remove("_site")  # Exclude the "_site" subfolder
        for file_name in files:
            # print(root, dirs, file_name)
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_md_file(file_path, False)

if __name__ == "__main__":
    # Replace with the path to the folder containing .md files
    folder_path = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"

    # Process all .md files in subfolders and write to the output file
    process_folder(folder_path)

    print(f"Images extracted and update completed for all .md files.")
