import shared
from os import listdir, path

def get_tar_files():
    sub_files = listdir(shared.config["grade_dir"])
    tar_files = filter(lambda name: '.tar' in name, sub_files)

    userMap = {}

    for archive in tar_files:
        name = path.splitext(archive)[0]
        userMap[name] = archive

    return userMap
