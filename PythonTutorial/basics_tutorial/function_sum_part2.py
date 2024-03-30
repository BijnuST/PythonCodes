'''
Types of arguments:
1. Formal arguments
    a. Default arguments
    b. Variable length positional arguments
    c. Variable length actual arguments
2. Actual arguments
    a. Positional arguments
    b. Keyword arguments
Positional arguments : add(2,3)
Formal arguments are being used as keys : Keyword arguments : add(b=4,a=5)

Special cases:
a. Passing positional and keyword arguments for single function.

'''
def add(a,b):
    print(a," ",b)
    c=a+b
    print(c)
print("Positional arguments")    
add(4,2) 
print("Keyword arguments")    
add(b=4,a=1)
#print("Syntax error, positional arg cannot be passed after keyword arg")    
#add(8,b=6)
print("To add default formal arguments.")  
def addition(a=0,b=0):
    print(a," ",b)
    c=a+b
    print(c)
    
addition(2)

print("To add n number of arguments. Variable length arguments.")  
def addn(*a): #positional arguments
    c=0
    for i in a:
        c=c+i
    print(c)

addn(1,2,3,4,5)

print("Variable length keyword arguments.")  
def display_details(**a):
    print(a)
display_details(a=1,b=2,c=3,d=4,e=5)

print("Mixing positional and keyword arguments.") 
mixed_v_arg(1,2,3,4,c=3,d=4,e=5)


