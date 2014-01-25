import sys

import shared
from fetch import get_tar_files
from extract import extract_assign
from compile import gen_mk, create_mk, compile_dir

user_map = get_tar_files()
directories = extract_assign(user_map)

print directories

working = []
failing = []

if shared.GEN_MAKEFILE == True:

    for student in directories:
        print("generating makefile for: {}".format(student))
        mk_lines = gen_mk(directories[student], student)
        create_mk(mk_lines, directories[student])

        if compile_dir(directories[student]) == False:
            print("compilation failed for {}".format(student))
            failing.append(student)
        else:
            working.append(student)

print("working: {}".format(working))
print("failing: {}".format(failing))
