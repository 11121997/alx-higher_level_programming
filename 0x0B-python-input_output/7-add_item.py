#!/usr/bin/python3
"""Load, add, save module"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

the_list = list(sys.argv[1:])

try:
    the_data = load_from_json_file('add_item.json')
except Exception:
    the_data = []

the_data.extend(the_list)
save_to_json_file(the_data, 'add_item.json')
