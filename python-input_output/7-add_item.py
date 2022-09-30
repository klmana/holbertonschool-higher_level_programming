#!/usr/bin/python3
"""
  Script that adds all arguments to
  a Python list, and then save them to a file or
  (create an object):
"""
import sys

save_the_json = __import__('5-save_to_json_file').save_to_json_file
load_the_json = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    the_new_one = load_the_json(file)
except (ValueError, FileNotFoundError):
    the_new_one = []
for args in sys.argv[1:]:
    the_new_one.append(args)
save_the_json(the_new_one, file)
