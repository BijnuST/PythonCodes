'''
While loop can define condition and the loop will be executed until condition is me.
For loop is for srqunetial

syntax : while count<=200:

Loop control statements : break and continue.These control the execution of the loop.

Continue is like skip..it skips particular values..loop is not executed for particular values. 
Continue is given before loop executes. 

Whatever comes after continue is skipped, but th eloop will be completed.
Break will break out of the loop.
'''
#While loop

count=1
while count<=20:
    if count==100:
        count=count+1
        continue
    print(count)
    count=count+1
    
#for loop - goes over seq going one by one. 

for count in range(5): # range is default function-- starts from 0
    print("Hi there")
    
#for i in "India":
#    if i=='I'