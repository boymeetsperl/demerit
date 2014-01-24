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
    print dir_path
    if path.isfile(dir_path+"/"+"Makefile") != True:
        return False
    else:
        chdir(dir_path)
        result = call(["make"], stdout=shared.DEVNULL)
        if result != 0:
            return False
        return True
