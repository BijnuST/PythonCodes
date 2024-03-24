'''
Created on 10-Mar-2024

Data Types

@author: bijnu
'''
import sys 
# the following comes under numerical data types
a=2 # int 28 bytes :: hard coded values
b=3.5 # float 24 bytes
c=6+8j # complex 32 bytes
# string data type
d="Nice day!"
#boolean
e=True
f=False
#None type
g=None

print(type(a))
print(sys.getsizeof(a))
print(type(b))
print(sys.getsizeof(b))
print(type(c))
print(sys.getsizeof(c))
print(type(d))
print(sys.getsizeof(d))
print(type(e))
print(sys.getsizeof(e))
print(type(f))
print(sys.getsizeof(f))
print(type(g))
print(sys.getsizeof(g))