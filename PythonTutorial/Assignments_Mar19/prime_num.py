'''
Write a program that checks if the given num is a prime num or not.
'''

num=int(input("Enter a num to find if its prime or not :"))
half=int(num/2)
flag=0
for i in range(half):
    i=i+2
    if(num%i==0):
        break
    else:
        flag=1
        continue
if(flag==1):
    print("Prime")
else:
    print("Not prime")