import copy
from os import getcwd
from yaml import load, dump

try:
    CONFIG_FILE = open(getcwd()+"/"+"config.yml", "r")
except IOError:
    print "can't load config"
    sys.exit(0)

opts = load(CONFIG_FILE)
config = copy.deepcopy(opts)

DEVNULL = open("/dev/null", "w")
