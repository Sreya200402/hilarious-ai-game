#Functions
"""
Function is a reusable block of code to do a specific task

syntax:

     def fun_name(parameter1,parameter2......): function can be defined with
     key word 'def' along with function name with paranthesis to pass parameters
     or arguments
     function definition would return print nothing if i didnot call function

     

        #function body with indentation

        return value


 function definition would return print nothing if i did call function

    def product(a, b): #function definition  with parameters 
    
    pr = a*b
    print(pr)


Function will not run with definition , to run that block of code
we have to make function call

how to make function call ?

function call has to made using function name by passing the values to the parameters
these are actual values are called arguments
ex : fun_name(arg1, arg2,.....)


key points:

1. "def" is a keyword used to define function
2. parameters are variables used to pass values to the functions
3. "return" keyword is used to get values out of the functions
4. if we do not write any return statement, by default function returns none
5. Once the control reaches return, it will be the last statement
anything written after return statement will not be executed.
"""

def fun(a , b):
    print(a+b)

ans = fun(2, 3) # 5
print(ans)# output 5
print(ans * 2) #will give  TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'


###
def fun(a , b):
    print(a+b)

ans = fun(2, 3)# 5
ans = fun(4, 6) # 10
print(ans)# output 5 , 10



###
def add(a, b):
    return a + b

result = add(2, 3)
print(result)       # Output: 5
print(result * 2)   # Output: 10




#product of two numbers

def product(a, b): #function definition  with parameters 
    
    pr = a*b
    print(pr)

    
print('start')
product(2,4) #function call with arguments
print('done')
product(12,8)
product(1,10)



#how to use return

def product(a, b): #function definition  with parameters 
    

    pr = a*b
    print(pr)
    return pr

product(12,3) #nothing is printed without 'print' statement


########
def product(a, b): #function definition  with parameters 
    

    pr = a*b

    return pr
    print('done')#return will be last line after return print will not be executed

result = product(13,3)
print(result)





#write a program to check whether the number is even or odd

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(7))

####
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(even_odd(7))

#write  a function to print the greatest three numbers

def great(a , b , c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
print(great(6,9,19))


#write a function to check given number is composite or not

def composite(n):
    if n <= 1:
        return False # 0 and 1 are not composite


    for i in range(2,n):
         if n % i == 0:
            return True # Found a divisor other than 1 and itself

    return False # No divisors found, so it's prime
print(composite(45))
    
print(composite(2))




######
number = int(input("enter the number:"))

def composite(n):

    if n == 2:
        return False
        
    for i in range(2,n):

        if n % i == 0:
            return True
    return False
print(composite(number))

#passing values to the parameters as arguments can be done in 3 ways
#1.positional arguments -
"""
Passing the arguments based on the position of the parameters . in case we change the order ,
arguments will be collected in wrong variables.
"""

def info(name,age):
    print(f"Name:{name}")
    print(f"Age:{age}")
info("bob",38)#positional arguments - order of arguments is essential


# 2 .default arguments -
"""
The values to the parameters are assigned during the function definition only
In case we dont give the any arguments during the function call ,
default values will be considered
there can be the combination of parameters of non default and non default parameters ,
but always define all the non default arguments first and then the default.
"""
def info (name = "bob" , age = 30): #default parameters
    print(f"Name : {name}")
    print(f"Age: {age}")
info()#default arguments
info("john",40)#actual arguments (positional)
info("jay") #changing name for default arguments

####
def info (name, age = 30): #default parameters and positional parameters
    print(f"Name : {name}")
    print(f"Age: {age}")
info("jay") 

###

#def info (name = "jay", age): #default parameters and positional parameters but system take non default arguments(positional) first then default arguments
def info (age , name = "Jay"):
    print(f"Name : {name}")
    print(f"Age: {age}")
info(30)



#keyword arguments
'''
these arguments are passed during the function call using the parameter names
here the order of the parameters is not important
'''
def info(name, age):
    print(f"Name: {name}")
    print(f"Age:{age}")
info(name = "John",age = 40)#keyword arguments where order is not neccesary



