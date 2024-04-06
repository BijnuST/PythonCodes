'''
Created on 30-Mar-2024

Any variable or method of a class is its property.

Inheritance : 
1. Single level inheritance : Parents class gets only from GrandParents class. ( GP--> P )
2. Multi-level inheritance : Child class gets from both Parents and GrandParents class. ( GP--> P --> C)
3. Multiple inheritance : Child gets from ( GP--> P--> C <--A ). The order in which class is called matters.

Method Resolution Order : MRO :  is a built in function.
'''

'''
#No Inheritance here
class GrandParents:      # cannot call methods from Parents class.
    def gp_method(self):
        print("This is method gp")

class Parents:          # cannot call methods from GrandParents class.
    def p_method(self):
        print("This is method p")
 
gp=GrandParents()
p=Parents()

gp.gp_method() 
p.p_method()
'''    
'''
# By passing Grandparents class in to Parents class, the properties can be inherited.
class GrandParents:      
    def gp_method(self):
        print("This is method gp")

class Parents(GrandParents):          # Inheriting everything from Grandparents class
    def p_method(self):
        print("This is method p")
 
gp=GrandParents()
p=Parents()

gp.gp_method() 
p.p_method()
p.gp_method()  # able to call Grandfathers class' method.
'''
class GrandParents:      
    def gp_method(self):
        print("This is method gp.")
    def car(self):
        print("This is method car from class GrandParents")

class Parents(GrandParents):          # Inheriting everything from Grandparents class
    def p_method(self):
        print("This is method p.")
    def car(self):
        print("This is method car from class Parents")
        GrandParents.car(self)
        
class Aunt:
    def a_method(self):
        print("This is method a.")
    def car(self):
        print("This is method car from class Aunt")
 
class Child(Parents,Aunt):  # Multiple Inheritance. Inheriting everything from Parents class which includes GarndParents class properties as well.
    def c_method(self):
        print("This is method c.")
    def car(self):
        print("This is method car from class Child")
        Parents.car(self)
        Aunt.car(self)
        
        
gp=GrandParents()
p=Parents()
me=Child()

print("=======================GrandParents Class===========================")         
gp.gp_method() 
p.p_method()

print("=======================Parents Class===========================") 
p.p_method()
p.gp_method() 

print("=======================Child Class===========================") 
me.c_method() 
me.gp_method()
me.p_method()
me.a_method()
me.car() # MRO : The order in which call goes is , first within, net goes to the first class name, and then to the next, then to the next

print("=======================MRO===========================") 
print(Child.mro())