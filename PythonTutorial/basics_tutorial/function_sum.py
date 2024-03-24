'''
 SUM
'''
'''
# This function does not return value.
def add(a,b):       # function with parameters/arguments. These are formal arguments.
    total=a+b
    print("Sum is",total)
    
a=int(input("Enter a num :"))
b=int(input("Enter another num :"))
add(a, b)               # Actual arguments

print("____________________________________________________________________")
'''
'''
# This function returns one value.
def retvalue(a,b):       # function with parameters/arguments. These are formal arguments.
    total=a+b
    print("Sum is",total,". This is from within function")
    return total
    
a=int(input("Enter a num :"))
b=int(input("Enter another num :"))
returnedvalue=retvalue(a, b)
print("Returned value from function is",returnedvalue)

print("____________________________________________________________________")
'''
# This function returns multiple values.
def mult_retvalue(a,b):       # function with parameters/arguments. These are formal arguments.
    total=a+b
    diff=a-b
    print("This is from within function. Sum is",total,". Difference is",diff)
    return total,diff
    
a=int(input("Enter a num :"))
b=int(input("Enter another num :"))
ret1,ret2=mult_retvalue(a, b)
print("Returned values from function are: Sum =",ret1,"and Difference =",ret2)