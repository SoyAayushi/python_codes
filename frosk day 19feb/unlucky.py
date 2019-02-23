# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:58:58 2019

@author: Aayushi
"""

input_string = input("Enter a list element separated by space ")
list1  = input_string.split()
if input_string==" ":
    print("input should be in integer")
    
for item in list1:
    if item != 13:
        sum = 0
        index_13=input_string.index(13)
        #del input_string(index_13 + 1)
for num in list:
    sum += int (num)
print("Sum = ",sum)
