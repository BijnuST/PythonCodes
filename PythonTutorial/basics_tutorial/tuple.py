'''
Dictionary
'''
d={1:"India",2:"Switzerland",3:"Canada"}
print(d[1])

d[2]="CH"
print(d)

c=[1,2,3,4]
print(d.fromkeys(c, "ABCD")) # iterable can be anything,list, num
c=[10,20,30,40]
print(d.fromkeys(c, "EFGH"))

print(d.items()) # lists as tuples
print(d.keys())
print(d.values())