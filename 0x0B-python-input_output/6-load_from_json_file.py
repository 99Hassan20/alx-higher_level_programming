#!/usr/bin/python3
"""module to handle json"""


import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
