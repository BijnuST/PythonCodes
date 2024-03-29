'''
1. Calling a function within itself :recursive function.

----------> We can call a function from one module to another module. Only user defined or 
predefined functions can be called. Built in functions cannot be. To use predefined, we have to import them.
2. 
'''
def decrement(a):
    while(a>0):
        a=a-1
        print(a)
        if(a>0): 
            decrement(a)         #recursive
        elif(a==0):
            break
    print("------------------")   
decrement(5)


