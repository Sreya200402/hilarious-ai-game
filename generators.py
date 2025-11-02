#Generators

'''
These are the special function that are used to produce
a series of values on demand .

Working of generators:

These are "yield" keyword instead of "return" keyword
Yeild keyword helps to pause the execution of the function
and yield the value whie remembering the state of execution.

When we make function call ,
a special kind of object called called generator object
is returned rather than executing the entire function.


We use a built in function called "next()" on this generator object to
execute the defined generator function.

First usage of next() starts the execution and the consecutive usage
help in resuming from the point where ever it left off.
continue usage of next() even after the complete execution result in stopIterationError
'''


def fun():

    print(1) #1
    return 1 #1.....# the function ends here. what if i want to print 1 , 2 , 3 we use generators
    print(2)
    return 2
    print(3)
    return 3
#print(fun())
ans = fun()
print(ans)

#o/p : 1
#      1

 
#generator

def gen_fun():
    print(1)
    yield 1
    print(2)
    yield 2
    print(3)
    yield 3

ans = gen_fun() #creates the generator object
#next()
print(next(ans)) #1,1
print(next(ans))  # 2,2
print("generator!!")
print("hello dora!!!")
print(next(ans)) # 3,3



#write a generator function that can produce infinite series of natural numbers

def gen_nat():
    n = 1
    while n > 0:
        
        yield n # the function stops and print 1 without for loop
        n += 1
res = gen_nat()
print(next(res))#1
print(next(res))#2
for i in range(10):#print  next 10 natural numbers after 2
     print(next(res))


#write a generator function to return infinite exponent values of a given number starting from 0th exponent

def gen_expo(base):
    expo = 0
    while True:
        yield base ** expo
        expo += 1
    
power = gen_expo(2)
print(next(power)) # 2**0 = 1
for i in range(10):
    print(next(power))




