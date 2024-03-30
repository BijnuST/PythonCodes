'''
Created on 30-Mar-2024

@author: bijnu
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)  