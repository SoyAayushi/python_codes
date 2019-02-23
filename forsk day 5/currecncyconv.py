# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:09:59 2019

@author: Aayushi
"""
import json
import requests
url="http://data.fixer.io/api/latest?access_key=699acc8932a978eea97f449428ae38bb"
response=requests.get(url)
data=response.json()
print(data)
print(data['rates'])