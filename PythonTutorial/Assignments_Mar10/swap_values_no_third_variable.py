'''
Swap values without a third variable
'''
print("Enter two variables")
variable1=int(input())
variable2=int(input())
print("Before swapping")
print("Variable1=",variable1)
print("Variable2=",variable2)
variable1=variable1+variable2
variable2=variable1-variable2
variable1=variable1-variable2
print("After swapping")
print("Variable1=",variable1)
print("Variable2=",variable2)