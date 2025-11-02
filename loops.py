#loop - a programming structure used to repeat a block of code more than once
#for loop - no of iterations
#while loop - condition based
"""
#for loop
''' for var_name in iterable:
        #block of code
'''
for i in range(5):
    print(i)

'''o/p
0
1
2
3
4 '''

#print python 5 times
for i in range(1, 6):
    print("python")
print("Done")
'''o/p
python
python
python
python
python
Done '''

n = int(input("enter te value:"))
for i in range(0, n):
    print("python")
'''enter te value:4
python
python
python
python
'''    
#write a program to print numbers in range of 1 to given n    
n = int(input("enter the value: "))
for i in range(1 , n+1):
    print(i , end = " ") #without "end" the numbers will print vertically
'''enter the value: 3 #without end
1 2 3
enter the value : 3 #without "end"
1
2
3
'''
# print a table
n = int(input("\nenter the table: "))
for i in range(1 , 11):
    #n x 1 = 1n
    print(f'{n} X {i} = {n*i}')
'''
enter the table: 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
'''

#write a program that print even numbers in range of 1 to given n
n = int(input("enter the value:"))#12
for i in range(1, n+1):
    if i % 2 == 0:
        print(i,end = " ") #2 4 6 8 10 12

# write a program that print even numbers are ther in range of 1 and given n           
n = int(input("enter the value:"))#12
count = 0
for i in range(1, n+1):
    if i % 2 == 0:
        #print(i,end = " ")#2 4 6 8 10 12
        count += 1
print(count)#6

#write a program to check if given number is prime or not
n = int(input("enter the value:"))
fact = 0
for i in range(1, n+1):# 1 2 3 4 5
    if n % i == 0:
        fact += 1
if fact == 2:
        print("prime")
else:
        print("!prime")

lst = ['a' ,'b' ,124,'python']
for i in lst:
    print(i)
tup = ('a' ,'b' ,124,'python')
for i in tup:
    print(i)
s = {'a' ,'b' ,124,'python'}
for i in s:
    print(i)
d = {'a':1 , 'b':'sri','c':'hyd'}
for i in d:
    print(i)

#write a program to print number of elements present in the given input list without using len function
    #list will bw elements separated with space
lst = input("enter elements:").split()
count = 0
for i in lst:
        count += 1
print(count)

#write a program to print names whose score is greater
#than average score of all in the given 
d = {'Alex' : 30 , 'Bob' :40 ,'Charles':20 , 'David':50}
avg = sum(d.values())//len(d)
for i in d:
    val = d[i]
    if val > avg :
        print(i)
#d.values() , d.keys() , d.items()
for scores in d.values():
    print(scores)
for names in d.keys():
    print(names)
for items in d.items():
    print(items)
for keys , values in d.items():
    print(keys)
    print(values)

    
#loop control statements
#break - to come out of a loop early
basket = [12, 48, 32, 90, 11, 66, 88]
for i in basket:
    if i % 2 == 1:
       print(i)
       break
    print(i)
print("task done")

for i in range(10):
    if i == 5:
        break
    print(i)
'''o/p
0
1
2
3
4'''


#continue - to skip some steps in current iteration
lst = [11, 4, 21, 2, 6, 13]
s = 0
for i in lst:
    if i % 2 == 1:
        continue
    s += i
print(s)

for i in range(5):
    if i == 2:
        continue
    print(i)
'''o/p
0
1
3
4
'''

#else
#for with else - else body execute only when loop does not break
s = 'pythan'
for ch in s:
    if ch == 'a':
        print("present")
        break
    else:
        print("not present")

s = 'python'
for ch in s:
    if ch == 'a':
        print("present")
        break
    else:
        print("not present")

for i in range(3):
    print(i)
else:
    print("Loop completed")
'''o/p
0
1
2
Loop completed '''

#write a program where a input string is given (word) eg : 'python' o/p =6 characters such that consonent = 0 and vowels = 1
inp_str = input("enter the string:").lower()
op_str = ' '
for ch in inp_str:
    if ch in 'aeiou':
        op_str += '1'
    else:
        op_str += '0'
print(op_str)

#codechefATM
t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    withdraws = list(map(int, input().split()))
    op_str = ''
    for i in withdraws:
        if k >= i:
            op_str += '1'
            k -+ i
        else:
            op_str += '0'
    print(op_str)
"""

#while - condition based loop
'''while condition:
            #code to be executed
'''
i = 0 #initialization
while i < 10: #termination
    print('python')
    print(i)
    i += 1 #updation if we not incrementing results infinite loop

