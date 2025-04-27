# #1. #Create a Python function called greeting that takes two arguments: a person's name (a string) and
# #their age (an integer). The function should return a string that says "Hello, [name]! You are [age] years old.
# def greeting(name, age):
#     return "Hello, {}! You are {} years old.".format(name, age)

# name = 'Alice'
# age = 30
# result = greeting(name, age) 
# print(result) 

# #2. #Question:
# #Write a Python function called is_even that takes an integer as input and returns True if the number is even, 
# #and False if the number is odd.

# def is_even(integer):
#     if integer % 2 == 0:
#         return True
#     else:
#         return False 
    
# num = int(input("Enter a number: "))
# result = is_even(num) 
# print(result)

# # 3. Write a Python function called calculate_sum that takes a list of numbers as input 
# # and returns the sum of all the numbers in the list.
# def calculate_sum(list_num):
#     return sum(list_num) 

# list = [1, 2, 3, 4, 5]
# result = calculate_sum(list) 
# print("The sum of the list is {}.".format(result)) 

# 4. Write a Python function named count_vowels that takes a string as input 
# and returns the number of vowels (a, e, i, o, u) in the string.
# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string: 
#         if char in vowels:
#             count += 1
#     return count
# str1 = count_vowels("Hello Python!") 
# str2 = count_vowels("How are you?") 
# print(f"The first one has {str1} vowels.\nAnd the second one has {str2} vowels.")

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count 

# print(count_vowels("Hello!"))
# print(count_vowels("Hi, everyone!"))

## 6. Reverse a String
# Write a function reverse_string that takes a string as an 
# argument and returns the string in reverse order.
# def reverse_string(str):
#     return str[::-1] 

# result = reverse_string('hello') 
# print(result) 

# Exercise 5: Reverse a Number
# Write a program that takes an integer input from the user 
# and reverses the digits of the number using a while loop.
# Get user input and convert it to an integer
number = int(input("Enter a number: "))  
reverse_number = 0  # Initialize the reversed number to 0

# Make sure to handle negative numbers as well
#if the number is positive it becomes negative and if negative become positive
is_negative = False  # Initially assume the number is not negative

if number < 0:  # Check if the number is negative
    is_negative = True  # If the number is negative, set is_negative to True
    number = -number  # Convert the number to positive for the reversal process
# is_negative = True: This means the original input number was negative.
# is_negative = False: This means the original input number was positive or zero.
# No, True in this context does not mean that is_negative is a negative number. It simply means that 
# the variable is_negative is acting as a flag to indicate that the original number was negative.

# Reverse the digits using a while loop
while number > 0:
    remainder = number % 10  # Get the last digit
    reverse_number = reverse_number * 10 + remainder  # Append it to the reversed number
    number //= 10  # Remove the last digit from the original number. ###So, x //= y is the same as x = x // y.

# Restore the negative sign if necessary
if is_negative:
    reverse_number = -reverse_number

# Output the reversed number
print("Reversed number:", reverse_number)