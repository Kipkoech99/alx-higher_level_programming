#!/usr/bin/python3

import json

def load_from_json_file(filename):
    """A function that creates an object from json file"""
    with open(filename) as f:
        json.loads(f)
