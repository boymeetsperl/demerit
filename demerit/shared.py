from os import getcwd
from yaml import load, dump

try:
    CONFIG = open(getcwd()+"/"+"config.yml", "r")
except IOError:
    print "can't load config"
    sys.exit(0)

opts = load(CONFIG)

GRADE_DIR = opts["grade_dir"]
DEMERIT_DIR = opts["demerit_dir"]
GEN_MAKEFILE = opts["gen_makefile"]
DEVNULL = open("/dev/null", "w")
