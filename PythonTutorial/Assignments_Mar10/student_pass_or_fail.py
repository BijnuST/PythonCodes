'''
Student pass or fail
'''
print("Please enter marks scored for each subject below")
Maths=int(input("Maths :"))
English=int(input("English :"))
Social=int(input("Social :"))
Science=int(input("Science :"))
IILang=int(input("II Lang :"))

print("Please enter the total marks")
Total=int(input())
Score=Maths+English+Social+Science+IILang
Result=(Score/Total)*100

if Result>25:
    print("You have scored ",Result," and passed the exam! ")
else:
    print("Sorry, you did not pass the exam..You have scored only ",Result)