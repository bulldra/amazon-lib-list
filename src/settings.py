#!/usr/bin/env python3
__version__ = "0.1.0"

import os
import json

def load_json_setting(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    if os.path.exists(path):
        conf = open(path, 'r')
        return json.load(conf)
    else:
        return None

def load_text_list(path):
    result = []
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path, 'r') as conf:
        for line in conf.read().splitlines():
            result.append(line)
    return result

settings_dict = load_json_setting('../config/settings.json')
secrets_dict = load_json_setting('../config/secrets.json')

kindle_xml = settings_dict['kindle_xml']
outfile = settings_dict['outfile']

