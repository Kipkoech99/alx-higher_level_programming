#!/usr/bin/python3

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers['X-Request-Id']
    print(f'{x_request_id}')
