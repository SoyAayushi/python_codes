# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:37:12 2019

@author: Aayushi
"""

import requests
url="https://free.currencyconverterapi.com/api/v6/convert?apiKey=sample-api-key&q=USD_PHP&compact=y&callback=sampleCallback"
response=requests.get(url)
data=response.json()
print(data)