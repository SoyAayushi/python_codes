# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:08:20 2019

@author: Aayushi
"""

n=0
while(n<51):
    n=n+1
    if(n%3==0):
        print("fizz")
    elif(n%5==0):
        print("buzz")
    else:
        print(n)
    if(n%3==0 and n%5==0):
        print( "fizzbuzz")
        
       