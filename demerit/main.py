from os import listdir, mkdir, path
from subprocess import call

GRADE_DIR = "/Users/ianmcgaunn/submissions"
# finds association between student names and .tar files
def get_tar_files():
    sub_files = listdir(GRADE_DIR)
    tar_files = filter(lambda name: '.tar' in name, sub_files)

    userMap = {}

    for archive in tar_files:
        name = archive.split(".")[0]
        userMap[name] = archive

    return userMap
# takes a mapping between student name and archive
# and extracts each archive to new directory corresponding
# to student name.
def extract_assign(user_map):
    assign_dir_map = {}

    for key in user_map:
        print key
        curr_dir = GRADE_DIR + "/{}".format(key)
        curr_archive = GRADE_DIR + "/{}".format(user_map[key])
        if path.exists(curr_dir) != True:
            mkdir(curr_dir)

        print("current file: {}".format(curr_archive))
        print("current directory: {}".format(curr_dir))
        status = call(["tar", "-xf", curr_archive,
                      "--directory", curr_dir])
        if status != 0:
            print("problem extracting {}".format(user_map[key]))
            assign_dir_map[key] = None
        else:
            assign_dir_map[key] = curr_dir
    return assign_dir_map

user_map = get_tar_files()
directories = extract_assign(user_map)

print directories
