# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 18:14:40 2019

@author: Aayushi
"""

name=input("enter your name:")
spaceIndex = name.find(" ")

print ( name[spaceIndex+1:],name[:spaceIndex])
