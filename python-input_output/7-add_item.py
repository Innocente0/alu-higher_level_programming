#!/usr/bin/python3
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

args = sys.argv[1:]

file_name = "add_item.json"

if not os.path.exists(file_name):
    save_to_json_file([], file_name)

data = load_from_json_file(file_name)
data.extend(args)
save_to_json_file(data, file_name)
