# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:21:50 2019

@author: Aayushi
"""

#to and fro travelled distance in km
dist_total = int(input("enter the total to fro distance in kms"))
print(dist_total)
f_p_L= 80
#fuel average in km per litre
fuel_avg = 18
print(fuel_avg)
total_fuel = f_p_L/fuel_avg
print(total_fuel)
total_cost = dist_total*total_fuel
print(total_cost)
