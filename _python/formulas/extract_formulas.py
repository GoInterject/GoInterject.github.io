# 

# ---------------------------------------------------------------
import os
import re
import json
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.root_directory import get_root_dir
from utils.formula_list import InterjectFormulas

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = "_metadata" # relative to gointerject.github.io folder
OUTPUT_FILENAME = 'formulas.json'
FILENAME = "ReportRange.md"

# ---------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------
def extract_json_from_file(filename):
    """Extract JSON data from a single Markdown file."""
    output = {
        "interject_formula_descriptions": []
    }
    
    # Initialize variables for storing data
    formula = ""
    description = ""
    parameters = {}

    # Read the file content
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract formula name
    formula_match = re.search(r'title:\s*(\w+\(\))', content)
    if formula_match:
        formula = formula_match.group(1).replace("()", "")

    # Extract description from the Function Summary section
    summary_match = re.search(r'##\s*Function Summary\s*(.*?)\n##', content, re.DOTALL)
    if summary_match:
        description = summary_match.group(1).strip()

    # Extract parameters
    parameter_blocks = re.findall(r'<button class="collapsible-parameter">\*\*(.*?)\*\*<br>(.*?)</button>.*?<table>(.*?)</table>', content, re.DOTALL)
    for param_name, param_desc, param_details in parameter_blocks:
        # Initialize dictionary for each parameter
        param_info = {
            "description": param_desc.strip(),
            "data_type": [],
            "constraints": "",
            "if_blank": ""
        }
        
        # Extract details from the table
        type_match = re.search(r'<b>Type</b></td>\s*<td>(.*?)</td>', param_details)
        if type_match:
            # Clean the type string and split by '/'
            types_raw = type_match.group(1)
            # Remove HTML tags
            types_cleaned = re.sub(r'<[^>]+>', '', types_raw)  # Remove all HTML tags
            # Split by '/'
            param_info["data_type"] = [t.strip() for t in types_cleaned.split('/') if t.strip()]
        
        constraints_match = re.search(r'<b>Constraints</b></td>\s*<td>(.*?)</td>', param_details)
        if constraints_match:
            param_info["constraints"] = constraints_match.group(1).strip()
        
        if_blank_match = re.search(r'<b>If Blank</b></td>\s*<td>(.*?)</td>', param_details)
        if if_blank_match:
            param_info["if_blank"] = if_blank_match.group(1).strip()
        
        # Add parameter info to the parameters dictionary
        parameters[param_name.strip()] = param_info

    # Construct the final JSON structure
    output["interject_formula_descriptions"].append({
        "formula": formula,
        "description": description,
        "parameters": parameters
    })

    return output

# ---------------------------------------------------------------
def extract_formulas(root_folder):
    """Extract JSON data from all Interject Formula Markdown files."""
    all_descriptions = {
        "interject_formula_descriptions": []
    }

    for file in InterjectFormulas:
        file_path = os.path.join(root_folder, file.value)

        with open(file_path, "r", encoding="utf-8") as file_handle:
            json_data = extract_json_from_file(file_path)
            all_descriptions["interject_formula_descriptions"].extend(json_data["interject_formula_descriptions"])

    # Convert to JSON format
    return json.dumps(all_descriptions, indent=4)

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
def main():
    root_folder = get_root_dir(3)
    root_functions_folder = os.path.join(root_folder, "wFunctions")

    input_filepath = os.path.join(root_folder, "wFunctions", FILENAME)
    # print(F"input_file = {input_filepath}")

    output_folder_path = os.path.join(root_folder, OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)
    output_file = os.path.join(root_folder, OUTPUT_FOLDER, OUTPUT_FILENAME)

    # Run the function and print the JSON output
    json_output = extract_formulas(root_functions_folder)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json_output)

    print(f"  JSON output saved to {output_file}")

if __name__ == "__main__":
    main()
