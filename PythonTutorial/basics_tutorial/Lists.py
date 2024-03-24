'''
Index : Position value of any element present

left to rt is 0,1,2,...
rt to left is-1,-2,-3...
Lists doesnt sort automatically
List is mutable
List stores duplicate values
Insertion order is preserved
Empty set cannot be created.
Python provides built in functions for int float tuple etc etc
'''
c= list(range (2, 20, 2)) # from 2, till < 20, skipping 2
print("c-->",c)
c.append(22) # value
print("c after appending 22-->",c)
d=[1,2,3,4] # another list
c.append(d)
print("c after appending d-->",c) # issue with appending object is, it takes the entire d as a single thing.
print(c[10])

c.extend(d) # opens content of another list and merges to the list it was copied to
print(c)

e=c.copy() # to copy contents of one list to another
print("e =",e)

print(c.index(4))

print(c.index(2,2))

c.insert(5, 99)
print("After inserting 99 at index 5",c)

print("Before pop, c=",c)
print(c.pop(7)) #if specified index value,it removes particular element.If unspecified,the rt most will be popped out.
print("After pop, c=",c)

c.remove(2) # removes the value 2 that appears first
print(c)

c.reverse() 
print("After reversing",c)

c.pop(4)
c.sort()
print("After sorting : c =",c)

print(c.count(2))

print("Length of c =",len(c))
