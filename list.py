#list - mutable , ordered , heterogenous elements
lst = [12,73.2 , 'A' , [1,2] , {6,7} , {'a':1}]
print(lst)

#empty lst
empty_lst = []

#list input
lst = ["1" , "2"]
new_lst = list(map(int,lst))
print(new_lst)

#type conversion in list

lst_input = list(map(int ,input("enter list:").split(",")))
print(lst_input)

#nested list
nested_lst = [[1,2] , [3,4]]
print(nested_lst)


#list operationa
#concatenation - (+)

lst_1 = [1,2,3]
lst_2 = [4,5,6]
new_lst = lst_1+lst_2
print(new_lst)


#repetition - (*)
lst_1 = [1,2,3]
repeated_lst = lst_1 *3
print(repeated_lst)


#indexing and slicing

lst = [1,2,3,4,5,6,7,8,9,10]
print(lst[3])
print(lst[-1])


#slicing - list[start:stop+1:step]
sliced_lst = lst[2:8]
print(sliced_lst)

#builtin functions - len(),min(),max(),sorted(),sum()
print(sum(lst))

#modifying items in list
lst = [1 , 3 ,5 ,7, 8 , 11]
print(lst)
lst[3] = 9
print(lst)

#membership operator
lst1 = [1,2,3,4,5]
print(9 in lst)


#write a program to find avg of number in list
list = list(map(int,input("enter list:").split()))
print(sum(list))
print(len(list))
avg = sum(list)/len(list)
print(avg)


#Write a program to append 7 to the list and print the updated list

numbers = list(map(int, input().split()))
numbers.append(7)
print("Updated List:", numbers)

#Write a program to print the last element of the given list
numbers = list(map(int, input().split()))
print("Last element of the list:", numbers[-1])

#Write a program that takes a list and returns a new list with elements in reverse order
numbers = list(map(int, input().split()))
reversed_list = numbers[::-1]
print("Reversed List:", reversed_list)


# write a program to fetch the even position numbers and check the sum of even position number is equal to odd
lst = list(map(int,input("enter the numbers:").split()))
fetch = lst[0::2] # fetch even position number
print(fetch)
sum_even = sum(fetch)
print(sum_even)
print(sum_even % 2 == 1)












