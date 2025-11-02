"""#seating Arrangement
# Define the number of rows and columns
num_rows = 26  # A to Z
num_cols = 10 # 1 to 10

# Outer loop for rows (A to Z)
for row_num in range(num_rows):
    # Determine the row letter
    row_letter = chr(ord('A') + row_num) #chr() convert ASCII into character & ord() does vice versa

    # Inner loop for columns (1 to 10)
    for col_num in range(1, num_cols + 1): #cols_num starts from 1

        # Print the seat arrangement format
        seat_number = f"{row_letter}{col_num}"
        print(seat_number, end=" ")

    # Move to the next line after each row
    print()
#1. Sum of Digits Until Single Digit
#Write a program to repeatedly add the digits of a number until the result is a single digit.
#Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2.
number = int(input("Enter a number: "))

while number >= 10:  # Continue looping until the number is a single digit
    sum_of_digits = 0
    temp_number = number  # Create a temporary variable to work with

    while temp_number > 0:
        digit = temp_number % 10  # Extract the last digit
        sum_of_digits += digit  # Add the digit to the sum
        temp_number //= 10  # Remove the last digit

    number = sum_of_digits  # Update the number with the sum of its digits

print("The single-digit sum is:", number)

#10.Find Second Largest Element

# Find the second largest number in a list using loops (no sorting).
numbers = [10, 5, 8, 20, 15]  # Example list
if len(numbers) < 2:
    print("List must have at least two elements")
else:
    largest = numbers[0]
    second_largest = numbers[1]

    if second_largest > largest:
        largest, second_largest = second_largest, largest

    for number in numbers[2:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    print("Second largest:", second_largest)


#11. Longest Word in a Sentence
#Given a sentence, find the longest word using loops (not max).
# 11. Longest Word in a Sentence
sentence = "This is a test sentence with some long words"
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
#12. Count Each Word’s Frequency
#Input: "this is is a test" → Output: {'this':1, 'is':2, 'a':1, 'test':1}.
# 12. Count Each Word's Frequency
sentence = "this is is a test"
words = sentence.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word counts:", word_counts)
#13. Remove Duplicates from a String
#Input: "programming" → Output: "progamin".
# 13. Remove Duplicates from a String
string = "programming"
unique_chars = ""
for char in string:
    if char not in unique_chars:
        unique_chars += char

print("Without duplicates:", unique_chars)


#Anagram
str1 = input("Enter the str1:").lower()
str2 = input("Enter the str2:").lower()
fre = {}
for i in str1:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1
for i in str2:
    if i in fre:
        fre[i] -= 1
        if fre[i] == 0 :
             fre.pop(i)
    else:
        fre[i] = 1
        
if fre:
    print("not Anagram")
else:
    print("Anagram")

#prime or not
n = int(input("Enter value of n: "))

prime = []
num = 2  

while len(prime) < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)
    num += 1

print(prime)

#or
n = int(input("Enter value of n:"))

for number in range(2,n+1):#2,3....n
    c = 0
    for fact in range(1,number+1):
        if number%fact == 0:
            c += 1
    if c == 2:
        print(number)
"""
#reverse the digits in the string - a1b2c3 to a3b2c1
user_input = input("enter the string:")
digits =[]
for char in user_input:# a,1,b,2,c,3
    if char.isdigit():
        digits.append(char)
digits = digits[::-1]# ['1','2','3'] to ['3','2','1']
res = " "
for char in user_input:# a,1,b,2,c,3 and ['3','2','1']
    if char.isdigit():
        res += digits[0]
        digits.pop(0)
    else:
        res += char
print("result:",res)
        
    
