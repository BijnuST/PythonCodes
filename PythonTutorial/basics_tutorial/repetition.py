#Black box testing == no look at code
#White box testing == look at code
'''
print num of times a number appears in the list

'''

a= [20,10,30,50,40,60,80,99]
print(a)
'''
for i in range(5):
    print(c[i]," repeats",c.count(c[i]),"times.")
'''
''' FOR Loop
b=a.copy()
for i in b:
    ele_count=b.count(i)
    print(f"{i}-->{ele_count} times") #giving f in the beginning formulises it and then copies the value present at the i index.
    for j in range(ele_count):
        b.remove(i)
'''
# WHILE Loop
b=a.copy()
i=0
while True:             # Infinite loop is given when we cannot say any condition for sure
    element=b[i]
    ele_count=b.count(element)
    print(f"{element} --> {ele_count} times")
    for j in range(ele_count):
        b.remove(element)
    if len(b)==0:       # when length og list gets reduced, it breaks out of the infinite loop
        break

        