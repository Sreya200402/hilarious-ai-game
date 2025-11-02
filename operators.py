#arthematic operators => + , - ,* , / , % , //
a = 9
b = 2
sum_num = a+ b
print(sum_num)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)


#relational operators => < ,  > , ==, != ,<= ,>=
print(56 < 109)
print(45 > 99)
print(109 == 109)
print(56 != 56)
print(56 <= 78)
print(99 >= 99)
print('a' < 'A')



# logical operator => and ,or , not
weight = 60
height = 160
eligible = weight > 50 and height > 160
print(eligible)

weight = 60
height = 160
eligible = weight > 50 or height != 160
print(eligible)


weight = 60
height = 160
eligible = weight != 50 or height > 160
print(eligible) 


#Assigment operator
a = 10
print(a)
a += 5 #a = a+5 =>15
print(a)
a -= 5 #a = a-5=>10 where a=15
print(a)
a *=5 # a = a*5
print(a)
a /= 5 # a = a/5
print(a)

#check whether the number is in between 300 to 500
number =int(input("enter the value:"))
check = number > 300 and number <= 500
print(check)

#membership check operator
lst = [1,2,3,4,5]
print(50 not in lst)
print(50 in lst)

str = 'Python'
print('p' in str) # return false becase python is case sensitive since "Python" contain capital 'P' and we are checking small 'p'

#identity operator - is , is not {it works to identify whether the number is present at certain "address" or not}
a = 50
b = 50# integers are imutable
print(id(a))
print(id(b))
print(a is b)
list_1 = [1,2,3,4,5] #lists are mutable... both list have two address through it has same elements for int its not the same case
list_2 = [1,2,3,4,5]
print(list_1 is list_2)
print(list_1 is not list_2)

#bitwise operators - & (bitwise and),~(bitwise not) , |(bitwise or) ,^(exclusive or) , <<(left shift) , >>(right shift)
a = 5 #0101
b = 3 #0011
print(a&b) #0001 checks at bit level same like logical and truth table and converts to bit to number
print(a|b) #0111 = 7
print(a^b) #0110 if the both are same it returns false  , if it have different inputs then it returns true
print(~5) #(-n-1) 'n is bit position here it is 5'
print(~-5)
print(100 << 1) #move the bits of 100 by 1 positions i.e lift shift 100*2^n , n=1
print(100 << 2)
print(100 << 3)
print(100 >> 1)
print(100 >> 2)
print(100 >> 3) #divides by 2^n 'n is position' n=3











































