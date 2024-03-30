'''
Created on 30-Mar-2024

Types of variables:

1. Instance/Object variables. Their values changes from object to object. This can be declared anywhere.
2. Static/Class variable. Can be used in code with classname.class variable name. Refer line#17
3. Method/Local variables.

Note:
Instance/Object variables can be declared anywhere with the help of self keyword.
Static/Class variables can be declared anywhere with the help of class name.
'''

class Student():
    school_name="iQuest" # Static or class variable
    def __init__(self,name,rollno):
        self.name=name # Object/instance variables. Their vale changes from object to object.
        self.rollno=rollno
    
    def display_details(self):
        print(f"{self.name} has {self.rollno} as roll number. The student is from {Student.school_name}.")
        
    def display_total_score(self,english,science,maths):
        self.english=english # this converts local variable to instance variable. Now this can be used in any where.
        total=english+science+maths #Method/Local variable. This cannot be used outside display_total_score.
        print(f"The total score is {total}")
        
    def display_english_score(self):
        print(f"{self.name} has scored {self.english} in English")

me=Student("ABCD",101)
me.display_details()
me.display_total_score(95,85,75)
me.display_english_score()