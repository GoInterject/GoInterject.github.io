from enum import Enum
import os
import logging


class PageDirs(Enum):
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
                        print("Checking if >> {} image location exists".format(imagelink_parse))
                    except:
                        passing = False
                        print(">> ERROR Image link in: {} is broken and cannot be parsed.".format(file_path))
                        return passing

                    if os.path.exists(root_folder + imagelink_parse):
                        passing = True
                       # print(" >> {} exists".format(os.path.basename(imagelink_parse)))
                    else:
                        passing = False
                        print(">> ERROR {} does not exist. \n File location at: {}".format(os.path.basename(imagelink_parse), file_path))
                        return passing
    
    return passing


def test_valid_imagelinks():

    root = get_root_dir()
    ret_val = check_image_links_in_dir(root)
    assert ret_val == True