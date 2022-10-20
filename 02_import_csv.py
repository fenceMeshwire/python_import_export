#!/usr/bin/env python3

# Python 3.9.5

# 02_import_csv.py

# Purpose: Import data from a CSV file.

# Dependency
import csv
import os
from pathlib import Path

path = Path.home()  # Set path e.g. to home directory
os.chdir(path)      # Change working directory

# Import the CSV file as a list and the headline (which is stored in a separate variable):
with open('sample.csv') as fin:
    csv_file = csv.reader(fin)
    headline = next(csv_file)   # Headline is stored separately
    
    for row in csv_file:
        print(row)
        
    print(headline)
