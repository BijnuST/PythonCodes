'''
Write a program that asks user for numerical score and prints out the corresponding letter grade A,B,C,D or F
'''

'''Using elif'''
a=int(input("Please enter the score :")) 
b=int(input("Please enter the total :"))
c=((a/b)*100)
if(c>=85):
    print("You have scored A grade.Congrats!")
elif(c>=70):
    print("You have scored B grade.Good Work!")
elif(c>=55):
    print("You have scored C grade!")
elif(c>=40):
    print("You have scored D grade!")
else:
    print("You have scored E grade!")

'''Using flag 

a=int(input("Please enter the score :")) 
b=int(input("Please enter the total :"))
c=((a/b)*100)
flag=0
if(c<40):
    print("You have scored E grade!")
if((c>=85)and flag==0):
    print("You have scored A grade.Congrats!")
    flag=1
if((c>=70)and flag==0):
    print("You have scored B grade.Good Work!")
    flag=1
if((c>=55)and flag==0):
    print("You have scored C grade!")
    flag=1
if((c>=40) and flag==0):
    print("You have scored D grade!")
    flag=1
'''





