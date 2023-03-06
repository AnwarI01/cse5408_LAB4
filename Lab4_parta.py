#Names: Anwar Ibrhaim, Luis garcia, Ileana Lopez
#Group 6
#CSE 5408 Spring 2023
#Lab 4

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
    
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:49:38 2023

@author: anwar
"""

def ConvertToMilitaryTime(time):
    
    #Checks if it is 12:00 AM
    if time[-2:] == "AM" and time[:2] == "12":
        Mil_time = "00" + time[2:-2]
        return Mil_time
    
    #Checks if it is 12 PM or anything past 12:59 AM
    elif (time[-2:] == "PM" and time[:2] == "12") or (time[-2:] == "AM"):
        Mil_time = time[:-2]
        return Mil_time
    
    #Will add 12 to the times from 1:00 PM to 11:59 PM
    else:
        Mil_time = str(int(time[:2]) + 12) + time[2:-2]
        return Mil_time
    
    

print("Enter a time to be converted to military time, e.g. 01:00 PM")
Time = input("Time to be converted to military time : ")

ConvertedTime = ConvertToMilitaryTime(Time)

print("Converted military time: ", ConvertedTime)