'''
Write a program that asks the user for two numbers and determines which one is greater.
'''
a=int(input("Please enter a number :")) 
b=int(input("Please enter another number :"))
if(a>b):
    print(a,"is greater than",b,".")
if(a<b):
    print(b,"is greater than",a,".")
if(a==b):
    print("Both numbers are the same.")