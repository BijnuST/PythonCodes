'''
Write a program that determines whether a given character is a vowel or consonant
'''
a=input("Please enter a character to determine whether it is a vowel or consonant : ") 
if (len(a)>1):
    print("Please enter a single character.")
else:
    if ((a>='a' and a<='z') or (a>='A' and a<='Z')):
            if(a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U'):
                print(a,"is a vowel.")
            else:
                print(a,"is a consonant.")
    else:
        print("Incorrect input.")    