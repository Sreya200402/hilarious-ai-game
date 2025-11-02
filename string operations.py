#string operations

#string concatenation => +
str_1 = 'python'
Str_2 = "class" # str are immutable if we want to concat we need a new object
new_str = str_1 + Str_2 #if you need space it should be str_1 + " " + str_2
print(new_str)


#string repetition
str_ = 'python'
print(str_*3)

#string indexing
example = 'python' # strings palce value starts with 0,1,2,3,4....n the last palce value n-1 from left to right (zero based indexing)
print(example[3])
print(example[-4]) # string have negative indexing starts with -1 to -n from right to left


#string slicing - obtaining the part of string - variable[start:stop+1:step]
example = 'python'
print(example[2:5]) # the slicing will stop before the index number ie [2:5] slicing starts from 2 and ends at 4 but we represent it as 5 
print(example[::2])


#mask credit card number using slicing
credit_num = input("enter 16 digit number :")
print(credit_num[:12] + "****")

#or
card = input("enter the number:")
masked = card[:12] + "****"
print(masked)

#negative slicing
str_1 = 'Python'
print(str_1[::-1])
print(str_1[::-2])

#to check  any substring using membership operator
print('py' in 'pycharm')


#built-in fuctions in string
# lenght - len()
str = " hii , i love india "
print(len(str))


#to find ascii value
#chr() - will give alphabet for corresponded ascii value
#ord() - will give ascii value for corresponding alphabet
print(chr(99))
print(ord('c'))


#min() & max() => by using ascii value it compare and provide the output small alphabets have higher ascii value (97 to 122) and for capital alphabets (65 to 90)
print(max('Python'))
print(min('Python'))


#sorted() - though we give a str it give output interms of list
print(sorted('sreya'))


#a program on first half string is equal to second half string
str = input("python enter a string:")
l = len(str)
first = str[:(l//2)]  
second = str[(l//2)]
print(first)
print(second)
print(first == second)


#a program to check if the middle character is a vowel -odd length string is gauranted
str = input("enter a string:") #sreyagracy
l = len(str)
print(l)
middle = str[l//2]
vowels = "aeiouAEIOU "
print(middle in vowels)





