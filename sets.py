#sets - mutable , unordered collection of unique and immutable elements enclosed in curly parenthesis
#no indexing and slicing

s = {1,78.3,True,'python',(9,0)} # True = 1  no duplicate values
print(s)
s = {78.3,True,'python',(9,0)}
print(s)
s = {False,78.3,True,'python',(9,0)} # set treat True as 1 and False as 0 and it throws an error if we give list and dictionary
print(s)
print(type(s))

#empty set
empty_set = set()
print(empty_set)
e_t = {} # not create a set it create the empty dictionary
print(e_t)
print(type(empty_set))
print(type(e_t))

#input() in sets (user input())
inp = set(input("element:").split())
int_inp = set(map(int,input("elements:").split()))
print(inp)
print(int_inp)

#operations on sets
# built-in fuctions
s = {1,2,3}
print(len(s))
print(min(s))
print(max(s))
print(sum(s))
print(sorted(s))#always used to return list
print(sorted(s , reverse = True))

#write a program to finf the no of diffrent character present in a given string
#example - apple =4 , python -6 ,moon =3
s = input("enter elements:").lower()
unique = set(s)
res = len(unique)
print(res)


#set methods - setobj.method()
#set.

s = {1,2,3}
#adding elements
#add(ele) - adds single element
s.add(4)
print(s)

#update(group of elements)
s.update({5,6,7})
print(s)

#removing elements
#remove(ele) - remove the single element
s.remove(5)
print(s)
#s.remove(9)#shows error
#print(s)

#discard(ele) -remove the single element
s.discard(6)
print(s)
s.discard(9) # doesnot show sny thing for safer removal we use discard
print(s)


#pop() arbitary removal
s.pop()
print(s)

#clear()
s.clear()
print(s)

#set operations - union , intersection ,difference , symmetric difference
#set.

a = {1,2,3,5,7}
b ={4,5,6,8,9}
# | or union() - either in  set a or set b
c = a|b
print(c)

c = a.union(b)
print(c)
c = b.union(a)
print(c)

#& or intersect
c = a&b
print(c)

c  = a.intersection(b)
print(c)
c = b.intersection(a)
print(c)


#- or difference()-either in set a or set b
c = a-b
print(c)

c = a.difference(b)
print(c)
c = b.difference(c)
print(c)


# ^ or symmetric_difference
c = a^b
print(c)

c = a.symmetric_difference(b)
print(c)
c = b.symmetric_difference(a)
print(c)



# write a program tp print a list of numbers such that it contain missing numbers print those missing numbers
#in the range 1-10
numbers = set(map(int,input("elements:").split()))
full_range = list(range(min(numbers), max(numbers) + 1))
missing_numbers = sorted(list(set(full_range) - set(numbers)))
print("Original list:", numbers)
print("Missing numbers:", missing_numbers)

#or
numbers = set(map(int,input("elements:").split()))
set_num = {1,2,3,4,5,6,7,8,9,10}
diff = set_num - numbers
print(sorted(diff))

#superset() , subsets()
a = {2,4,6}
b ={1,2,3,4,5,6,7}
print(a.issuperset(b))
print(b.issuperset(a))
print(a.issubset(b))


#disjointsets()
print(a.isdisjoint(b))



















