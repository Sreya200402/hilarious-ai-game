#dictionary - mutable , ordered , key based indexing ,collection of key value pairs unclosed in curly braces where key is immutable and unique and no restriction for values
d = {'name':'sreya' , 'rollno': 234 , 'age' : 34 ,'location':'Hyd'}
print(d)
print(type(d))

#dict()
empty_dict = {}
print(empty_dict)

e_d = dict()
print(e_d)


#type casting to dictionary
lst = [('a',1) , ('b',2) ,('c',3)]
d = dict(lst)
print(d)


#dictionary input
#eval() - evaluates everything as true 

print(eval('6+11'))
print(eval('sum((1,2,3))'))


inp = eval(input("enter elements:")) #if we give int , str , list, tuple it takes because of 'eval' and evaluates to corresponding type
print(inp)
print(type(inp))


#dict opearations
#accessing values using indexing
d = {'name':'sreya' , 'rollno': 234 , 'age' : 34 ,'location':'Hyd'}
#key based indexing
print(d['location'])
print(d['name'])
print(d['age'])
print(d['rollno'])


#builtin functions - len() , max(), min(), sum(),sorted()
d = {'name':'sreya' , 'rollno': 234 , 'age' : 34 ,'location':'Hyd'}

print(len(d))
print(min(d))
print(max(d))
my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print(total)  # Output: 60

print(sorted(d))


#dictionary methods = dict.method()
menu = {'biryani':300 ,'chickentikka':500 ,'desserts':800}

#inserting key value pairs 
menu['starter'] = 200 #for adding single pair key value
print(menu)

#replacing values
menu['biryani'] = 800
print(menu)

#update()- if we want to add multiple key value pair 
menu.update({'ice_cream' : 700 , 'juice' :400})
print(menu)

#accessind values - get()
#print(menu('startes'))#error
print(menu.get('starters',-1))

#remove elements - pop() , popitem() , clear()
menu.pop('desserts')
print(menu)
menu.popitem()
print(menu)
menu.clear()
print(menu)

#accessing the keys , values ,keyvalue pairs(items())
d = {'name':'sreya' , 'rollno': 234 , 'age' : 34 ,'location':'Hyd'}
print(d.keys())
print(d.values())
print(d.items())



# write a program to find the avg of age in a dictionary by taking input from users

age = eval(input("enter dict:"))
avg_age = sum(age.values()) // len(age)
print(avg_age)




