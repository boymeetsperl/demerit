import shared

from os import listdir, chdir, path
from subprocess import call

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
def create_mk(makefile_content, assign_dir):
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
    if path.isfile(dir_path+"/"+"Makefile") != True:
        return False
    else:
        chdir(dir_path)
        result = call(["make"], stdout=shared.DEVNULL, stderr=shared.DEVNULL)
        if result != 0:
            return False
        return True

# returns a mapping between student name and path of executable
# created from compilation. path is None if compilation fails
def compile_all(assign_dir_map):
    user_executable_map = {}

    for student in assign_dir_map:
        if compile_dir(assign_dir_map[student]) == True:
            exec_path = assign_dir_map[student]+"/"+student
            user_executable_map[student] = exec_path
        else:
            user_executable_map[student] = None

    return user_executable_map
