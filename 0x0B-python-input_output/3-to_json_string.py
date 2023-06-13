#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """
    Json representation of an object(string)

    Args:
        my_obj: string
    Return:
        json representation
    """
    return json.loads(my_obj)
