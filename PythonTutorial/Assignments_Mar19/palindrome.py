'''
Write a program that checks if given string is a palindrome.
'''
palindrome=input("Enter a string to check whether it is a palindrome or not :")

palindrome=palindrome.lower()

length=len(palindrome)
flag=1
j=length-1

for i in range(length):
    if(palindrome[i]!=palindrome[j]):
        flag=0
        break
    else:
        j=j-1

if(flag==1):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
    
    
