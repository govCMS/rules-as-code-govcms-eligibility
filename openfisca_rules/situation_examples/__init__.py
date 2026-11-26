"""This file provides a function to load json example situations."""

import json
from os.path import abspath, dirname, join

DIR_PATH = dirname(abspath(__file__))


def parse(file_name):
    """Load json example situations."""
    file_path = join(DIR_PATH, file_name)
    with open(file_path, encoding="utf8") as file:
        return json.loads(file.read())


govcms = parse("govcms.json")
