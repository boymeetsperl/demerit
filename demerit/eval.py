import shared
from subprocess import call, check_output, Popen, PIPE, STDOUT
from subprocess import CalledProcessError

# this will contain the functions relevant to evaluating
# student programs.

# function to run program, maps student name to output from program
# or none, if the program did not successfully run or produce output

# returns output from running program, or None if unsuccessful
def run_program(path):
    arg_list = []
    arg_list.append(path)

    if shared.config["argv"] != None:
        arg_list.append(shared.ARGV)

    print arg_list

    try:
        prog = Popen(arg_list, stdout=PIPE, stdin=PIPE, stderr=shared.DEVNULL)
        output = prog.communicate(input=shared.config["stdin"])[0]
    except CalledProcessError:
        output = None

    return output
