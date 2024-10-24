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

def process_md_file(file_path):
    print(f"Finding links in {file_path}")
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

def extract_links_from_content0(file_content):
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

def extract_links_from_content1(file_content):
    # Define the regex pattern to match [text](link)
    pattern_square_brackets = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Define the regex pattern to match <a href="url">
    pattern_a_tag = re.compile(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1')

    # Define the regex pattern for URLs, page links, and anchor links
    pattern_links = re.compile(r'(https?:\/\/[^\s#]+(?:#[^\s]*)?|\/w[^\s#]+(?:#[^\s]*)?|#[^\s]+)')

    # Find all matches in the file content for square brackets pattern using finditer
    matches_square_brackets = pattern_square_brackets.finditer(file_content)

    # Find all matches in the file content for <a href="url"> pattern using finditer
    matches_a_tag = pattern_a_tag.finditer(file_content)

    # Find all matches in the file content for URL and page links using finditer
    matches_links = pattern_links.finditer(file_content)

    # Combine matches from all patterns in the order they appear
    all_matches = sorted(
        list(matches_square_brackets) + list(matches_a_tag) + list(matches_links),
        key=lambda match: match.start()
    )

    # Extract and filter links
    filtered_matches = [match.group(2) if match.lastindex == 2 else match.group(0) 
                        for match in all_matches if not match.group(2).startswith('/images/')]

    return filtered_matches

def extract_links_from_content2(file_content):
    # Define the regex pattern to match [text](link)
    pattern_square_brackets = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Define the regex pattern to match <a href="url">
    pattern_a_tag = re.compile(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1')

    # Define the regex pattern for URLs, page links, and anchor links
    pattern_links = re.compile(r'(https?:\/\/[^\s#]+(?:#[^\s]*)?|\/w[^\s#]+(?:#[^\s]*)?|#[^\s]+)')

    # Find all matches in the file content for square brackets pattern using finditer
    matches_square_brackets = pattern_square_brackets.finditer(file_content)

    # Find all matches in the file content for <a href="url"> pattern using finditer
    matches_a_tag = pattern_a_tag.finditer(file_content)

    # Find all matches in the file content for URL and page links using finditer
    matches_links = pattern_links.finditer(file_content)

    # Combine matches from all patterns in the order they appear
    all_matches = sorted(
        list(matches_square_brackets) + list(matches_a_tag) + list(matches_links),
        key=lambda match: match.start()
    )

    # Extract and filter links
    filtered_matches = [
        match.group(2) if match.lastindex and match.lastindex == 2 else match.group(0)
        for match in all_matches
        if not (match.lastindex and match.group(2).startswith('/images/'))
    ]

    return filtered_matches

def extract_links_from_content3(file_content):
    # Define the regex pattern to match [text](link)
    pattern_square_brackets = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Define the regex pattern to match <a href="url">
    pattern_a_tag = re.compile(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1')

    # Define the regex pattern for URLs, page links, and anchor links
    pattern_links = re.compile(r'(https?:\/\/[^\s#]+(?:#[^\s]*)?|\/w[^\s#]+(?:#[^\s]*)?|#[^\s]+)')

    # Find all matches in the file content for square brackets pattern using finditer
    matches_square_brackets = pattern_square_brackets.finditer(file_content)

    # Find all matches in the file content for <a href="url"> pattern using finditer
    matches_a_tag = pattern_a_tag.finditer(file_content)

    # Find all matches in the file content for URL and page links using finditer
    matches_links = pattern_links.finditer(file_content)

    # Combine matches from all patterns in the order they appear
    all_matches = sorted(
        list(matches_square_brackets) + list(matches_a_tag) + list(matches_links),
        key=lambda match: match.start()
    )

    # Extract and filter links
    filtered_matches = []
    for match in all_matches:
        # Check if match has group(2); if not, use group(0)
        link = match.group(2) if match.lastindex and match.lastindex >= 2 else match.group(0)

        # Exclude links that start with "/images/"
        if not link.startswith('/images/'):
            filtered_matches.append(link)

    return filtered_matches

def extract_links_from_content4(file_content):
    # Define the regex pattern to match [text](link)
    pattern_square_brackets = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Define the regex pattern to match <a href="url">
    pattern_a_tag = re.compile(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1')

    # Define the regex pattern for URLs, page links, and anchor links
    pattern_links = re.compile(r'(https?:\/\/[^\s#\)]+(?:#[^\s]*)?|\/w[^\s#\)]+(?:#[^\s]*)?|#[^\s\)]+)')

    # Find all matches in the file content for square brackets pattern using finditer
    matches_square_brackets = pattern_square_brackets.finditer(file_content)

    # Find all matches in the file content for <a href="url"> pattern using finditer
    matches_a_tag = pattern_a_tag.finditer(file_content)

    # Find all matches in the file content for URL and page links using finditer
    matches_links = pattern_links.finditer(file_content)

    # Combine matches from all patterns in the order they appear
    all_matches = sorted(
        list(matches_square_brackets) + list(matches_a_tag) + list(matches_links),
        key=lambda match: match.start()
    )

    # Define patterns to filter out: strings consisting of # or multiple #
    patterns_to_filter = re.compile(r'^#+$')  # Matches any number of '#', like "##", "###"

    # Extra patterns to remove
    patterns_to_remove = re.compile(r'{:target="_blank"}{:rel="noopener"}')

    # Extract and filter links
    filtered_matches = []
    for match in all_matches:
        # Check if match has group(2); if not, use group(0)
        link = match.group(2) if match.lastindex and match.lastindex >= 2 else match.group(0)

        # Remove trailing unwanted parts like {:target="_blank"}{:rel="noopener"}
        link = re.sub(patterns_to_remove, '', link)

        # Exclude links that start with "/images/", or are just hashtags (e.g., "##", "###")
        if not link.startswith('/images/') and not patterns_to_filter.match(link):
            filtered_matches.append(link)

    return filtered_matches

def extract_links_from_content5(file_content):
    # Define the regex pattern to match [text](link)
    pattern_square_brackets = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Define the regex pattern to match <a href="url">
    pattern_a_tag = re.compile(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1')

    # Define the regex pattern for URLs, page links, and anchor links
    pattern_links = re.compile(r'(https?:\/\/[^\s#\)]+(?:#[^\s]*)?|\/w[^\s#\)]+(?:#[^\s]*)?|#[^\s\)]+)')

    # Find all matches in the file content for square brackets pattern using finditer
    matches_square_brackets = pattern_square_brackets.finditer(file_content)

    # Find all matches in the file content for <a href="url"> pattern using finditer
    matches_a_tag = pattern_a_tag.finditer(file_content)

    # Find all matches in the file content for URL and page links using finditer
    matches_links = pattern_links.finditer(file_content)

    # Combine matches from all patterns in the order they appear
    all_matches = sorted(
        list(matches_square_brackets) + list(matches_a_tag) + list(matches_links),
        key=lambda match: match.start()
    )

    # Define patterns to filter out: strings consisting of # or multiple #
    patterns_to_filter = re.compile(r'^#+$')  # Matches any number of '#', like "##", "###"

    # Extra patterns to remove
    patterns_to_remove = re.compile(r'{:target="_blank"}{:rel="noopener"}')

    # List to store links
    links = []

    # Extract and filter links
    for match in all_matches:
        # Check if match has group(2); if not, use group(0)
        link = match.group(2) if match.lastindex and match.lastindex >= 2 else match.group(0)

        # Remove trailing unwanted parts like {:target="_blank"}{:rel="noopener"}
        link = re.sub(patterns_to_remove, '', link).strip()

        # Exclude links that start with "/images/", or are just hashtags (e.g., "##", "###")
        if not link.startswith('/images/') and not patterns_to_filter.match(link):
            # Add the link to the list (maintaining duplicates)
            links.append(link)

    return links

def extract_links_from_content6(file_content):
    # Define the regex pattern to match [text](link)
    pattern_square_brackets = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Define the regex pattern to match <a href="url">
    pattern_a_tag = re.compile(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1')

    # Define the regex pattern for URLs and anchor links
    # pattern_links = re.compile(r'(https?:\/\/[^\s#\)]+(?:#[^\s]*)?|\/w[^\s#\)]+(?:#[^\s]*)?|#[^\s\)]+)')
    pattern_links = re.compile(r'(https?:\/\/[^\s#\)]+|\/w[^\s#\)]+|#[^\s\)]+)')

    # Find all matches in the file content
    matches_square_brackets = list(pattern_square_brackets.finditer(file_content))
    matches_a_tag = list(pattern_a_tag.finditer(file_content))
    matches_links = list(pattern_links.finditer(file_content))

    # Combine matches while preserving the order
    all_matches = sorted(
        matches_square_brackets + matches_a_tag + matches_links,
        key=lambda match: match.start()
    )

    # Define patterns to filter out
    patterns_to_filter = re.compile(r'^#+$')  # Matches any number of '#'
    patterns_to_remove = re.compile(r'{:target="_blank"}{:rel="noopener"}')

    # Set to keep track of added links
    seen_links = set()
    links = []

    # Extract and filter links
    for match in all_matches:
        # Check if match has group(2); if not, use group(0)
        link = match.group(2) if match.lastindex and match.lastindex >= 2 else match.group(0)

        # Remove unwanted suffixes
        link = re.sub(patterns_to_remove, '', link).strip()

        # Exclude unwanted links
        if not link.startswith('/images/') and not patterns_to_filter.match(link):
            # Only add link if it hasn't been added yet
            if link not in seen_links:
                links.append(link)
                seen_links.add(link)  # Track the added link

    return links

def extract_links_from_content7(file_content):
    links = []
    
    # Define regex patterns for the different types of links
    patterns = [
        r'https?://[^\s]+',  # URL (http or https)
        r'\[.*?\]\(https?://[^\s]+\)',  # Bracket URL Link
        r'\[.*?\]\(/w[^\s]*\)',  # Page Link
        r'\[.*?\]\(#.*?\)',  # Anchor Link
    ]

    # Combine the patterns into one regex
    combined_pattern = '|'.join(patterns)

    # Find all matches in the file content
    matches = re.findall(combined_pattern, file_content)

    # Clean up matches (if needed) and append to links
    for match in matches:
        links.append(match)

    return links

def extract_links_from_content8(file_content):
    links = []
    
    # Define regex patterns for the different types of links
    patterns = [
        r'https?://[^\s]+',  # URL (http or https)
        r'\[.*?\]\((https?://[^\s]+)\)',  # Bracket URL Link
        r'\[.*?\]\((/w[^\s]*)\)',  # Page Link
        r'\[.*?\]\((#.*?)\)',  # Anchor Link
    ]

    # Combine the patterns into one regex
    combined_pattern = '|'.join(patterns)

    # Find all matches in the file content
    matches = re.findall(combined_pattern, file_content)

    # Clean up matches and append to links
    for match in matches:
        # Each match will be a tuple; get the first non-empty group
        link = next(filter(None, match), None)
        if link:
            links.append(link)

    return links


def extract_links_from_content(file_content):
    links = []
    length = len(file_content)
    i = 0

    while i < length:
        char = file_content[i]

        # Check for the start of a URL
        if char == 'h' and i + 4 <= length and file_content[i:i + 4] in ['http', 'https']:
            # Extract the URL
            start = i
            while i < length and not (file_content[i].isspace() or 
                                    file_content[i] == '"' or
                                    (file_content[i] == '.' and (i + 1 >= length or file_content[i + 1].isspace()))):
                i += 1
            
            # Exclude the last quotation mark if it exists
            # if i > start and file_content[i - 1] == '"':
            #     links.append(file_content[start:i - 1])  # Exclude the last quote
            # else:
            links.append(file_content[start:i])  # Include the URL as is

        # Check for bracketed links: [text](url)
        elif char == '[':
            # print("found [")
            i = i + 1
            # Find the closing bracket
            # Ignore no text in brackets, e.g. []
            if i < length and file_content[i] != ']':
                # print("found text in []")
                start_bracket = i + 1
                end_bracket = file_content.find(']', start_bracket)
                
                if end_bracket != -1:
                    # print("found end bracket")
                    # Check if the character following the closing bracket is an opening parenthesis
                    if end_bracket + 1 < length and file_content[end_bracket + 1] == '(':
                        # print("( follows ]")
                        # Find the opening parenthesis
                        start_parenthesis = end_bracket + 2  # Move to the character after '('
                        end_parenthesis = file_content.find(')', start_parenthesis)
                        
                        if end_parenthesis != -1:
                            # print("found )")
                            # Extract the URL inside the parentheses
                            link = file_content[start_parenthesis:end_parenthesis]
                            links.append(link.strip())
                            # Move the index to the end of the parenthesis
                            i = end_parenthesis  # Move to the closing parenthesis
                        else:
                            # print("no ) found")
                            # No closing parenthesis found, skip to the end of the bracket
                            i = end_bracket
                    else:
                        # print("no ) found")
                        # If no opening parenthesis found, just skip to the end of the bracket
                        i = end_bracket
                else:
                    # print("no ] found")
                    i += 1  # Just move forward if no closing bracket is found

        # Check for page links that start with '/w'
        elif char == '/' and file_content[i:i + 2] == '/w':
            start = i
            while i < length and file_content[i] not in (' ', '\n', '.', ',', ')'):
                i += 1
            links.append(file_content[start:i])

        # Check for anchor links, skipping headings
        elif char == '#' and (i == 0 or file_content[i - 1] in [' ', '\n', '(', '[']):
            # Check for heading: skip if followed by another '#' or is the start of a heading
            if i + 1 < length and file_content[i + 1] not in (' ', '\n', '.', ',', ')'):
                start = i
                while i < length and file_content[i] not in (' ', '\n', '.', ',', ')'):
                    i += 1
                # Add the anchor link found, but ensure it is not part of a heading
                link = file_content[start:i]
                if not link.startswith('#'):
                    links.append(link)

        else:
            i += 1  # Move to the next character



    return links

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
