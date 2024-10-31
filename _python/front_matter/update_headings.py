# ADDS HEADINGS TO FRONT MATTER

# Run this script when updating documentation headings

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Deletes the headings entry in the Jekyll front matter if currently present
# Finds all headings in the file (as indicated by '##' or '###' or '####')
# Makes en entry of headings in the Jekyll front matter after the keywords entry

import os
import re

def extract_headings(file_content):
    # Use regex to find headings (lines starting with ##, ###, ####)
    headings = re.findall(r'^##\s*(.*?)$|^###\s*(.*?)$|^####\s*(.*?)$', file_content, re.MULTILINE)
    return [re.sub(r'^\s*#*\s*', '', heading.strip()) for heading in sum(headings, ()) if heading]

def process_md_file(file_path):
    print(f"Finding headings in {file_path}")
    # Read the content of the Markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
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
    root_folder = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"
    
    # Process all .md files in subfolders (excluding "_site")
    process_folder(root_folder)
    
    print("Headings extracted and update completed for all .md files.")
