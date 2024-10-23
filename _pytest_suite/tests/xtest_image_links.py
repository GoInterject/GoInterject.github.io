from enum import Enum
import os
import logging

logger = logging.getLogger(__name__)

class PageDirs(Enum):
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

def check_image_links_in_dir(root_folder):
    """ """
    passing = True
    test_failed = False

    for folder in PageDirs:
        dir_path = os.path.join(root_folder, folder.value)

        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)

            with open(file_path, "r", encoding="utf-8") as file_handle:
                file_str = file_handle.read()

                imagelink_list = file_str.replace('![]', '<<<SPL>>>').split('<<<SPL>>>')[1:]
                
                for image in imagelink_list:
                    try:
                        imagelink_parse = image.split('(')[1].split(')')[0].split('?')[0]
                        logger.info(f"Checking image: {imagelink_parse}")
                    except:
                        test_failed = True
                        logger.error(f"\nImage: {imagelink_parse} in: {file_path} is broken and cannot be parsed.")

                    if test_failed == False and os.path.exists(root_folder + imagelink_parse):
                        passing = True
                       # print(" >> {} exists".format(os.path.basename(imagelink_parse)))
                    else:
                        test_failed = True
                        logger.error(f"\nThe image: {imagelink_parse} does not exist.\nThe image link is located in: {file_path}")
    
    if test_failed:
        return False

    return passing

def test_valid_imagelinks():
    root = get_root_dir()
    ret_val = check_image_links_in_dir(root)
    assert ret_val == True
