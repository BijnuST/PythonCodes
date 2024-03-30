'''
Created on 30-Mar-2024

Constructor from parent class also is inherited and called implicitly when child class object is created.

'''
'''
class GrandFather:
    def __init__(self):
        print("This is constructor from class GrandFather")
    
    def gf_method(self):
        print("This is method from class GrandFather")
        
class Father(GrandFather):
    def __init__(self):
        print("This is constructor from class Father")
        #GrandFather.__init__(self)
        #GrandFather()
        super().__init__()
        
    def f_method(self):
        print("This is method from class Father")
        
    def car(self):
        print("This is car from class Father")

print("========GF==========")
a=GrandFather()

print("========F==========")
f=Father()
'''
class GrandFather:
    def __init__(self,name,age):
        self.name=name  # instance variables are tied with GF class object.
        self.age=age
        print("This is constructor from class GrandFather")
    
    def gf_method(self):
        print(f"Grandfather's name is {self.name} and he is {self.age} years old.")
        
class Father(GrandFather):
    def __init__(self,name,age,aadhar_id):
        self.aadhar_id=aadhar_id
        print("This is constructor from class Father")
        #GrandFather.__init__(self,name,age)
        super().__init__(name,age)
        
    def f_method(self):
        print(f"Father's name is {self.name} and he is {self.age} years old. His Aadhar ID number is {self.aadhar_id}")
        
    def car(self):
        print("This is car from class Father")

print("========GF==========")
a=GrandFather("GrandPa",80)
a.gf_method()
print("========F==========")
f=Father("Pa",50,9876)
f.f_method()