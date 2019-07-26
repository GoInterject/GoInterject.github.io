

from enum import Enum
import os
import logging
import requests
import re

# all the relative folder paths to check pages in 
class PageDirs(Enum):
    WABOUT = "wAbout"
    # WAPI = "wApi"
    # WGETSTARTED = "wGetStarted"
    # WINDEX = "wIndex"
    # WPORTAL = "wPortal"
    # WTROUBLESHOOT = "wTroubleshoot"
    # BAPPS = "bApps"
    # WAPPS = "wApps"
    # WDESIGN = "wDesign"

def verify(req):
    """ verify that a request response is valid (returns a response code of 200) """
    if req.status_code != 200:
        return req.status_code
    else:
        return 1


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



def check_links_in_dir(root_folder):
    """ """
    
    passing = True

    for folder in PageDirs:
        dir_path = os.path.join(root_folder, folder.value)

        # iterate over all files in folder
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            # print("Checking {}".format(file_path))
            with open(file_path, "r", encoding="utf-8") as file_handle:
                file_str = file_handle.read()

                # check all links
                link_list = file_str.replace('src', '<<<SPL>>>').replace('href', '<<<SPL>>>').split('<<<SPL>>>')[1:]
                # print(link_list)
                for link in link_list:
                    link_parse = link.split('"')[1].split('"')[0]
                    print(" {} >> {}".format(file, link_parse))
        


    return passing

def test_valid_links():

    root = get_root_dir()
    ret_val = check_links_in_dir(root)
    assert ret_val == True