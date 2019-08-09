from enum import Enum
import os
import logging

class PageDirectories(Enum):
    WABOUT = "wAbout"
    WGETSTARTED = "wGetStarted"
    WAPI = "wApi"
    WINDEX = "wIndex"
    WPORTAL = "wPortal"
    WTROUBLESHOOT = "wTroubleshoot"
    BFINANCIALS = "bApps\\bFinancials"
    INTERJECTTRAININGBUDGET = "bApps\\InterjectTraining\\Budget"
    INTERJECTTRAININGCAPITAL = "bApps\\InterjectTraining\\Capital"
    INTERJECTTRAININGPROJECTIONS = "bApps\\InterjectTraining\\Projections"
    INTERJECTTRAININGWIP = "bApps\\InterjectTraining\\WIP"

def prRed(skk): 
    print("\033[91m {}\033[00m" .format(skk)) 

def get_par_dir(n, file):
    """ returns n parent directory of file """
    file_path = os.path.abspath(file)
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return file_path


def get_root_dir():
    root = get_par_dir(3, __file__)
    return root

def get_cur_dir():
    currentDir = get_par_dir(1, __file__)
    return currentDir

def check_internal_links_in_dir(root_folder):
    """ """
    passing = True

    for folder in PageDirectories:
        dir_path = os.path.join(root_folder, folder.value)

        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)

            with open(file_path, "r", encoding="utf-8") as file_handle:
                file_str = file_handle.read()

                #excludes anchor links
                locUrls = [link.split(")")[0] 
                    for link in file_str.split("](")
                        if ".png" not in link
                        if ".jpg" not in link
                        if ".gif" not in link
                        if "https" not in link
                        if ".com" not in link
                        if "images" not in link
                        if "#" not in link
                        ][1:]
                locUrlsMD = [locUrl.replace('.html', '.md') for locUrl in locUrls]
                
                
                # locAnchorUrls = [link.split(")")[0]
                #     for link in file_str.split("](")
                #         if ".png" not in link
                #         if ".jpg" not in link
                #         if ".gif" not in link
                #         if "https" not in link
                #         if ".com" not in link
                #         if "images" not in link
                #     ][1:]
                # filteredLocAnchorUrls = filter(lambda x: '#' in x, locAnchorUrls)

                for locUrlMD in locUrlsMD:

                    locUrlMDList = locUrlMD.split('/')
                    if len(locUrlMDList) == 1:
                        currentDirectory = dir_path + "\\" + locUrlMD

                    else:
                        locUrlMD = "\\".join(locUrlMDList)
                        
                        currentDirectory = root_folder + locUrlMD
                        print("Checking... >>>" + currentDirectory)

                    if os.path.exists(currentDirectory):
                        passing = True

                    else:
                        passing = False
                        prRed("\n>>> ERROR")
                        print("The link route: {} does not exist. \nThe link is located in: {}".format(currentDirectory, file_path))
                        prRed("\n>>> END ERROR MSG")
                        return passing
                
    return passing


def test_valid_internal_links():

    root = get_root_dir()
    ret_val = check_internal_links_in_dir(root)
    assert ret_val == True