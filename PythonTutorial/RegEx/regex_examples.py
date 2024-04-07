'''
Created on 07-Apr-2024

1. Mobile Number Validation
    - have 10 digits
    - 1st digit should be any digit from 5 - 9
    - remaining digits can be any from 0 - 9
    
reg=[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
reg="[5-9][0-9]{9}
reg="[5-9]\d{9}
'''
import re
'''
number=input("Please enter a mobile number - ")
reg="[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
print(re.search(reg,number))
#output
#Please enter a mobile number - 9087654321
#<re.Match object; span=(0, 10), match='9087654321'>
#Please enter a mobile number - 5tghn67890poikjhgfdesaz
#None
'''
'''
number=input("Please enter a mobile number - ")
reg="[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
match_object=re.search(reg,number)
if match_object!=None:
    print("The phone number is valid !")
else:
    print("The phone number is invalid !")
# Output
#Please enter a mobile number - 512346789p
#The phone number is invalid !
#Please enter a mobile number - 09876543211234567890
#The phone number is valid ! ---> but this is wrong, so , using full match.
'''
'''
number=input("Please enter a mobile number - ")
reg="[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
#match_object=re.fullmatch(reg,number)
match_object=re.findall(reg,number)
print("match_object =",match_object)
if match_object!=None:
    print("The phone number is valid !")
else:
    print("The phone number is invalid !")
'''
'''
#Reducing repetition of reg -- reg="[5-9][0-9]{9}
number=input("Please enter a mobile number - ")
reg="[5-9][0-9]{9}"
#match_object=re.fullmatch(reg,number)
match_object=re.findall(reg,number)
print("match_object =",match_object)
if match_object!=None:
    print("The phone number is valid !")
else:
    print("The phone number is invalid !")
'''
#Reducing repetition of reg -- reg="[5-9]/d{9}
number=input("Please enter a mobile number - ")
reg="[5-9]/d{9}"
#match_object=re.fullmatch(reg,number)
match_object=re.findall(reg,number)
print("match_object =",match_object)
if match_object!=None:
    print("The phone number is valid !")
else:
    print("The phone number is invalid !")


