#rules for variables
""" Variable names can only contain letters, digits and underscores (_).
A variable name cannot start with a digit.
Variable names are case-sensitive (myVar and myvar are different).
Avoid using Python keywords (e.g., if, else, for) as variable names."""

# multiple variables in single line
A,B = 4, 6
#print (A,B)
print(A)
print(B)

#assingning variables in single with same value
x = y = z = 100
print(x , y , z)


#numeric data type ( integer/float/complex numbers)
int_var = 5
float_num = 145.90
com_num = 2+4j
print(int_var , float_num , com_num , sep = "  -  " , end = '   ')
print("Hello World")


# sequence data type ( string (' ' or " " ) , list [] , tuple ())
str_var = 'python'
list_var = [1 , 'Python' , 123.45]
tuple_var = (1,2,3)
print(str_var)
print(list_var)
print(tuple_var) 


#unordered - set data type
set_var ={1,2,3}
num = frozenset( {1,2,3})
print(set_var)
print(num)

#mapping type

dictionary = { 'name' :'Sreya' , 'password' : 'password'}
print(dictionary)

#Boolean -True, False
is_active = True
is_active = False
print(is_active)


#None type
is_present = None
print(is_present)










