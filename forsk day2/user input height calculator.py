# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:00:59 2019

@author: Aayushi
"""
#height in foots
x_height= int(input("enter your height in foots"))
#height in inches
y_height=int(input("enter your height in inches"))
#given parameters
one_foot=0.3048
one_inch=0.0254
#calculating height in foots and centimeters
in_5_foot=5.0*x_height
in_11_inch=11.0*y_height
new_height=in_5_foot+in_11_inch
print(new_height)
one_meter =100
new_foot=5.0*one_meter
new_inch=11.0*one_inch
#height in cwntimeters
new_cm_ht=new_foot+new_inch
print(new_cm_ht)