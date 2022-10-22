#!/usr/bin/env python3

# Python 3.9.5

# 04_import_json_to_python_data_model.py

# Dependency
import json

article = '{"product": "Sledge Hammer XXL", "ean_Code": "6411501200280", "country_of_origin": "Finnland", "price": "$70"}'
article = article.encode('utf-8')

class JSONObject:
    def __init__(self, dictionary):
        self.__dict__ = dictionary

# Create a Python object
json_data = json.loads(article, object_hook=JSONObject)

# Separate the single values from article variable - in order to create the 'data model':
json_data
json_data.product
json_data.ean_Code
json_data.country_of_origin
json_data.price
