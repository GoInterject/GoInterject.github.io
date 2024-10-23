# OUTPUTS ALL IMAGE REFERENCES FROM MD FILES

# Run this script when updating images

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Finds all image references in the file (as indicated by '![](/images/...))
# Output format: id @ filename @ title @ root folder @ sub folder @ image filename @ image type

import os
import re

id = 1

def extract_image_filenames_and_title(file_content):
    # Regular expression pattern to find image references in the format ![](/images/folder/filename)
    # pattern = re.compile(r'!\[([^\]]*)\]\(/images/([^/]+)/([^)]+)\)')
    pattern = re.compile(r'!\[([^\]]*)\]\(/images/([^/]+/|)([^)]+)\)')

    filenames = pattern.findall(file_content)

    # Regular expression pattern to extract the title from the front matter
    title_pattern = re.compile(r'^title:\s+(.+)$', re.MULTILINE)
    title_match = title_pattern.search(file_content)

    # Extract the title or set it to "No Title" if not found
    title = title_match.group(1) if title_match else "No Title"

    return title, filenames

def process_md_file(file_path, output_file, file_name):
    global id
    with open(output_file, 'a', encoding='utf-8') as output:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Extract title and image filenames from the Markdown content
        title, filenames = extract_image_filenames_and_title(content)

        if filenames:
            for image in filenames:
                alt_text, sub_folder, filename = image
                root_folder = sub_folder.split('/')[0] if sub_folder else ""  # Extract root folder from subfolder
                sub_folder = sub_folder.split('/')[1] if '/' in sub_folder else ""  # Extract subfolder if present
                if '/' in filename:
                    sub_folder = filename.split('/')[0]
                    filename = filename.split('/')[1]
                words = filename.rsplit('.', 1)
                type = words[1]
                filename = words[0]

             # Output lines for each image found in the Markdown file
                output.write(f"{id}@{file_name}@{title}@{root_folder}@{sub_folder}@{filename}@{type}\n")
                id = id + 1
        else:
            # Output a line with "None" for filenames when no images are found
            output.write(f"{id}@{file_name}@{title}@None\n")
            id = id + 1

def process_folder(folder_path, output_file):
    for root, dirs, files in os.walk(folder_path):
        if "_site" in dirs:
            dirs.remove("_site")  # Exclude the "_site" subfolder
        for file_name in files:
            # print(root, dirs, file_name)
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_md_file(file_path, output_file, file_name)

if __name__ == "__main__":

    # Replace with the path to the folder containing .md files
    folder_path = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"

    # Specify the output file path
    output_file = 'images.txt'

    # Delete or erase the existing images.txt file
    if os.path.exists(output_file):
        os.remove(output_file)

    # Process all .md files in subfolders and write to the output file
    process_folder(folder_path, output_file)

    print(f"Images meta data written to {output_file}")
