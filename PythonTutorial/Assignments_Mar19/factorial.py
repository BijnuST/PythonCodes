'''
Factorial
Write a program that calculates the factorial of a number.
'''
num=int(input("Enter a num to find factorial of :"))
factorial=1
for i in range(num):
    factorial=factorial*(i+1)
print("Factorial is :",factorial)