# ADDS LINKS TO FRONT MATTER

# Run this script when updating documentation links

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Deletes the links entry in the Jekyll front matter if currently present
# Finds all links in the file (as indicated by '[text](link)' or 'a href="url"' but not if the link starts with "/images")
# Excludes references to the same page (as indicated by '[text](#link)')
# Makes en entry of links in the Jekyll front matter after the headings entry

import os
import re

def extract_links_from_content(file_content):
    # Define the regex pattern to match [text](link)
    pattern_square_brackets = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Define the regex pattern to match <a href="url">
    pattern_a_tag = re.compile(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1')

    # Find all matches in the file content for square brackets pattern using finditer
    matches_square_brackets = pattern_square_brackets.finditer(file_content)

    # Find all matches in the file content for <a href="url"> pattern using finditer
    matches_a_tag = pattern_a_tag.finditer(file_content)

    # Combine matches from both patterns in the order they appear
    all_matches = sorted(
        list(matches_square_brackets) + list(matches_a_tag),
        key=lambda match: match.start()
    )

    # Exclude links that begin with "/images/"
    filtered_matches = [match.group(2) for match in all_matches
                        if not match.group(2).startswith('/images/')]

    return filtered_matches

def process_md_file(file_path):
    # Read the content of the Markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    # Delete existing links entry in the front matter, if present
    content = re.sub(r'(links:\s*\[.*?\])\n*', '', raw_content, count=1, flags=re.MULTILINE | re.DOTALL)

    # Extract links from the content
    links = extract_links_from_content(content)

    if links:
        # Use double quotes around each heading
        links_str = ', '.join([f'"{link}"' for link in links])
        # Wrap the links in brackets
        links_str = f'[{links_str}]'
    else:
        # If there are no links, set an empty list
        links_str = '[]'

    # Find the position of the headings entry
    match = re.search(r'^headings:\s*\[.*?\]', content, re.MULTILINE | re.DOTALL)
    
    if match:
        # Insert the links entry after the headings entry without extra spaces and comma
        front_matter = content[:match.end()] + f'\nlinks: {links_str}' + content[match.end():]
    else:
        # If headings entry is not found, insert headings and links entry at the beginning
        front_matter = f'---\nheadings: []\nlinks: {links_str}' + content[3:]

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
    # Process all .md files in subfolders (excluding "_site")
    # root_file = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io\index.md"
    # process_md_file(root_file)

    root_folder = r"D:\Users\samuelr\Documents\GitHub\GoInterject.github.io"
    process_folder(root_folder)

    print("Links extracted and update completed for all .md files.")
