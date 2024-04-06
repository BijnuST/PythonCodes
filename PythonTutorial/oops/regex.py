'''
Created on 06-Apr-2024

Regular Expressions (RegEx)
    RegEx is used for validating input. It has to be imported from a module called 're'. 
Its predefined, but not built in.


'''
import re  # Ctrl+click on re to see the documentation.
a="Hel123lo"
print(re.search("Hello", a))
print(re.search("hELLO", a))
print(re.search("h.", a))
print(re.search("l.", a)) #. represents any character except new line.
print(re.search(".l", a)) #. represents any character except new line.
print(re.search("^l", a)) #. matches start of the string.
print(re.search("^H", a)) #. matches start of the string.
print(re.search("l$", a)) #. matches end of the string.
print(re.search("o$", a)) #. matches end of the string.
print(re.search("Hello*", a)) #. matches as many repetitions as possible.
print(re.search("l+", a))
print(re.search("ll?", a))
print(re.search("ll*", a))
print(re.search("l+", a))
print(re.search("\d{2,5}",a))
print(re.search("\D{2,5}",a))
print(re.search("\w",a))
print(re.search("\w{1,3}",a))
print(re.subn("\d", "*", a,7))
print(re.split("\s", a,3))
print(re.findall("\s",a))
print(re.findall("\s",a))