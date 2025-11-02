

#scope of the variable -
'''the region or the part of the program where a variable can be accessed is called as scope
'''
#1 . local scope -
'''
when the variable is defined inside an function ,
it can be accessed only within the function body
we call this as local scope where the variable is local to that function.
'''
def example(l,b):
    area = l*b
    print(area)#local
example(20, 10)
#print(area)#shows error since it is defined after the function call
#NameError as it is a local variable 

#2 global variable -
'''
when the variable is defined outside of every function present in the program
it is said to exist in global scope .

this kind of variable can be accessed in every part of program after its definition. 

incase we try to modify it , we get unboundlocal error as the interpreter seaches for the variable in local scope ,
to mention that it is a global variable , we use global keyword inside the function and
then the modification can be done.
'''
x = 5 # global
def example():
    global x
    x += 5 #trying to modify but it shows the error instead use "global keyword" to define x inside the function
    print(f"Inside Function : {x}")
example()
print(f"outside function : {x}")#global


#fixed length arguments

#sum of the three numbers
def sum_numbers(a,b,c):
    return sum((a,b,c))
print(sum_numbers(1,98,0))#fixed length arguments
#print(sum_numbers(1,98))#type error - missing 1 required positional argument
#print(sum_numbers(1,98,0,98))#type error - takes 3 positional arguments but 4 were given



#variable length arguments -
'''
variable  length arguments can be of 2 ways
1 . variable length positional arguments

we use * operator to pack all the given arguments into a tuple

we generally use args as name of that tuple by defining *args
as parameter inside the paranthesis. but that can be given any name

this tuple supports all the operations required for the logic


2 . variable length keyword arguments

We use ** operator to pack the given keyword arguments into a dictionary

we usaually give **kwargs and a dictionary with name Kwargs wiil be created.
We can use any name we want and this dictionary supports all kind of
dictionary operations

'''

#variable length positional arguments
def printing(*args):
    
    print(type(args))

    for i in args:
        print(i)
        
printing(27, 90)
printing(31, 87, 41 ,11, 65)
#o/p
'''
<class 'tuple'>
27
90
<class 'tuple'>
31
87
41
11
65
'''

#write a function that take n number of arguments and give the count of that arguments

def ex(*args):
    count = 0
    for i in args:
        count += 1
    print(count)

ex(12, 45, 78, 99)

#or

def accept(*args):
    return len(args)
print(accept(12,34,23))


#variable length keyword argument
def info(**kwargs):
    print(type(kwargs))

    for i , j in kwargs.items():
        print(f"Key: {i} - value:{j}")
info(insitute = "codegnan")
print()
info(insitute = "codegnan",location = "hyderabad" , course = "data analytics")


#passing the mutable and immutable objects 
def change(number):

    print(f"Inside befor: {number}")
    number += 1
    print(f"Inside after: {number}")
x = 10
change(x)
print(x)

####3
def change(lst):

    print(id(lst))

    print(f"Inside Before : {lst}")
    lst.append(10)
    print(f"Inside After: {lst}")

l = [1, 3.4, "python"]
print(id(l))
change(l)
print(l)


#passing mutable and immutable objects
'''
in python , a variable always has the object reference only.

=>when we are passing immutable objects ,
the modification made during the function execution ..
do not exit outside of the function,this is just is behaving like pass by value

=>when we are passing mutable objects , the modification made during the function execution,
exist outside the function . this like pass by reference.

'''

