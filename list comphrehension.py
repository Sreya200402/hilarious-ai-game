#list compherension
'''
It is the way of creating the list for an iterable(list,tuple,dictionary...)
by combining the for loop  functionality and conditional  statements if any
into a single line of code

syntax
[expression for var in iterable conditinal statements]

expression(transformation related expression) - it tells about how elements from existing iterable should be adde to the new list

for var in iterable - To iterate in the iterable

conditional statements - to check for any filtersss before adding new elements to the list

'''

#wap to print 5th multiple of each element in list
lst = [1,2,3,4,5]
n = []
for i in lst: # for var in iterable
    n.append(i*5) #transformation related expression i * 5
print(n)

#or [list comphrehension]
new_lst = [i*5 for i in lst]
print(new_lst)


#wap to print even numbers in lst
lst = [1,2,3,4,5]
even = []
for i in lst: # for var in iterable
    if i % 2 == 0: # conditional statement
        even.append(i) #transformation related expression i 
print(even)

# or[list comphrehension]
even = [i for i in lst if i % 2 == 0]
print(even)


#wap program to retur the prime numbers in alist
num = [45, 2, 78, 11, 17]
prime = [x for x in num if x > 1 and all(x % i != 0 for i in range(2,int(x**0.5)+1))]
print(prime)



#or
n = 50
primes = [x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
print(primes)



#or
num = [45, 2, 78, 11, 17]
prime = []
def is_prime(n):
    if n == 2 :
        return True
    for i in range(2,n): #2 to n-1
        if n % i == 0:
            return False#(composite)
    return True
for i in num:
    
        if is_prime(i):
            prime.append(i)
print(prime)
p_l = [i  for i in num if is_prime(i)]
print(p_l)


#tuple values of list of alpha and nums
#[(a,1), (a,2) (b,1),(b,2)]
num = [1,2]
alpha = 'ab'
pairs = []
for i in num:
    for j in alpha:
        pairs.append((j ,i))
print(pairs)

#or
nums = [1,2]
alphs = 'ab'
pairs = []
for i in alphs:
    for j in nums:
        pairs.append((i ,j))
print(pairs)
pa_lst = [(i,j)for i in alphs for j in nums]
print(pa_lst)
    
    
#consonents and vowels
s = "python"
vowels = 'aeiou'
for i in s:
    if i.lower() in vowels:
        print(f"{i} -> v")
    else:
        print(f"{i} -> c")

#or
s = "python"
vowels = 'aeiou'
ch_lst = []
for i in s:
    if i in vowels:
        ch_lst.append('v')
    else:
        ch_lst.append('c')

print(ch_lst)
lst = ['v' if i in vowels else 'c' for i in s] # if there is else statement we consider to write if statement first and then else statement then after for statement
print(lst)



#[-3, 12, -8, 47, -45] - ['Neg', 'Pos', 'Neg', 'Pos', 'Neg']
lst = [-3, 12, -8, 47, -45]
new = []
for i in lst:
    if i > 0:
        new.append('Pos')
    else:
        new.append('Neg')
print(new)

#[-3, 12, -8, 47, -45] - ['Neg', 'Pos', 'Neg', 'Pos', 'Neg']
n = ['pos' if i > 0 else 'Neg' for i in lst]
print(n)
