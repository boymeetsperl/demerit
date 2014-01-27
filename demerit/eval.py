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
        arg_list.append(shared.config["argv"])

    try:
        prog = Popen(arg_list, stdout=PIPE, stdin=PIPE, stderr=shared.DEVNULL)
        if shared.config["stdin"] != False:
            output, error = prog.communicate(input=shared.config["stdin"])
        else:
            output, error = prog.communicate()
    except CalledProcessError:
        print "failed"
        output = None
    return output

def run_all(executable_map):
    user_output_map = {}

    for student in executable_map:
        if executable_map[student] != None:
            output = run_program(executable_map[student])
            user_output_map[student] = output
        else:
            user_output_map[student] = None

    return user_output_map

def check_program(user, executable):
    # attempt to autoeval. if unsuccessful, ask me about it
    print("checking {}".format(user))
