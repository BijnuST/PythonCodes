'''
5 stars
  *
 ***
***** 
OR
6 stars
   *
  **
 ****
****** 
'''
count=int(input("Enter the num of rows :"))
for i in range(count):
    for j in range(count-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
