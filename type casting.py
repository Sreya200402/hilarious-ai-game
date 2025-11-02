#int()
a = 2
print(int(a))#2
print(float(a))#true 2.0
print(str(a))#true 2
print(bool(a))# true -1 , false -0
#0,1 bool of empty items is false and with items is true 
#print(dict(a))#false
#print(tuple(a))#-false
#print(list(a))#-false
#print(set(a))#-false


#float()
a = 6
print(int(a))#true 4
print(str(a))#true 4.0
print(float(a))#true 4.0
print(bool(a))# true -1 , false -0
#0,1 bool of empty items is false and with items is true 
#print(dict(a))#false
#print(tuple(a))#-false
#print(list(a))#-false
#print(set(a))#-false 

#str()
a = "jai"
#print(int(a))#false
#print(float(a))#false
print(str(a))#jai
print(bool(a))# True 
#print(dict(a))# false
print(tuple(a))# true ('j' , 'a' , 'i')
print(list(a))#true  ['j' , 'a' , 'i']
print(set(a))#true  {'j' , 'a' , 'i'}

#str()
a = "2"
print(int(a))# 2
print(float(a))# 2.0
print(str(a))#2
print(bool(a))#  True
#print(dict(a))# false
print(tuple(a))# ('2',)
print(list(a))# ['2']
print(set(a))# {'2'} 

#list
a = [1,2,3]
#print(int(a))#false
#print(float(a))# false
print(str(a))#[1,2,3] true
print(bool(a))# true 
#print(dict(a))# false must contain key value pairs only to evaluate as true
print(tuple(a))# (1,2,3)
print(list(a))# [1,2,3]
print(set(a))# {1,2,3}

#list
a =[1,89.7,"sru",(9,0) ,{12.5} ,[1,9]]
#print(int(a))#false
print(str(a))#true [ 1,89.7,'sru',(9,0) ,{12.5} ,[1,9]]
#print(float(a))#false 
print(bool(a))# true 
#print(dict(a))#false
print(tuple(a))#true (1, 89.7, 'sru', (9, 0), {12.5}, [1, 9])
print(list(a))# true [1, 89.7, 'sru', (9, 0), {12.5}, [1, 9]]
print(set(a))#false

#tuple
a = (1,34.4 ,"sry" ,(2,4),[1,4],{3,5},{'s':1} , False)
#print(int(a))#false
print(str(a))# true (1, 34.4, 'sry', (2, 4), [1, 4], {3, 5}, {'s': 1}, False)
#print(float(a))# false
print(bool(a))#True  
#print(dict(a))#false only keyvalue pairs are present
print(tuple(a))# true (1, 34.4, 'sry', (2, 4), [1, 4], {3, 5}, {'s': 1}, False)
print(list(a))#true [1, 34.4, 'sry', (2, 4), [1, 4], {3, 5}, {'s': 1}, False]
#print(set(a))#false


#dict()
a = {'a' : 1 , 'b' : 2 , 'c':4}
#print(int(a))#false
#print(float(a))# false
print(bool(a))# True 
print(dict(a))# true {'a': 1, 'b': 2, 'c': 4}
print(tuple(a))#true ('a', 'b', 'c')
print(list(a))#true ['a', 'b', 'c']
print(set(a))#true {'c', 'b', 'a'}

#dict()
a = {'a' : 'sre' , 'b' : 'ram' , 'c':'hii'}
#print(int(a))#false
#print(float(a))# false
print(bool(a))# True 
print(dict(a))# true {'a': 'sre', 'b': 'ram', 'c': 'hii'}
print(tuple(a))#true ('a', 'b', 'c')
print(list(a))#true ['a', 'b', 'c']
print(set(a))#true {'b', 'c', 'a'}


