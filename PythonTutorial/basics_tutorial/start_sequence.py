'''
*
**
***
****
*****


for i in range(5):
    for j in range(i+1):
        print("*",end=" ") 
    print() # using empty print statement moves cursor to new line.
'''
from _ast import If
''' Triangle
   * 
  ***
 *****
*******
'''
    
    
''' Inverse triangle
*****
****
***
**
*

for i in range(5): # rows
    for j in range(5-i): # column
        print("*",end=" ")
    print()
'''   
    
'''
*
**
***
****
*****
****
***
**
*
'''

r=int(input("Enter the number of stars required : "))
for i in range(r):
    if(i<=r):
        for j in range(i+1):
            print("*",end=" ") 
        print() 
  
for i in range(r):
    r=r-1  
    for k in range(r):  
        print("*",end=" ")
    print()      