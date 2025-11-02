# taking the input
a = input("enter your input:")# by default it takes value as string
b = a*2
print(b)
print(type(a))

#by default it covert float
var_1=123
var_2=45.8
print(var_1+var_2) #if we add str and numeric it shows type error

#by adding prefix 0x,0b,0x
var1=0x10
print(var1)#it converts the 123 to binary-(0B,0b) , hexa-(0x,0X), octa-(0o,0O)


#type of variable
var_1=123
var_2=45.8
var3="sri"
var4=(1,"sri")
var5=[1,"s"]
var={1,2,3}
var6={'name':'sreya'}
var7=True
print(type(var_1))
print(type(var_2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var))
print(type(var6))
print(type(var7))

#type conversion
'''int()
float()
str()
bool()
tuple()
list()
set()
dict()'''
a = int(input("enter your input:"))
b = a*2
print(b)
print(type(a))


floatnum = float(input("enter float:"))
print(type(floatnum))


length = len("sreya gracy")
#print("your name has " + length + "characters")# it shows type error lenght(int) concatenate with str is not possible instead
print("your name has " + str(length) + " characters")#type conversion
print(type(length))

#squareroot
num = int(input("enter a number:"))
sqrt_root = num ** 0.5
print(sqrt_root)


#product odf two number is equal to their sum
a = int(input('enter a number1:'))
b = int(input('enter a number2:'))
print(a*b)
print(a+b)
print((a*b)== (a+b))


#sum of two numbers
first_number = int(input())
second_number = int(input())
sum = first_number + second_number
print(sum)

#or
number = input("enter a two digit number:")
first_number = number[0]
second_number = number[1]
print(int(first_number) + int(second_number))

#swapping
a , b = 5,7
print(a , b)
a , b = b , a
print(a , b)


#or
a=input("enter the value1:")
b=input("enter the value2:")
temp=a
a=b
b=temp
print("a=" +a)
print("b=" +b)

#delete variable
a , b = 5,7
print(a , b)
a , b = b , a
print(a , b)
del a
#print(a)
print(b)

#lenght of str
name=input("enter your name:")
lenght=len(name)
print(lenght)

# calculate BMI = weight/(height*height)
weight = int(input("enter the weight:"))
height = float(input("enter the height:"))
bmi = weight /( height * height)
print(int(bmi))


#program on area of circle
r = float(input())
pi = 3.14
area = pi*r*r
print(f"{area:.2f}")

# to know current age
birth_year = int(input())
current_year = int(input())
age = current_year - birth_year
print(age)
