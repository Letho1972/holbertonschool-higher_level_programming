#!/usr/bin/python3
"""creates an Object from a JSON file """

import json

def load_from_json_file(filename):

    """Open the file in read ('r') mode using the with"""

    with open(filename, 'r', encoding="utf-8") as file:

        """Use the json.load() function to read
        and parse the JSON content from the file"""

        return json.load(file)
