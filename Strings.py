#Strings
str_1 = 'python789  #$@%()' #single quotes
print(str_1)
str_2 = "python  6453 ^&%~" # double quotes
print(str_2)
str_3 = '''this
is the python
class '''
print(str_3)#multi line variable should be put in triple quotes


#input
str_input = input() # by default it takes values as str
print(str_input)


#new_str = 'It's python class' # shows the error in such case use double quotes or back slash it act as escape
new_str = 'It\'s python class'
print(new_str)

new_str = "It's python class"
print(new_str)

str = "hello\nWorld!!!!!" #\n
print(str)

str1 = "hello\tworld" #\t
print(str1)

# \ is used for the line continuous  
para = 'this is codegnan . it is located at '\
'hyderabad.it provides various courses.for example '\
'python full stack........'
print(para)


#f-strings # for formatting mutiple datatypes if we use '+' -concat it shows error as int cannoy concat with str 
# f with curly braces {} make's it work easier instead use "," 
name = input("enter the name:")
age = int(input("enter the age:"))
height = float(input("enter the height:"))
print("my name is",name,"I'am",age,"and my height is",height)
print(f"my name is {name} , I'am {age} , and my height is {height}")


# to know how months(12), days(365) and week(52) left to reach age 90

age = int(input("enter the age :"))
years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"months lefts {months_left} , weeks left {weeks_left} , days left {days_left}") 

