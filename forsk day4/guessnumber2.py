# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:48:01 2019

@author: Aayushi
"""


winning_num=44
guess = 1
game_over= False
num=int(input("guess a number between 1 to 100:"))
print(num)

while not game_over:
    if guess<6:
        
        if(num==winning_num):
            print(f"you have guessed it right in {guess} times")
            game_over=True
        else:
            if(num<winning_num):
                print("too low")
                num=int(input("guess again:"))
                guess=guess+1
            else:
                print("too high")
                num=int(input("guess again:"))
                guess=guess+1 
                
    else:
        print("Exceed limit")
        break
            