#pattern printing

#square
'''
enter side: 4
* * * * 
* * * * 
* * * * 
* * * * 
'''

n = int(input("enter side: "))
for i in range(n):#0 t0 n-1 0r 1, n+1 for n times
    print("* " * n)
#or
n = int(input("enter side: "))
for i in range(1 , n+1):#0 t0 n-1 0r 1, n+1 for n times
    print("* " * n)

#rectangle
'''
enter length:5
enter breadth:4
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''

# l , b are given print rectangle dynamically based on given l , b
l = int(input("enter length:"))
b = int(input("enter breadth:"))
for i in range(1 , b+1):# 0,b
    print("* " * l)

#hallow square
'''
enter the size:6
* * * * * * 
*         * 
*         * 
*         * 
*         * 
* * * * * *
'''
size = int(input("enter the size:"))
 #outer loop
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size -1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

 # Inner part
for i in range(1, size - 1):
    for j in range(1, size - 1):
        print(" ", end=" ")
    print()


#or
n=int(input('enter n:'))
for i in range(1,n+1):
    if i==1 or i==n:
            print("* "*n)
    else:
            print("*"+" "*(2*n-3)+"*")

#hallow rectangle
'''
enter l:4
enter b:5
* * * * 
*     *
*     *
*     *
* * * *
'''
l=int(input('enter l:'))
b=int(input('enter b:'))
for i in range(1,b+1):
    if i==1 or i==b:
            print("* "*l)
    else:
            print("*"+" "*(2*l-3)+"*")


#right angle triangle
'''
enter n : 6
*
**
***
****
*****
******
'''
n = int(input("enter n : "))
for i in range(1, n+1):
    print("*"*i)
    
#inverse right angle triangle
'''
enter n: 6
******
*****
****
***
**
*
'''
n = int(input("enter n: "))
for i in range(1 , n+1):
    print("*"*(n-i+1))

#triangle
'''
Enter the number : 4
   *
  **
 ***
****
'''
n = int(input("Enter the number : "))
for i in range(1 , n+1):
    print(" "*(n-i) + "*" *i)

# H formating
'''
enter the value:6
*    *
*    *
*    *
******
*    *
*    *
'''
# Height of the pattern
n = int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        # Print stars at the first and last column, and middle row
        if j == 0 or j == n-1 or i == n//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


#or
n = int(input("enter n:"))
mid = n//2+1
for i in range(1 , n+1):
    if i == mid :
        print("*" *n)
    else:
        print("*" + " "*(n-2)+"*")


#pattern with number
'''
enter the n : 5
1
22
333
4444
55555
'''
n = int(input("enter the n : "))
for i in range (1 , n+1):
    print(str(i) * i)

'''
enter the value:3
1
12
123
'''
n = int(input("enter the value:"))
output = ''
for i in range(1,n+1):
    output += str(i)
    print(output)

'''
enter n : 2
a
bb
'''

n = int(input("enter n : "))
out = " "
for i in range(1 , n+1):
    out = chr(96 + i) * i
    print(out)
'''
enter the n :5
 a
 ab
 abc
 abcd
 abcde
 '''
n = int(input("enter the n :"))
output = ' '
for i in range(1, n+1):
    output += chr(96 + i) 
    print(output)


    
    '''
    Enter the size of the house: 4
   * 
  * * 
 * * * 
* * * * 
* * * * 
* * * * 
* * * *
'''
  

#house    
size = int(input("Enter the size of the house: "))
for i in range(1, size * 2):
    if i <= size:
        # Roof: centered triangle
        print(' ' * (size - i) + '* ' * i)
    else:
        # Body: rectangle
        print('* ' * size)

#rhombus - parallelogram
size = int(input("Enter the size : "))
for i in range(1, size + 1):
    if i <= size:
        # Roof: centered triangle
        print(' ' * (size - i) + '* ' * size)
'''
Enter the size : 5
    * * * * * 
   * * * * * 
  * * * * * 
 * * * * * 
* * * * *
'''
        
#diamound
size = int(input("Enter the size of the diamond: "))

# Top half
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)

# Bottom half
for i in range(size - 1, 0, -1):
    print(' ' * (size - i) + '* ' * i)
'''
Enter the size of the diamond: 4
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   *
'''
