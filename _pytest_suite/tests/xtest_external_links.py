from enum import Enum
import os
import logging
import requests

logger = logging.getLogger(__name__)

# all the relative folder paths to check pages in 
class PageDirectories(Enum):
    WABOUT = "wAbout"
    WAPI = "wApi"
    WDESIGN = "wDesign"
    WDEVELOPER = "wDeveloper"
    WFUNCTIONS = "wFunctions"
    WGETSTARTED = "wGetStarted"
    WINDEX = "wIndex"
    WLABS = "wLabs"
    WPORTAL = "wPortal"
    WRELEASENOTES = "wReleaseNotes"
    WTROUBLESHOOT = "wTroubleshoot"
    BFINANCIALS = "bApps\\bFinancials"
    InterjectTRAININGBUDGET = "bApps\\InterjectTraining\\Budget"
    InterjectTRAININGCAPITAL = "bApps\\InterjectTraining\\Capital"
    InterjectTRAININGPROJECTIONS = "bApps\\InterjectTraining\\Projections"
    InterjectTRAININGWIP = "bApps\\InterjectTraining\\WIP"

def verify(url):
    """ verify that a request response is valid (returns a response code of 200) """
    response = requests.get(url)
    
    if response:
        return True

    else:
        return False

def get_par_dir(n, file):
    """ returns n parent directory of file """
    file_path = os.path.abspath(file)
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return file_path

def get_root_dir():
    root = get_par_dir(3, __file__)
    print("root folder is {}".format(root))
    return root

def check_external_links_in_dir(root_folder):
    """ """
    passing = True
    test_failed = False

    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)

        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)

            with open(file_path, "r", encoding="utf-8") as file_handle:
                file_str = file_handle.read()

                extUrls = [link.split(")")[0] 
                    for link in file_str.split("](")
                        if ".png" not in link
                        if ".jpg" not in link
                        if ".gif" not in link
                        if ".html" not in link
                        if ".zip" not in link
                        if "images" not in link
                        if "mailto" not in link
                        if "#" not in link
                        ][1:]
                
                for extUrl in extUrls:
                    logger.info(f"Checking url: {extUrl} in: {file_path}")
                    if verify(extUrl):
                        passing = True
                    
                    else:
                        test_failed = True
                        logger.error(f"\nThe url link route: {extUrl} does not exist.\nThe url link is located in: {file_path}")
    
    if test_failed:
        return False

    return passing

def test_valid_links():
    root = get_root_dir()
    ret_val = check_external_links_in_dir(root)
    assert ret_val == True