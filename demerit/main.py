from os import listdir, mkdir, path, chdir, getcwd
from subprocess import call

GRADE_DIR = "/Users/ianmcgaunn/submissions"
DEVNULL = open("/dev/null", "w")
# finds association between student names and .tar files
def get_tar_files():
    sub_files = listdir(GRADE_DIR)
    tar_files = filter(lambda name: '.tar' in name, sub_files)

    userMap = {}

    for archive in tar_files:
        name = path.splitext(archive)[0]
        userMap[name] = archive

    return userMap

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

# generates a makefile for the current assignment
# given its directory and its name
def gen_mk(assign_dir, assign_name):
    cwd = getcwd()
    c_files = filter(lambda name: '.c' in name, listdir(assign_dir))

    makefile_lines = []
    makefile_lines.append("TARGET = "+assign_name+"\n")
    makefile_lines.append("SOURCES = " + " ".join(c_files)+"\n")
    makefile_lines.append("CFLAGS = -ansi -pedantic -Wall -lm\n")
    makefile_lines.append("include "+cwd+"/resources/edam.mk"+"\n")

    try:
        makefile = open(assign_dir+"/"+"Makefile", "w")
        makefile.writelines(makefile_lines)
    except IOError:
        print "Couldn't open Makefile for writing"

# compiles the program contained by dir_path
# returns True if successful, else if no Makefile
# found or compilation fails, return False.
def compile_dir(dir_path):
    print dir_path
    if path.isfile(dir_path+"/"+"Makefile") != True:
        return False
    else:
        chdir(dir_path)
        result = call(["make"], stdout=DEVNULL)
        if result != 0:
            return False
        return True

user_map = get_tar_files()
directories = extract_assign(user_map)

print directories

gen_mk(directories["something"], "something")
