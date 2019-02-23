# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:08:08 2019

@author: Aayushi

"""
#Write a Python program to generate and print a list of first 
#and last 5 elements where the values are square of numbers between 1 and 30 (both included).
list1=[]
for i in range(1,31):
    list1.append(i**2)
print(list1[:6])
print(list1[-6:])
