import os
import logging
from enum import Enum

logger = logging.getLogger(__name__)

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

def prRed(skk): 
    logger.error(skk)

def get_par_dir(n, file):
    """ returns n parent directory of file """
    file_path = os.path.abspath(file)
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return file_path

def get_root_dir():
    root = get_par_dir(3, __file__)
    return root

def check_internal_links_in_dir(root_folder):
    passing = True
    test_failed = False

    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)

            with open(file_path, "r", encoding="utf-8") as file_handle:
                file_str = file_handle.read()

                locUrls = [link.split(")")[0]
                    for link in file_str.split("](")
                        if ".png" not in link
                        if ".jpg" not in link
                        if ".gif" not in link
                        if "https" not in link
                        if ".com" not in link
                        if "images" not in link
                        # if "#" not in link
                        ][1:]
                locUrlsMD = [locUrl.replace('.html', '.md') for locUrl in locUrls]

                for locUrlMD in locUrlsMD:
                    locUrlMDList = locUrlMD.split('/')
                    if len(locUrlMDList) == 1:
                        currentDirectory = dir_path + "\\" + locUrlMD
                    else:
                        locUrlMD = "\\".join(locUrlMDList)
                        currentDirectory = root_folder + locUrlMD
                        logger.info(f"Checking file: {currentDirectory}")

                    if os.path.exists(currentDirectory):
                        passing = True
                    else:
                        test_failed = True
                        logger.error(f"\nThe link route: {currentDirectory} does not exist.\nThe link is located in: {file_path}")

    if test_failed:
        return False

    return passing

def test_valid_internal_links():
    root = get_root_dir()
    ret_val = check_internal_links_in_dir(root)
    assert ret_val == True
