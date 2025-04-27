# #Let's print a square using for loop:
# for i in range(5):
#     for j in range(5):
#         print("*", end=' ') 
#     print() 

# #A triangle: Using for loop:
# for i in range(5):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print() 

# #A triangle: Upside down:
# for i in range(5):
#     for j in range(i, 5):
#         print("*", end=' ') 
#     print() 

# #Meter to kilometer: 
# def meter_to_kilometer(meter):
#     kilometer = meter / 1000 
#     return meter / 1000 
# meter = 2020 
# result = meter_to_kilometer(meter)
# print(f"{meter} meters = {result} kilometers.") 

# #Kilometers to meters:
# def kilometers_to_meters(kilometers):
#     meters = kilometers * 1000 
#     return kilometers * 1000 
# kilometers = 5 
# result = kilometers_to_meters(kilometers) 
# print(f"{kilometers} kilometers is {result} meters.")

# for i in range(5):
#     for j in range(5):
#         print("*", end=' ') 
#     print()
    
# #kilometers to miles:
# def kilometers_to_miles(kilometers):
#     miles = kilometers * 0.621371 
#     return kilometers * 0.621371 
# kilometers = 5 
# result = kilometers_to_miles(kilometers) 
# print(f"{kilometers} kilometers is {round(result)} miles.")   

# #Converting kg to grams:
# def kg_to_grams(kg):
#     grams = kg * 1000 #since 1000 grams = 1kg
#     return kg * 1000 
# kg = 20 
# result = kg_to_grams(kg) 
# print(f"{kg} kg = {result} grams.") 

# # File truncating and writing:
# from sys import argv 
# script, fine_name = argv 
# target_file = open(fine_name, 'w')
# print(f"Hit enter if you want to truncate:\nOR hit ctrl-c to quit.") 
# input("> ")
# target_file.truncate() 
# print("I am going to ask you for three lines.") 
# line1 = input("Line 1: ") 
# line2 = input("Line 2: ") 
# line3 = input("Line 3: ") 
# target_file.write(f"{line1}\n{line2}\n{line3}\n")
# target_file.close()

# #Math Eligibility:
# print("What is 2^4?: ") 
# n = input("What is 2 to the power of 4? ")
# if int(n) == 16: 
#     print("You know math.") 
# else:
#     print("You don't know math.") 

# #Kilometers to miles: 
# def kilometers_to_miles(kilometers):
#     miles = kilometers * 0.621371
#     return kilometers * 0.621371 
# kilometers = int(input("How many kilometers?: \n>> ")) 
# result = kilometers_to_miles(kilometers) 
# print(f"{kilometers} kilometers = {round(result)} miles.") 

# #miles_to_kilometers:
# def miles_to_kilometers(miles):
#     kilometers = miles * 1.6 
#     return miles * 1.6 
# miles = int(input("How many miles do you want to convert into kilometers? \n >>"))
# result = miles_to_kilometers(miles) 
# print(f"{miles} miles = around {round(result)} kilometers.") 

# # Tell me a math: 
# def addition(a, b):
#     sum = a + b 
#     return a + b
# a = 75
# b = 50
# result = addition(a, b) 
# print(f"{a} + {b} = {result}.")

# fruits = ['apple', 'cherry', 'apricot', 'pineapple'] 
# for fruit in fruits:
#     print(fruit)

# #Looping through a list:
# for letter in 'pineapple':
#     print(letter, end='  ') 

# print('\n')

# #use of else in for-loop:
# y = range(1, 6)

# for numbers in y:
#     print(numbers)
# else:
#     print("The loop is done.") 

# ##Print all even and odd integers from a list and what would be the sum of even and \
# # odd numbers seperately 
# list = [1, 2, 0, 3, 4, 5, 81, 0, 19, 20, 88, 100, 87, 9]

# even_count = 0 
# odd_count = 0 

# even_sum = 0 
# odd_sum = 0

# for i in list:
#     if i == 0:
#         even_count == 0 
#     elif i % 2 == 0:
#         even_count += 1 
#         even_sum += i 

#     else:
#         odd_count += 1
#         odd_sum += i  
# print(f"There are {even_count} even numbers in the list.") 
# print(f"There are {odd_count} odd numbers in the list.") 

# # Sum of even and odd numbers:
# print(f"The sum of even integers is {even_sum}.")
# print(f"The sum of odd integers is {odd_sum}.") 

# #Find the sum of the multiples of 3 and 5 from the following list
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# total = 0 
# for i in list:
#     if i % 3 == 0 or i % 5 == 0:
#         total += i 

# print(f"The total sum of the multiples of 3 and 5 is {total}.") 

# # print the first element 1 time, the second element 2 times, and the third element three times of a list:
# list = ["apple", "cherry", "mango"] 

# for i in range(len(list)): # it becomes 0, 1, and 2 
#     for j in range(i + 1):
#         print(list[i]) 

# #printing a increasing triangle pattern:
# print("Increasing Pattern:")
# num = 6
# for i in range(num):
#     for j in range(i + 1):
#         print("*", end=' ') 
#     print()

# #Decreasing pattern of a triangle:
# print("\nPrinting the decreasing pattern: \n") 
# for i in range(num):
#     for j in range(i, num):
#         print("*", end=' ') 
#     print()

# print("\nRight sided Triangle: \n") 
# for i in range(num):
#     for j in range(i, num):
#         print(" ", end=' ') 
#     for j in range(i + 1):
#         print("*", end=' ') 
#     print()

# print("\nRight Sided Triangle: 2 \n")
# for i in range(num):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, num):
#         print("*", end=' ') 
#     print() 

# print("\n Hill Pattern: \n") 
# num += 1
# for i in range(num):
#     for j in range(i, num):
#         print(" ", end=" ") 
#     for j in range(i):
#         print("*", end=' ') 
#     for j in range(i + 1): 
#         print("*", end=' ')
#     print() 

# #practicing for loop tonight: Date: 14/Aug/2024
# fruits = ["Apples", "Bananna", "Cherry"]
# for fruit in fruits:
#     print(fruit) 

# # 2.#####
# for num in range(5):
#     print(num) #It's going to print 0,1,2,3,4 vertically.

# # 3. ######
# word = "Python"
# print("\n")
# for letters in word:
#     print(letters) 

# ##4. #### Nested loop:
# for i in range(3):
#     for j in range(2):
#         print(i, j)

# for i in range(3):
#     for j in range(2):
#         print(i, j)

# for i in range(5):
#     for j in range(5):
#         print("*", end=' ')
#     print()

# ## Can you count how many vowels are there in a word like: "Hello everyone!"
# def count_vowels(string):
#     vowels = "AEIOUaeiou"
#     count = 0 
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count

# # string = "Hello everyone!"
# # result = count_vowels(string) 
# # print("There are {} vowels in the string: 'Hello everyone!'".format(result))

# # ##Output should be 0\n01\n012\n
# # for i in range(4):
# #     for j in range(i):
# #         print(j, end=' ') 
# #     print()
# # ## Write a for loop that prints the numbers from 1-10.
# # for i in range(1, 11):
# #     print(i, end=" ")

# # ## Sum of the first 10 natural numbers:
# # sum = 0
# # for i in range(1, 11):
# #     sum += i
# # print(f"The sum of the first 10 natural numbers is {sum}.")

# # #Write a for loop that prints each character of a string on a new line.
# # words = "I love you!"
# # for word in words:
# #     print(word)

# # #Given a list, write a for loop to print the first 5 elements:
# # list = [5, 10, "Ten", 9, 8, 23, "eight"]
# # for i in range(5):
# #     print(list[i])

# # #Print even numbers from 1-20:
# # for i in range(1, 21):
# #     if i % 2 == 0:
# #         print(i, end=' ')

# # ##Write a for loop to print the multiplication table for a given number n.
# # t = int(input("Which time table would you like to print, 1 through 100?\nJust enter the number here: "))
# # for i in range(1, 11):
# #     print(f"{t} x {i} = {t * i}")

# # #the sum of 1-100 numbers:
# # sum = 0 
# # for i in range(1, 101):
# #     sum += i 
# # print("The sum of 1-100 is {}.".format(sum))

# # #print even and odd numbers seperately:
# # even_num = 0
# # odd_num = 0
# # for i in range(1, 21):
# #     if i % 2 == 0:
# #         even_num += f"{i}, " 
# #     else:
# #         odd_num += f"{i}, " 
# # even_num = even_num.rstrip(", ") 
# # odd_num = odd_num.rstrip(",  ")
# # print(f"These are even numbers: {even_num}")
# # print(f"These are odd numbers: {odd_num}")

# # print((25*4) * 0.8)
# # print(100 * 0.8)
# # print(20/100)

# # Original text in English
# original_text = "Hello, this is a test."

# # Encode the text in UTF-8 (or any other encoding) and decode it using a different encoding
# garbled_text = original_text.encode('utf-8').decode('latin-1')

# print("Original Text:", original_text)
# print("Garbled Text:", garbled_text)


# Original text in English
original_text = "Hello, this is a test."

# Encode the text in UTF-8 and then decode it using UTF-16
# This mismatch should create garbled text
garbled_text = original_text.encode('utf-8').decode('utf-16', errors='ignore')

print("Original Text:", original_text)
print("Garbled Text:", garbled_text)

original_text = "I am a man who walks alone."
#encode the text using UTF-8 and the deode it using UTF-16
#This mismatch should be garbled text
garbled_text = original_text.encode('utf-8').decode('utf-16', errors='ignore')

print("Original_text = {}".format(original_text)) 
print("Garbled_text = {}".format(garbled_text)) 

import base64

# Define the file paths
input_file_path = 'C:\Users\Topu\Documents\Python\lpthw\text.txt'
output_file_path = 'C:\Users\Topu\Documents\Python\lpthw\new_file.txt'

# Read the file
with open(input_file_path, 'rb') as file:
    file_data = file.read()

# Encode the file data
encoded_data = base64.b64encode(file_data)

# Write the encoded data to a new file
with open(output_file_path, 'wb') as file:
    file.write(encoded_data)
