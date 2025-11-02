#conditional statements
"""conditional statements are used to help to execute certain block of code based on whether given condition is true or false
1. if , nested if
2. if-else
3.if elif-else
"""
#if
#sytax:
'''
if condition:
    firstline
    secondline
    thirdline
'''
#check whether the number is +ve or-ve
'''inp = int(input("Enter the Number:"))
if inp >= 0 :
          print('Positive Number')

print('completed')'''# if i give positive integer it print to print statements ,
#if it is -ve number then it return nothing just return second print statement


'''
write a program to print the cube of the number
if it is divible by 3 , the fourth power of a number
if it is divisible by 4 and
square if it is not divisible by any of the two
'''
#nested if 
'''
n = int(input("Enter the Number:"))
if n%3 == 0:
    print("cube of number:" , n**3)
if n%4 == 0:
    print(" fourth power :" , n**4)
if not(n%3 == 0 or n%4==0) :
    print(n**2)
'''

#if - else
#syntax:
'''
if condition :
    # if block of code
else :
    # else block of code
'''
#check whether the number is +ve or-ve
'''
inp = int(input("Enter the Number:"))
if inp >= 0 :
          print('Positive Number')
else :
    print('Negative number')
'''

#check whether the number is even or odd
'''
number = int(input("enter the number:"))
if number%2 == 0:
    print('even number')
else:
    print('odd number')
'''

#write a program line - words in list line 2 = word check line 2 is in line 1
'''
words = input("enter the words:").split(",")
word = input("enter the word:")
if word in words:
    print("present")
else:
    print("not present")

'''
#write a program to check vowel or consonent
'''
word = input("enter the alpha:")
vowels = 'aeiouAEIOU'
if word in vowels:
             print('vowel')
else:
    print('consonent')
'''
#check if student is present find avg is student not present return not there
'''student = {
    'alex' : [12,25,30] ,
    'bob':[25,20,15],
    'charles':[25,22,20]
    }
'''
students = {
    'alex' : [12,25,30] ,
    'bob':[25,20,15],
    'charles':[25,22,20]
    }
'''
student1 = input("enter the name:")
if student1 in students:
    marks = students[student1]
    avg = sum(marks)//len(marks)
    print(avg)
else:
    print("details not found")
'''
#i have certain basket that can exactly fit in 20 items .
# given a dictionary with item name as key and count as value .
#check whether all the item can fit in ,. print "yes" or "no"

'''eg :
    input{'pens':10 , 'books':13}
    o/p=no

{'apple':10,'oranges':5}
o/p = yes
'''
'''
d = eval(input("enter the values:"))
no_of_units = sum(d.values())
if no_of_units <= 20:
    print("yes")
else:
    print("no")
'''

#above 15000 -20percent
#above 10000-15per
#above 5000-5per
#print the final amount to be paid by customer
#input customer bill
'''
inp = int(input("enter the amount:"))

if inp > 15000:
    dis = 0.20 * inp
if inp > 10000 and inp <=15000:
    dis = inp * 0.15
if inp > 5000 and inp <= 10000:
    dis = inp * 0.05
if inp < 5000:
    dis = 0
final_amount = inp - dis
print("final amount:",final_amount)

'''
'''
n = int(input("enter the bill:"))
if n > 15000:
    d = n * 0.20
elif n >= 10000:
    d = n * 0.15
elif n > 5000:
    d = n * 0.05
else:
    d = 0
final = n - d
print(final)

'''





#if - elif ....- else
'''
n = int(input("enter the number:"))
if n > 0 :
    print("if")
    print("positive")
elif n < 0 :
    print("elif")
    print("-ve")
else:
    print("else")
    print("zero")

'''




'''
write a program to take a number  as input and do the following
1 if the number is in range of 50 and 100 and is divisible by 3 print divisible
2 . if the number in range of 50 and 100 and is not divisible by 3 print not divisible
3. if it is not in the range print NOT in range
 '''
'''
n = int(input("enter the number:"))
if n >= 50 and n <= 100 and n % 3 == 0:
    print("divisible")
elif n >= 50 and n <= 100 and n % 3 != 0:
    print("not divisible")
else:
    print("NOT in range")

'''
#nested conditional statements = condition is placed inside another condition
'''
n = int(input("enter the number :"))
if n >= 50 and n <= 100:
    if n % 3 == 0:
        print("divisible")
else:
    print("not divisible")
'''
'''
for household -
first 100 units-rs 2/units
next 200 units - rs . 3/units
after that for every unit - rs . 4
For commercial-
first 100 units-rs 3/units
next 200 units - rs . 4/units
after that for every unit - rs . 5
input
commercial
400 - 300+800+500 = 1600
150 -300+200 =500
'''
# Input type of connection and units consumed
connection = input("Enter connection type (household/commercial): ")
units = int(input("Enter number of units consumed: "))

bill = 0

if connection == "household":
    if units <= 100:
        bill = units * 2
    elif units <= 300:
        bill = (100 * 2) + (units - 100) * 3
    else:
        bill = (100 * 2) + (200 * 3) + (units - 300) * 4

elif connection == "commercial":
    if units <= 100:
        bill = units * 3
    elif units <= 300:
        bill = (100 * 3) + (units - 100) * 4
    else:
        bill = (100 * 3) + (200 * 4) + (units - 300) * 5

else:
    print("Invalid connection type!")

print("Total bill amount:", bill)



