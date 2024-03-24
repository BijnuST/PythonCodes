'''
Operators : They are symbols which performs operations on one or more 
operands(variables).
1. Arithmetic : +,-,*,/,% ,**(exponents),//(integer division) (ip numeric op numeric )
2. Logical : AND, OR, NOT ( ip boolean op boolean )
3. Assignment operator : =
4. Relational or Comparison operators : >,<,>=,<=,==,!= (ip numeric,op boolean )
5.a. Increment operator : +=
5.b. Decrement operator : -=
6. Membership operators : in,not in
7. Identity operators : is, is not (This operator not only checks the value,it checks the value 
and datatype are exactly the same)
'''
'''
a=12
b=21
c=a+b
print(c)
#String
a=input("Please enter a number :")
b=input("Please enter a number :")
c=a+b #concantination happens here
print("Sum of",a," and",b," is",c)
#print(type(a))
#print(type(b))
#print(type(c))
#Integer
a=int(input("Please enter a number :"))  #type-casting
b=int(input("Please enter another number :"))
c=a+b 
print("Sum of",a," and",b," is",c)
c=a//b
print("Exponential value =",c)
#print(type(a))
#print(type(b))
#print(type(c))
'''
'''
# Logical operators - AND , OR, NOT
print("---------AND------------")
print("True and True =",True and True)
print("True and False =",True and False)
print("---------OR------------")
print("True or False=",True or False)
print("True or True=",True or True)
print("---------NOT-----------")
print("not True=",not True)
print("not False=",not False)
'''
'''
print("Relational Operators")
print(2>3)
print(2>=3)
print(2<3)
print(2<=3)
print(2==3)
print(2!=3)
'''
'''
print("Increment operation")
a=int(input("Please enter a number :"))
a+=1
print("a =",a)

print("Decrement operation")
a-=1
print("a =",a)
'''
'''
print("Membership operators")
print('b' in 'Bijnu')
print ('U' not in 'Bijnu')
'''
'''
print("Identity operators")
a=2
b=2.0
print(a is b)
print(a==b)
print(id(a))
print(id(b))
# no separate containers are created in this case
print("Identity operators")
 a=2

 
b=2
print(a is b)
print(a==b)
print(id(a))
print(id(b))
'''
