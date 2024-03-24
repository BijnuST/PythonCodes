'''
Created on 10-Mar-2024

@author: bijnu
'''
year=int(input("Enter an year to determine whether it is a leap year or not :"))
#remainder=year%4
if((year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 )):
    print("Leap year")
else:
    print("Not a leap year")