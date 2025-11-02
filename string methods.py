#string methods
#case conversion methods
print("Python".lower())
print("python".upper())
print("python".swapcase())
print("python program".title())
print("python program".capitalize())

#stripping
print( ' Python   ')
print('     python   '.strip())#remove unneccesary space
print('   python    '.lstrip())#remove left spacing
print('   python     '.rstrip())#remove right spacing


#validating methods
print('pycharm'.startswith('py'))
print('pycharm'.endswith('m'))
print('pycharm'.islower())
print('pycharm'.isupper())

#check whether the passeord is valid or not min-5 max-8 start-uppercase atleast one special symbol
password = input("enter the password:")
con1 = len(password)<=8 and len(password)>=5 # password in range 5-8
con2 = password[0].isupper()#first letter should capital
con3 = not password.isalnum()# special characters should be there (alnum is used to check  whether the password contain alphabets and numbers) 
con = con1 and con2 and con3
print(con)



#searching methods

#index(),find()

str_1 = 'apple'
print(str_1.index('p')) 
print(str_1.find('p'))
print(str_1.rindex('p')) #right indexes
print(str_1.rfind('p'))

print(str_1.count('p'))


#splitting() and joining()
str_1 = '1,2,3,4'
lst = str_1.split(',')
print(lst)

new_str = "-".join(lst)
print(new_str)

#empty string

empty_str = ''

#remove inbetween whitespaces
text = input()
result = text.replace(" ", "")
print(result)   # thisisawesome

                          


