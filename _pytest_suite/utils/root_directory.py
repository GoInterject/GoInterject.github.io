import os

# ---------------------------------------------------------------
def get_par_dir(n, file):
    """ returns n parent directory of file """
    file_path = os.path.abspath(file)
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return file_path

# ---------------------------------------------------------------
# dir_travel_up is number of directories to travel up from the script dir
def get_root_dir(dir_travel_up):
    root = get_par_dir(dir_travel_up, __file__)
    return root
