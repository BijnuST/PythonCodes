'''
Every function defined inside a class is called a method.

First we have to create a class, then we have to create an object from the class and 
then call the class using the object.
'''
# Defining a class
class HumanBeing():
    def display_details(self):
        print("I am a human.")

# Created an object which belongs to HumanBeing class  --- Instantiation
me=HumanBeing()
# Called a method from HumanBeing class using object me.
me.display_details()
#Checking type of object
print(type(me))
        