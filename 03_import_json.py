#!/usr/bin/env python3

# Python 3.9.5

# 03_import_json.py

# Dependency
import json

article = {
    'product': 'Sledge Hammer XXL',
    'EAN-Code': '6411501200280',
    'Country of origin': 'Finnland',
    'Price': '$70'
}

# Convert a json object to a string object with dumps() method
str_article = json.dumps(article)
print(article)

# Convert a string object to a json object with loads() method
article = json.loads(str_article)
print(article)
