#!/usr/bin/python3
"""module to handle json"""


import json


def from_json_string(my_str):
    """convert from json"""
    return json.loads(my_str)
