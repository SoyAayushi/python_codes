# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:20:42 2019

@author: Aayushi
"""

#my weight in kgs
weight= int(input("whats your weight?"))
print(weight)
#my height in meters
height_foot= int(input("enter your height in foots"))
#enter height in inches
height_inch=int(input("enter your height in inches"))
print(height_foot)
print(height_inch)
#concatenation of foots and inches
height = height_foot*height_inch
print(height)
#calculating bmi
dval1 = weight/height
dval2= dval1/height
#bmi
bmi = dval2
print(bmi)
pdi= bmi/height
print(pdi)