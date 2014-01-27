from os import getcwd
from yaml import load, dump

try:
    CONFIG = open(getcwd()+"/"+"config.yml", "r")
except IOError:
    print "can't load config"
    sys.exit(0)

opts = load(CONFIG)

config = {}
for key in opts:
    config[key] = opts[key]

DEVNULL = open("/dev/null", "w")
