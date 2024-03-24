'''
Write a program that prints the nums from 1 to 100.
For multiples of three, print "Fizz".
For multiples of five, print "Buzz"
For multiples that are multiples of both three and five, print "FizzBuzz"
'''

for i in range(100):
    i=i+1
    if(i%15==0):
        print(i,"FizzBuzz")
        continue
    elif(i%3==0):
        print(i,"Fizz")
        continue
    elif(i%5==0):
        print(i,"Buzz")
    else:
        print(i)
    
        