
#output formatting
a = 5
b=6
print(a , b)

#comma based (type 1 formatting)
name = input("enter name: ")
age = int(input("enter age: "))
height = float(input("enter height: "))
print("Name :", name , "Age:" , age , "height:" , height)


#product of two numbers
a = int(input("enter first number:"))
b = int(input("enter secong number:"))
print("The product of given numbers is :" , a*b)


#type2 - modulo based formatting
name = input("enter name: ")
age = int(input("enter age: "))
height = float(input("enter height: "))
print("Name : %s  Age = %d  height : %.f"%(name , age , height)) # %s - str , %d - int , %.nf - float "n=1 it round off ,n=2 decimal upto 2" 


#type 3 - format method in string class
#hello {username} , welcome!
name = input("enter the name : ")
s = 'Hello {} , Welcome!!!'
print(s.format(name))



name = input("enter name: ")
age = int(input("enter age: "))
height = float(input("enter height: "))
f = 'Name : {} , Age : {} , Height : {:.2f} ' #comma based output and if you want to put restriction for decimal then palce it like {:.2f} at the float type
print(f.format(name , age , height))
f = 'Name : {}  Age : {}  Height : {} '#space based output
print(f.format(name , age , height))


#formatted string literals (f-strings)
name = input("enter name: ")
age = int(input("enter age: "))
height = float(input("enter height: "))
print(f"Name : {name} , Age: {age} , height : {height:.2f}" ) #f-strings


#if we want to print curly braces in output then you need to use "doubling"-{{ }}
name = "Alice"
age = 25
height = 5.678
print(f"Name : {name} , Age: {age} , Height : {height:.2f} {{static-text}}")

#o/p - Name : Alice , Age: 25 , Height : 5.68 {static-text}
#If you change "static-text" to something else, say "Hello123", or even symbols like "Age=25", it will print exactly that inside {}:
print(f"Height : {height:.2f} {{Age=25, Unit=cm}}")
#Height : 5.68 {Age=25, Unit=cm}


name = "Alice"
age = 25
print(f"{{Name={name}, Age={age}}}")#o/p-{Name=Alice, Age=25}

#write a program to know how years , months , weeks left to get to age 90
#1 year = 365 days
#1 year = 52 weeks
#1 year = 12 months
curr_age = int(input("enter the age: "))
left = 90 - curr_age
months_left = left * 12
weeks_left = left * 52
days_left = left * 365
print(f"he has {months_left} months {weeks_left} weeks and {days_left} days")




