#list method -
#[1,2,3].

#adding elements#
lst = [2,4,6,8,10]

#append(ele) - adds ele to the end
lst.append(12)
print(lst)
lst.append(14)
print(lst)

#insert(Pos , ele) - adds at given position
lst.insert(3,100)
print(lst)

#extend(element) - add group of elements at the end
lst.extend([15,16,17])
print(lst)

#removing elements#
#remove(ele) - remove the given element
lst.remove(100)
print(lst)

lst_1 = [1,2,3,1,4]
lst_1.remove(1)
print(lst_1)

#pop(pos) - remove element at given position(index)
lst.pop(3)
print(lst)
lst.pop()#if we didnt mention the index by dafault it takes value as '-1' i.e remove last digit
print(lst)

#clear - removes elements in list
lst.clear()
print(lst)

lst_1.clear()
print(lst)

#index(ele) - returns the index of first occurence
lst = [2,4,1,8,1,8]
print(lst.index(8))

#count(element) - returns total occurence of a given elements
print(lst.count(1))

#sort(),reverse()
lst.sort()
print(lst)
lst.reverse()
print(lst)

#copy
lst_1 = lst.copy()
print(lst_1)


# a fitness app stores the minutes spent exercising each day.
#please find how many seconds a person spent
#exercising and how many hours a person spent exercising
#[12,67,45,80,23,90,30]
min_spent = [12 , 67 , 45 , 80 , 23 , 90 , 30]
res = sum(min_spent)
print(res)
print(max(min_spent)+1)
total_sec = res *60
total_hours = res / 60
print(total_sec)
print(round(total_hours))

#or
week = list(map(int,input().split()))
m_sum = sum(week)
seconds = m_sum *60
hours = m_sum / 60
max_time = max(week)
day = week.index(max_time)+1
print(seconds)
print(hours)
print(day)


#find the differebce between the second largest and second smallest number in given list
num = list(map(int,input().split()))
num.sort()
print(num)
second_largest = num[-2]
second_smallest = num[2]
diff = second_largest - second_smallest
print(diff)


# give a list of first n natural numbers . a number from the sequence is missing .please find the missing number
lst = list(map(int, input("Enter numbers: ").split()))
n = len(lst) + 1 # total numbers should be length + 1
print(n)
natu = n * (n + 1) // 2   # sum of 1..n
print(natu)
res = sum(lst) # sum of given list
print(res)
missing = natu - res
print("Missing number:", missing)


































