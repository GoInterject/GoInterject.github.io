# RUNS ALL EXTRACT SCRIPTS

# BE SURE TO SET THE CONFIG VARIABLES IN `config.py`
# ---------------------------------------------------------------

import extract_front_matter
import extract_keywords_txt
import extract_keywords
import extract_content
from formulas.extract_formulas import main as extract_formulas

# ---------------------------------------------------------------
def run_all():
    print("Running extract_front_matter.py...")
    extract_front_matter.main()

    print("Running extract_keywords_txt.py...")
    extract_keywords_txt.main()

    print("Running extract_keywords.py...")
    extract_keywords.main()

    print("Running extract_content.py...")
    extract_content.main()

    print("Running extract_formulas.py...")
    extract_formulas()

    print("All scripts completed successfully.")

# ---------------------------------------------------------------
if __name__ == "__main__":
    run_all()
