#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit=number%10
# YOUR CODE HERE

print("Last digit of {} is {}".format(number,last_digit),end="")

if(last_digit>5):
    print(" and is greater than 5",end="")
elif(last_digit<6 and last_digit!=0):
    print(" and is less than 6 and not 0")
else:
    print(" and is 0")