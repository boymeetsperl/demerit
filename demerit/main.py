from os import listdir, mkdir, path, chdir, getcwd
from subprocess import call
import yaml as yml
import sys

import shared
from fetch import get_tar_files

# the directory where the root of the demerit project is
# try:
#     CONFIG = open(getcwd()+"/"+"config.yml", "r")
# except IOError:
#     print "error loading config file"
#     sys.exit(0)

def extract_assign(user_map):
    assign_dir_map = {}

    for key in user_map:
        print key
        curr_dir = shared.GRADE_DIR + "/{}".format(key)
        curr_archive = shared.GRADE_DIR + "/{}".format(user_map[key])
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
    c_files = filter(lambda name: '.c' in name, listdir(assign_dir))

    makefile_lines = []
    makefile_lines.append("TARGET = "+assign_name+"\n")
    makefile_lines.append("SOURCES = " + " ".join(c_files)+"\n")
    makefile_lines.append("CFLAGS = -ansi -pedantic -Wall -lm\n")
    makefile_lines.append("include "+shared.DEMERIT_DIR+"/resources/edam.mk"+"\n")

    return makefile_lines

# takes a list of lines comprising a Makefile and places
# it in assign_dir. Returns True if successful else False
def create_makefile(makefile_content, assign_dir):
    try:
        makefile = open(assign_dir+"/"+"Makefile", "w")
        makefile.writelines(makefile_content)
        return True
    except IOError:
        print "Couldn't open Makefile for writing"
        return False

# compiles the program contained by dir_path
# returns True if successful, else if no Makefile
# found or compilation fails, return False.
def compile_dir(dir_path):
    print dir_path
    if path.isfile(dir_path+"/"+"Makefile") != True:
        return False
    else:
        chdir(dir_path)
        result = call(["make"], stdout=shared.DEVNULL)
        if result != 0:
            return False
        return True

user_map = get_tar_files()
directories = extract_assign(user_map)

print directories

if shared.GEN_MAKEFILE == True:
    successes = []
    fail = []
    for student in directories:
        print("generating makefile for: {}".format(student))
        mk_lines = gen_mk(directories[student], student)
        create_makefile(mk_lines, directories[student])
        if compile_dir(directories[student]) == False:
            print("compilation failed for {}".format(student))
            fail.append(student)
        else:
            successes.append(student)

print successes
print fail
