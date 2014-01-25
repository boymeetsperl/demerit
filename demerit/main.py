import sys

import shared
from fetch import get_tar_files
from extract import extract_assign
from compile import gen_mk, create_mk, compile_dir, compile_all
from pprint import pprint

user_map = get_tar_files()
directories = extract_assign(user_map)

compiled = compile_all(directories)
pprint(compiled)
