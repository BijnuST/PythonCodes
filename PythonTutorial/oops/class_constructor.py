'''
Created on 30-Mar-2024

Constructor :This is  a method used to construct an object.
1. Constructor is not mandatory. 
    There is a built in function dir. '__class__', '__delattr__', '__dict__'--> 
    The underscore is given for magic methods.Even though constructor is not mentioned,Py creates one on its own.
2. Constructor will be called implicitly when an object is created.
3. Constructor can be defined with/without parameters.
'''

class HumanBeing():
    def display_details(self): # constructor without parameter
        print("This is the method Human being.")
    def __init__(self):
        print("This is a constructor.")

me=HumanBeing()  # implicitly calling constructor. There is ambiguity, I am not sure which one would run.
#me.display_details()
me.__init__()   # explicitly calling constructor. Calling exact fn by name.
me.display_details()  
#print(dir(me))
  
        