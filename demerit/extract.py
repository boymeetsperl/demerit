from os import path, mkdir
from subprocess import call

import shared

def extract_assign(user_map):
    assign_dir_map = {}

    for key in user_map:
        curr_dir = shared.config["grade_dir"] + "/{}".format(key)
        curr_archive = shared.config["grade_dir"] + "/{}".format(user_map[key])
        if path.exists(curr_dir) != True:
            mkdir(curr_dir)

        status = call(["tar", "-xf", curr_archive,
                      "--directory", curr_dir])
        if status != 0:
            print("problem extracting {}".format(user_map[key]))
            assign_dir_map[key] = None
        else:
            assign_dir_map[key] = curr_dir
    return assign_dir_map
