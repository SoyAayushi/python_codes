# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:11:05 2019

@author: Aayushi
"""

name=input("enter your name")
spaceIndex=name.find(" ")
print(name[spaceIndex+1:],name[:spaceIndex])