# ADDS LINKS TO FRONT MATTER

# Run this script when updating documentation links for a file or all files of a root folder

# This script will search the root folder and all subfolders for .md files
# Excludes the "_site" folder
# Deletes the links entry in the Jekyll front matter if currently present
# Finds all links in the file (as indicated by '[text](link)' or 'a href="url"')
# Valid links are preceded by '"', '[', or '('
# Excludes links preceded by white space - these are explanatory links
# Excludes links that start with "/images" - these are images
# Excludes references to the same page (as indicated by '[text](#link)') - these are headings
# Makes an entry of links in the Jekyll front matter after the headings entry

# ---------------------------------------------------------------
import os
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import ROOT_FOLDER

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def process_md_file(file_path):
    # Read the content of the Markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_content = file.read()

    # Delete existing links entry in the front matter, if present
    content = re.sub(r'(links:\s*\[.*?\])\n*', '', raw_content, count=1, flags=re.MULTILINE | re.DOTALL)

    # Extract links from the content
    links = extract_links_from_content(content)

    links = clean_links(links)

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

# ---------------------------------------------------------------
def clean_links(links):
    cleaned_links = []
    
    for link in links:
        # Remove trailing parentheses if they exist
        while link.endswith(')'):
            link = link[:-1]
        cleaned_links.append(link)

    return cleaned_links

# ---------------------------------------------------------------
def extract_links_from_content(file_content):
    links = []
    length = len(file_content)
    i = 0

    while i < length:
        char = file_content[i]
        # print(f"i = {i}, char = {char}")

        # Check for the start of a URL
        if (char == '"' or char == '(') and i + 9 <= length and file_content[i+1:i + 9] in ['http://', 'https://']:
            # print("found http link")
            # Extract the URL
            start = i + 1
            i += 1
            # This will signal the end of the url: whitespace, quotation mark, period followed by a whitespace
            while i < length and not (file_content[i].isspace() or 
                                    file_content[i] == '"' or
                                    (file_content[i] == '.' and (i + 1 >= length or file_content[i + 1].isspace()))):
                i += 1
            
            links.append(file_content[start:i])  # Include the URL as is

        # Check for bracketed links: [text](url)
        elif char == '[':
            #print("found open bracket [")
            i += 1
            # Find the closing bracket
            # If there is text inside the brackets, e.g. [text]
            if i < length and file_content[i] != ']':
                #print("found text in [brackets]")
                start_bracket = i
                end_bracket = file_content.find(']', start_bracket)
                
                # Found ending bracket
                if end_bracket != -1:
                    #print("found end bracket")
                    # Check if the character following the closing bracket is an opening parenthesis
                    if end_bracket + 1 < length and file_content[end_bracket + 1] == '(':
                        #print("( follows ]")
                        # Find the opening parenthesis
                        start_parenthesis = end_bracket + 2  # Move to the character after '('
                        end_parenthesis = file_content.find(')', start_parenthesis)
                        
                        # Found ending parenthesis
                        if end_parenthesis != -1:
                            #print("found )")
                            # Extract the URL inside the parentheses
                            link = file_content[start_parenthesis:end_parenthesis]
                            if not link.startswith("/images"): # exclude image links
                                links.append(link.strip())
                            # Move the index to the end of the parenthesis
                            i = end_parenthesis  # Move to the closing parenthesis
                        # No closing parenthesis found, skip to the end of the bracket
                        else:
                            #print("no ) found")
                            i = end_bracket + 1
                    # If no opening parenthesis found, just skip to the end of the bracket
                    else:
                        #print("no ( found")
                        i = end_bracket + 1
                # No ending bracket found
                else:
                    #print("no ] found")
                    i += 1  # Just move forward if no closing bracket is found

        # Check for page links that start with (/w or "/b or "/w
        elif char == '(/)':
            if file_content[i:i + 2] == '/w' and file_content[i-1] == '(':
                #print("found /w link")
                start = i
                while i < length and file_content[i] not in (' ', '\n', '.', ',', ')'):
                    i += 1
                links.append(file_content[start:i])
            elif file_content[i-1] == '"' and (file_content[i:i + 2] == '/b' or file_content[i:i + 2] == '/w'):
                #print("found /b or /w link inside href")
                start = i
                while i < length and file_content[i] != '"':
                    i += 1
                links.append(file_content[start:i])
            else:
                i += 1

        # Check for anchor links, skipping headings
        elif char == '#' and (i == 0 or file_content[i - 1] in [' ', '\n', '(', '[']):
            # Check for heading: skip if followed by another '#' or is the start of a heading
            if i + 1 < length and file_content[i + 1] not in (' ', '\n', '.', ',', ')'):
                #print("found # link")
                start = i
                while i < length and file_content[i] not in (' ', '\n', '.', ',', ')'):
                    i += 1
                # Add the anchor link found, but ensure it is not part of a heading
                link = file_content[start:i]
                if not link.startswith('#'):
                    links.append(link)
            else:
                i += 1 # Move to the next character
        
        elif char == 'm' and i + 6 <= length and file_content[i:i + 6] in ['mailto']:
            #print("found mail link")
            # Extract the URL
            start = i
            # This will signal the end of the link: whitespace, quotation mark, period followed by a whitespace
            while i < length and not (file_content[i-3] == 'c' and file_content[i-2] == 'o' and file_content[i-1] == 'm'):
                i += 1
            
            links.append(file_content[start:i])  # Include the URL as is
        
        else:
            i += 1  # Move to the next character

    return links

# ---------------------------------------------------------------
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if "_site" in dirs:
            dirs.remove("_site")  # Exclude the "_site" subfolder
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_md_file(file_path)

# ---------------------------------------------------------------
if __name__ == "__main__":
    process_folder(ROOT_FOLDER)
    print("  Links updated in front matter for all md files.")
