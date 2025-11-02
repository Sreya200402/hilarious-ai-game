
#builtin function

import builtins

#print(dir(builtins)) #list of builtin functions

for i in dir(builtins): # insequence of bulitin functions
    print(i)


#help function
help('max')

#anonymous functions
'''
Anonymous functions do not have any name.

They are defined using lambda keyword .
so they are also called as lambda function.

parameters neednot be enclosed in parenthesis.

return keyword is not necessary. the object present after colon
is returned automatically.

these will have single line of code .so complex structures using conditonal blocks and
loops cannot be represented as lambda functions .

syntax:

lambda parameters: return object

'''

#take no and increementing by 10
#by using functions
def increment(x):
    x += 10
    return x
print(increment(10))

#lambda function
increment = lambda a: a+10
print(increment(10))


#write a lambda function to return if sum of two given numbers is even or odd - true / false 

even = lambda n,z : (n+z) % 2 == 0
print(even(3,8))
print(even(20,88))



#lambda functions can be used with other higher order functions
#as arguments to help in their working
#example : map(), sorted(), filter(), etc

#map(), filter() iterate the objects without type casting and for loop
#we cannot print the result insted it gives <filter object at 0x00000292623CF130> for lambda with filter as a reference 

#lambda with map()
lst = [1,2,3,4,5,6,7,8,9,10]
new_lst = []
for i in lst:
   new_lst.append(i*2)
print(new_lst)


new_lst = list(map(lambda n:n*2, lst))
print(new_lst)

#lambda with filter()
#type casting
even_lst = list(filter(lambda i : i % 2 == 0 , lst))
print(even_lst)

#using  for loop
even_lst = filter(lambda i : i % 2 == 0 , lst)
for i in even_lst:
    print(i)


#lambda with sorted()

lst = ["ball","cat","donkey","apple"]
print(sorted(lst))
print(sorted(lst,reverse= True))
#custom sorting base on the len of each string in the list
print(sorted(lst, key = lambda s : len(s)))
print(sorted(lst, key = lambda s : len(s),reverse = True))

#convert a list of string to their uppercase
lst = input().split()
lst1 = list(map(lambda s:s.upper(),lst))
print(lst1)

#sort string by last char
lst = input().split()
print(sorted(lst,key=lambda s:s[-1]))

#filter numbers greated than 20
lst = list(map(int,input().split()))
new_lst = list(filter(lambda i : i > 20 , lst))
print(new_lst)



#divible by 4
lst = list(map(int, input().split()))
new_lst = list(filter(lambda i : i % 4 == 0 ,lst))
print(new_lst)


#palindrome
lst = input().split()
new = list(filter(lambda i:i == i[::-1] , lst))
print(new)
