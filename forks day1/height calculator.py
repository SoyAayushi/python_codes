# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:25:46 2019

@author: Aayushi
"""



#current age
my_age=21
#my past age after 5 years
future_age = my_age+ 5
print(future_age)
#my age before 10 years
past_age = my_age-10
print(past_age)





 #my height 
height=5.11
#given parameters
one_foot=0.3048
one_inch=0.0254
#calculating height in foots and centimeters
in_5_foot=5.0*one_foot
in_11_inch=11.0*one_inch
new_height=in_5_foot+in_11_inch
print(new_height)
one_meter =100
new_foot=5.0*one_meter
new_inch=11.0*one_inch
#height in cwntimeters
new_cm_ht=new_foot+new_inch
print(new_cm_ht)

#my weight in kgs
weight= 55
#my height in meters
height=1.65
#calculating bmi
dval1 = weight/height
dval2= dval1/height
#bmi
bmi = dval2
print(bmi)



#my weight in kgs
weight= 55
#my height in meters
height=1.65
#calculating bmi
dval1 = weight/height
#calculating pdi
dval2= dval1/height
bmi = dval2
pdi= bmi/height
print(pdi)



#target heart rate range
age = 21
print(age)
#maximum heart range
print("maximum heart range :")
mhr = 220-age
print(mhr)
print("lower range of heart target :")
L_range = mhr * 70/100
print(L_range)
print("upper range of heart target:")
U_range = mhr*85/100
print(U_range)

#temperature in jaipur in degree celcius
temp = 29
print("temperature in jaipur in degree celcius:")
print(temp)
#convert in degree fahrenheit
Deg_F = temp*9/5+32
print("temperature in degree fahrenheit:")
print(Deg_F)
#convert to degree kelvin
print("converting in kelvin:")
Deg_K=temp+273
print("tenmperature in degree kelvin:")
print(Deg_K)

#distance travelled by car in killometers
distance = 100
print("distance covered by car:100")
#fuel used in car in litres
f_val = 5
print("fuel used in car: 5")
print("average of car:")
avg = distance/ f_val
print(avg)


#to and fro travelled distance in km
dist_total = 80
print(dist_total)
f_p_L= 80
#fuel average in km per litre
fuel_avg = 18
print(fuel_avg)
total_fuel = f_p_L/fuel_avg
print(total_fuel)
total_cost = dist_total*total_fuel
print(total_cost)







#object fall time in seconds
time= 10
acceleration = -9.81
print(time)
print(acceleration)
dist = (acceleration*time*time)/2
print(dist)


#weighted score calculator
assignments = 3
exams = 2
max_score = 100
A_1 = max_score * 10/100
print(A_1)
A_2 = max_score * 10/100
print(A_2)
A_3 = max_score * 10/100
print(A_3)
E_1 = max_score * 35/100
print(E_1)
E_2 = max_score * 35/100
print(E_2)
weighted_score = (A_1+A_2+A_3)*0.1+(E_1+E_2)*0.35
print(weighted_score)





