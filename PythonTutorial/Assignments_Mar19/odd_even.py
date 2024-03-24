'''
Write a program that asks the user for a number and determines whetehr its Odd or Even
'''
num=int(input("Enter an number to determine whether it is an odd or even number : "))
remainder=num%2
if(remainder == 0):
    print(num,"is an EVEN number.")
else:
    print(num,"is an ODD number.")