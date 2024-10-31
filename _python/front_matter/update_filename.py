# ADDS FILENAME TO FRONT MATTER

# Run this script when updating documentation filenames

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Deletes the filenames entry in the Jekyll front matter if currently present
# Extracts the name of the file
# Makes en entry of filename in the Jekyll front matter after the title entry

import os
import re

def process_md_file(file_path):
    print(f"Finding filename in {file_path}")
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

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if "_site" in dirs:
            dirs.remove("_site")  # Exclude the "_site" subfolder
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_md_file(file_path)

if __name__ == "__main__":
    # Process all .md files in subfolders (excluding "_site")
    # root_file = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io\index.md"
    # process_md_file(root_file)

    root_folder = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"
    process_folder(root_folder)

    print("Filenames extracted and update completed for all .md files.")
