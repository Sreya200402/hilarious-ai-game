#tuple - immutable , ordred , heterogenous , unclosed in round paranthesis

t = ( 1 , 45.87 , "pthon" , [1,2,3] , (91,4,60),{1 , 7, 4})
print(t)
print(type(t))


#empty tuple
e_t = ()
empty = tuple()# usually this tuple() is used to type converstion but without any arguments it creates the empty tuple
# str()  list() to give string , list empty
print(e_t)
print(empty)


# tuple input
tup = tuple(input("enter ele:").split())
print(tup)

#int tuple
tup1 = tuple(map(int , input("enter ele:").split()))
print(tup1)

#(2) - in tuple after given the element with comma then it consideres as tuple
single_ele = ("python",)
print(single_ele)

#implicit tuple creation

my_tuple = 1,2,8,0,4 # if not place in round paranthesis by default it creates the tuple
print(my_tuple)
print(type(my_tuple))


#tuple operations

#tuple concatenation - +
tup1 = (1 ,2 , 3)
tup =  ('a','b','c')
res = tup1 + tup
print(res)

#nested tuple
tuple1 = (1,2,34.4,"sreys" ,true,[1,3])
tuple2 = (1,2,3)
tuple3 = (tuple1 , tuple2)
print(tuple3)
print(len(tuple3))
res = tuple1 + tuple2
print(len(res))

#tuple repetition - *
tup_1 = (1,2,3)
r = tup_1 *3
print(r)

#tuple indexing 
t = (1,2,3,4,5)
print(t[0])
print(t[-1])

#slicing
tup_ = (1 , 2 , 4 , 5 ,6 ,8)
slic = tup_[0 : 4 : 2]
print(slic)

# login , logout(9:00, 15:00) #3000m, 8hrs per day
logs = (9.00 , 15.00)#3000 , 8 hrs per day
login_time = logs[0]
logout_time = logs[1]
hours = logout_time - login_time
sal = 3000/8 *hours
print(sal)


# membership operators
t = (1,[4,5],6,5)
print(4 in t)
print(5 in t)


# in built fuctions - len(),min(),max(),sum(),sorted()
tup = (1 , 23.4 ,[1,2],{1,3},"python")
print(len(tup))

t = (45,78,90,2,34)
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t))



#tuple methods  - tuple.object.function_name
#tuple.
t = (1,1,2,3,4,4,4,4,5)

print(t.count(4))
print(t.index(1))


#tuple unpacking 

details = ('bob' , 'bob@gmail.com' , 'DS')
name , gmail , batch = details
print(name)
print(gmail)
print(batch)


t = (1 , [2 , 3] ,6)
t[0] = 10 # tuple is immutable so shows type error
print(t)

t[1][1] = 30
print(t) # here we change elements in list which is part of tuple and it gives(1,[2,30],6)


#list to tuple
list = [1,2,3]
print(tuple(list))




















