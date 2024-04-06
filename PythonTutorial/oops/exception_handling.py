'''
Created on 06-Apr-2024

Exception Handling: Handling abnormal/unexpected behaviors of/from web sites.

Types of errors:
    1. Compile time errors : This cannot be handled. Coder/developer/programmer is solely responsible for this.
    2. Run time errors : These are unexpected and can be handled.

How to handle exception ?
Exceptions can be handled using:
    1. single try-single except block
    2. single try-specific except block
    3. single try-multiple specific except blocks
    4. single try-multiple specific except and single except default block 
    5. nested try - except blocks.
    6. try-except-finally
    
'''
'''
print("1+2=",1+2)
print("5-3",5-3)
print("4*3=",4*3)
print("9/0=",9/0) # the program terminates abruptly here.
print("2**5=",2**5)
print("9//4=",9//4)
'''
#Using try-block
'''
print("1+2 =",1+2)
print("5-3 =",5-3)
print("4*3 =",4*3)
try:
    print("9/0=",9/0) 
except:
    print("9/0 = ZeroDivisionError: division by zero")
print("2**5 =",2**5)
print("9//4 =",9//4)
'''
# To handle all types of errors in its own way 
'''
print("1+2 =",1+2)
print("5-3 =",5-3)
print("4*3 =",4*3)
try:
#    print("9/0 =",9/0) 
#    print("9/a = ",9/"a")
#    9=8 # Compile error, so throws error during compiling itself.
    a=[1,2,3,4]
    print(a[4]) # index error
except Exception as e:
    print("Exception thrown at line 5,",e)  
# OR 
#except:         # default except block, which can be used for handling any type of exception.
#    print("Exception thrown at line 5")
except ZeroDivisionError: # Throws during run time.
    print("9/0 = ZeroDivisionError: division by zero")
except TypeError:
    print("Type Error: Unsupported operand type(s) for /: 'int' and 'str'")
except SyntaxError:
    print("SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?")
print("2**5 =",2**5)
print("9//4 =",9//4)
'''
#Nested try-block and finally statement
print("1+2 =",1+2)
print("5-3 =",5-3)
print("4*3 =",4*3)
try:
    try:
        print(9/"a")
    except TypeError as te:
        print("Type Error: Unsupported operand type(s) for /: 'int' and 'str'")
except Exception as e:
    print("Exception thrown at line 5,",e)  
finally:  # independent of try, is executed no matter what. For default actions, like closing a browser after use etc.
    print("This is the 'finally' block")
print("2**5 =",2**5)
print("9//4 =",9//4)    
    
















