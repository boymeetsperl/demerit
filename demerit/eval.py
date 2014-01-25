import shared
from subprocess import call, check_output

# this will contain the functions relevant to evaluating
# student programs.

# function to run program, maps student name to output from program
# or none, if the program did not successfully run or produce output

# returns output from running program, or None if unsuccessful
def run_program(path):
    try:
        output = check_output(path)
    except CalledProcessError, e:
        print(e.returncode)
        output = None

    return output
