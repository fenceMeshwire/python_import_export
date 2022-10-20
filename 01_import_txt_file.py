#!/usr/bin/env python3

# Python 3.9.5

# 01_import_txt_file.py

# Dependency
import os
from pathlib import Path

path = Path.home()  # Set path e.g. to home directory
os.chdir(path)      # Change working directory

with open('sample.txt', 'rt', encoding='utf-8') as fin:
    # The read() method stores all lines from the file in a string variable.
    lines = fin.read()

print(type(lines))  # <class 'str'>
print(lines)        # print result

with open('sample.txt', 'rt', encoding='utf-8') as fin:
    # The readlines() method stores all lines from the file in a list:
    lines = fin.readlines()
    # Separate newline character \n from list elements:
    lines = [line.strip() for line in lines]

print(type(lines))  # <class 'list'>
print(lines)        # print result
