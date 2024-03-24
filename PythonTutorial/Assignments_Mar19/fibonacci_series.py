'''
Fibonacci Sequence generator
    Write a program that generates the fibonacci series upto a specified limit. 
Prompt the user to enter the number of terms they want in fibonacci series.
'''
limit=int(input("Enter the number of terms you want in the Fibonacci series :"))
list1=[0]
a=1
for i in range(limit):
    list1.append(a)
    a=list1[i]+list1[i+1]
print(list1)