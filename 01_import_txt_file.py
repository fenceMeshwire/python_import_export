#!/usr/bin/env python3

# Python 3.9.5

# 01_import_txt_file.py

# Dependency
import os
from pathlib import Path

path = Path.home() # Set path e.g. to home directory
os.chdir(path) # Change working directory

with open('sample.txt', 'rt', encoding='utf-8') as fin:
    lines = fin.read()

print(type(lines)) # <class 'str'>
print(lines)
