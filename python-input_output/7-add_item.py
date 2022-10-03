#!/usr/bin/python3
""" script that add arguments to a python list"""
from sys import argv
import os.path

if __name__ == '__main__':

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    load_json_file = __import__('6-load_from_json_file').load_from_json_file

    update = []
    f = "add_item.json"
    if os.path.exists(f):
        update = load_json_file(f)
    save_to_json_file(update + argv[1:], f)
