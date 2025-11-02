#recursion #backtracking
'''
It is the programing technique where function call itself to solve smaller problems of the same kind

Syntax:
def fun_name(parameters):

      #base case

      #fun_name(parameter with samaller problem)#recursive call
base case:
It is the condition that specifies where the recursive calls have to stop

It is mandatory in all recursive functions
without a base case , the function execution gives you maximum recursive depth exceeded error

We use this technique when we need backtracking in our logic
as the lastest called function will get the return value first
following the previously called function and so on.
'''


#printing python n times
# n = 3
def printing(n): # 3 ,2 , 1
     #base
    if n == 0:
        return #without the return and condition the recursive function runs n times even you call the function 3 times
    
    print("python")
    printing(n-1)#recursive call # 2,1,0

    
printing(3)#function call(main)


#write a recursive function to calculate the factorial of given number

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(5))#120
print(fact(10))#3628800

#write a recursive function to calculate te sum of first n natural numbers
#recursive method
def natural_recursive(n):
    if n == 1:
        return 1
    else:
        return n + natural_recursive(n - 1)


#mathematical formula 
def natural(n):
    if n == 1:
        return 1
    else:
        return n * (n + 1) // 2
print(natural(5))#15
print(natural(10))#55


#nth term in fibonacci series using recursion # 0,1,1, 2,3,5
def fibonacci(n):
    if n <= 0:
        return "invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:    
        return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(6))

#fibonacci series
def sum_fibonacci(n):
    if n <= 0:
        return 0
    else:
        return fibonacci(n) + sum_fibonacci(n - 1)

    
    
