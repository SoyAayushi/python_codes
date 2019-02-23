# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:04:01 2019

@author: Aayushi
"""

name=input("enter your name")
spaceIndex=name.find(" ")
print(name[:spaceIndex], name[spaceIndex+1:])