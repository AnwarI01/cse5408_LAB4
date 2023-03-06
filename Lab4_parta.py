#Changes from Luis

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:04:39 2023

@author: luisg
Luis Garcia 
CSE5408 Lab04

"""
#Write a program containing a function to reverse a user 
#inputted string. [start:stop:step]
def Reverse(x):
    print("Here is the reveresed string:\n",x[::-1])

user_input = input("Enter a string : ")

print("Here is the Original word:\n",user_input)
Reverse(user_input)



#created Mon Feb 27 7:40 2023
#Ileana Lopez
#CSE5408 LAB 4
#part b: write a program containing a function to 
# check if user imputted number is prime
number = int(input("Enter any number: "))

# prime number is greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1 its not prime
else:
    print(number, "is not a prime number")