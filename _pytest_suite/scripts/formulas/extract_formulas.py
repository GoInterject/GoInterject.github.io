# 

# ---------------------------------------------------------------
import os
import re
import json
from ...utils.root_directory import get_root_dir

# ---------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------
OUTPUT_FOLDER = "_metadata" # relative to gointerject.github.io folder
OUTPUT_FILENAME = 'formulas.json'
FILENAME = "ReportRange.md"

# ---------------------------------------------------------------
def extract_json(filename):
    # Dictionary to store extracted information
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

    # Extract description
    description_match = re.search(r'description:\s*(.*)', content)
    if description_match:
        description = description_match.group(1).strip()

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
            # Split types if there are multiple
            param_info["data_type"] = [t.strip() for t in re.split(r'[\/,]', type_match.group(1))]
        
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

    # Convert to JSON
    return json.dumps(output, indent=4)


root_folder = get_root_dir(4)
input_file = os.path.join(root_folder, "wFunctions", FILENAME)
print(F"input_file = {input_file}")

# Run the function and print the JSON output
# json_output = extract_json(FILENAME)
# print(json_output)
