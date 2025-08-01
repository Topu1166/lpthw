# ################## Reading from a file using argv and input function: ###################
# from sys import argv
# script, file_name = argv 

# current_file = open(file_name) 
# print(current_file.read()) 

# ###### Now Using input() function: #################
# file = input("Enter the name of the file: ") 
# file_name = open(file) 
# print(file_name.read()) 

# ################# Copying a file from another file: #####################
# ###### Using input() function: ############
# from_file = input("Enter the file name that would be copied from: ") 
# to_file = input("Enter the file name that would be copied to: ")

# in_data = open(from_file) 
# in_file = in_data.read() 
# out_data = open(to_file, 'w') 
# out_data.write(in_file) 
# in_data.close() 
# out_data.close() 

# ############ Reading and then writing new lines on a file ############################
# from sys import argv
# script, file_name = argv 

# current_file = open(file_name)
# print("Here is the content that you want to truncate: ") 
# print(current_file.read()) 
# ############
# print('Hit ctrl+c to abord.\nHit enter to continue.') 
# input(':> ') 
# current_file = open(file_name, 'w') 
# current_file.truncate() 
# print("I am going to ask you for three lines:")
# line1 = input("Line1: ")
# line2 = input("Line2: ") 
# line3 = input("Line3: ") 
# current_file.write(f"{line1}\n{line2}\n{line3}") 
# print("The file has been written successfully.") 
# current_file.close() 

# ##################Read from a file using seek(), readline(), and read() methods ###############
# from sys import argv
# script, file_name = argv 

# def print_whole_file(f):
#     print(f.read(), '\n') 

# def rewind(f):
#     f.seek(0) 

# def print_a_line(f):
#     for current_line in range(10):
#         print(current_line, f.readline(), end='') 

# current_file = open(file_name) 
# #Now is the time to call the function:
# print_whole_file(current_file) 
# rewind(current_file)
# print_a_line(current_file) 

# ################ 
# print("Did you understand it?") 
# understand = input("Enter 'Yes' or 'No': ") 
# if understand.title() == "Yes":
#     print("You really understood it.") 
#     print("Congrats!")
# else:
#     print("You didn't understand it.") 

# import random 

# def guess(x):
#     random_number = random.randint(1, x)
    
#     guess = 0 
#     while guess != random_number:
#         guess = int(input("Anticipate a number between 1 to {}: ".format(x)))

#         if guess < random_number:
#             print("Sorry! Guess again. Too low.") 
#         elif guess > random_number:
#             print("Sorry! Guess again. Too high.") 
#     print(f"Yea! Congrats! You have successfully gussed the number {random_number}.")

# guess(10) 

# ################ Use of While loop ##############
# ## While loop = executes some code some conditions remains true
# name = input("Enter you name: ").title() 

# while name == '':
#     print("You didn't enter your name.") 
#     name = input("Enter your name: ").title()  
# print("Your name is {}".format(name)) 

# age = int(input("Enter your age: ")) 

# while age < 1:
#     if age == 0:
#         print("Zero can not be someone's age.") 
#     else:
#         print("Age can't be negative.") 
#     age = int(input("Enter your age: "))
    
# print('You are {} years old.'.format(age)) 

# ########### FOOD ###################
# food = input("Enter a food you like (q to quit): ").title() 

# while not food == 'Q':
#     print("You like {}.".format(food)) 
#     food = input('Enter another food you like (q to quit): ').title()  

# print('Bye!') 

# ######## Numbers from 1 - 10 ##########
# num = int(input("Enter your number (1 - 10): "))

# while num > 10 or num < 1:
#     print("The number {} is not valid.".format(num)) 
#     num = int(input("Enter your number (1 - 10): ")) 

# print(f"Your number is {num}.") 

# foods = []

# food = input("Enter food that you like (q to quit): ").title()

# while food != "Q":
#     foods.append(food)
#     food = input("Enter food that you like (q to quit): ").title()

# if foods:
#     print("So you said you like {}.".format(', '.join(foods))) 

# print("Bye!")

# # ########### Reading a file line by line: ########### 
# print("Read the whole page of a file: ")
# target = input("Enter a file name: ")
# def read_whole_page(f):
#     print(f.read()) 

# def rewind(f):
#     f.seek(0) 

# def print_a_line(line_count, f):
#     print(line_count, f.readline()) 

# current_file = open(target) 
# read_whole_page(current_file)
# rewind(current_file) 

# current_line = 1
# print_a_line(current_line, current_file)
# current_line += 1
# print_a_line(current_line, current_file) 
# current_line += 1 
# print_a_line(current_line, current_file) 

# ##### Guess the number game: ###############

# number = int(input("Enter a number from (1-10): "))

# while number != 5:
#     print("Sorry! The number has not been matched.")
#     if number > 5:
#         print("You are too high.")
#     elif number < 5:
#         print("You are too low.")
#     number = int(input("Enter the number from (1-10): "))
# print("Congrats! You have correctly anticipated the number '{}'.".format(number)) 


# ########## Guess the number game using def() function #####################
# import random 
# def guess(num): 
#     num1 = random.randint(1, num)
#     number = 0
#     while number != num1: 
#         number = int(input("Enter a number: "))
#         if number < num1:
#             print("The number {} is too low.".format(number)) 
#         elif number > num1:
#             print("The number {} is too high.".format(number)) 

#     print("You have successfully gussed the number which is {}.".format(number)) 
# guess(10)

# ################ Guess the number game #####################
# import random 

# def anticipation(last_num):

#     random_number = random.randint(1, last_num)
#     num = 0 

#     while num != random_number:
#         num = int(input("Enter a number: ")) 
#         if num < random_number:
#             print("Sorry! {} is not the number. Go more than {}.".format(num, num)) 
#         elif num > random_number: 
#             print("Sorry! {} is not the number. Go less than {}.".format(num, num)) 
#     print(f"You have successfully guessed the number {num}.") 

# anticipation(10) 

# #Exercise 23: 
# import sys 
# script, input_encoding, error = sys.argv 

# def main(language_file, encoding, errors): 
#     line = language_file.readline() 
#     if line:
#         print_line(line, encoding, errors)
#         return main(language_file, encoding, errors) 
    
# def print_line(line, encoding, errors):
#     next_lang = line.strip() 
#     raw_bytes = next_lang.encode(encoding, errors=errors) 
#     cooked_string = raw_bytes.decode(encoding, errors=errors) 

#     print(raw_bytes, "<===>", cooked_string) 

# languages = open("languages.txt", encoding="utf-8") 

# main(languages, input_encoding, error) 

# ############ Read a file: ###############
# from sys import argv 
# script, input_file = argv 

# target = open(input_file) 
# print(target.read())

# ############# Truncating and writing a file: #############
# from sys import argv 
# script, input_file = argv

# target = open(input_file, 'w')
# print("Hit enter if you want to truncate your file: ")
# target.truncate() 
# print("I am going to ask you for three lines.")

# line1 = input("Line 1: ") 
# line2 = input("Line 2: ") 
# line3 = input("Line 3: ") 
# target.write(f"{line1}\n{line2}\n{line3}\n") 
# target.close() 

# ########### Copying a file and Pasting to another file: ##########
# from sys import argv
# script, from_file, to_file = argv 

# input_file = open(from_file).read() 

# out_data = open(from_file, 'w')
# out_data.truncate() 
# out_file = out_data.write(input_file) 
# print("The file has been copied successfully.")

# my_ranged = range(1, 5)

# a = 0 

# for val in my_ranged:
#     a = a + 1
#     print("Now a is {}.".format(a))
# print(a)

# my_range = range(1, 5)

# a = 0

# for val in my_range:
#     a += val
#     print("Now a is {}.".format(a))
# print(a)

# ### while loop: ########
# n = 1 
# b = 3
# sum = 0
# while n <= b:
#     n += 1
#     sum += n 
# print(n)
# print(f"Sum is {sum}.")

# # Truncation the whole file #############################
# # Taking the input from the user #######################
# from sys import argv 
# script, file_name = argv 

# warning = input(""""
#                 Warning! Truncating the file.
#                 Hit enter to erase the whole file.
#                 Or Hit ctrl-c to abort. :)
#                 """)
# print(warning) 
# input_file = open(file_name, 'w')
# print("The file {} has been truncated successfully.".format(file_name))
# input_file.truncate() 
# input_file.close() 

# # Truncating a file:
# from sys import argv 
# script, file_name = argv 

# target = open(file_name, 'w') 
# target.truncate() 
# target.close() 

# #Writing over a file:
# # Taking input from the user:
# from sys import argv
# script, from_file, to_file = argv 

# print("Copying {} file to {}.".format(from_file, to_file)) 
# print("You are about to copy the file:\nHit enter to continue.\nOr hit ctrl-c to abort.")
# input("> ")
# in_file = open(from_file)
# in_data = in_file.read() 
# out_data = open(to_file, 'w')
# out_data.write(in_data) 
# in_file.close() 
# out_data.close()
# print("The file has been successfully copied.")  

# # Copying a file from one to another:
# # Using the argv input:
# from sys import argv
# from os.path import exists 
# script, from_file, to_file =argv

# print(f"Does the file exist? {exists(to_file)}")
# print("Does the file exist? {}".format(exists(from_file))) # In dot(.) format formation
# in_data = open(from_file) 
# in_file = in_data.read() 
# out_data = open(to_file, 'w')
# out_data.write(in_file) 
# in_data.close() 
# out_data.close() 
# print("The file has been successfully copied to {} from {}.".format(to_file, from_file)) 

# #Truncation files:
# from sys import argv
# script, file_name = argv 

# target = open(file_name, 'w') 
# print("Warning!\nYou are about to truncate the file.\nHit enter to proceed.\nOr Hit ctrl-c to abort.") 
# input("> ")
# target.truncate() 
# target.close() 
# print("The file has been truncated successfully.") 

# #Sum of Two Numbers:
# from sys import argv
# script, num1, num2 = argv 

# convertNum1 = int(num1) 
# convertNum2 = int(num2)
# sum = convertNum1 + convertNum2 
# print("The sum of the two given numbers is {}.".format(sum)) 

# #printing the number which is greater: 
# if convertNum1 == convertNum2: 
#     print(f"Both the numbers are equal. So both the numbers {convertNum1} is greater.") 
# elif convertNum1 > convertNum2: 
#     print(f"The number {convertNum1} is greater than the number {convertNum2}.")
# else:
#     print(f"The number {convertNum2} is greater than the number {convertNum1}.") 
# print("I think it is going to work now.") 

# # Anticipate the number:
# import random 


# def guess(num):
#     random_num = random.randint(1, num)
#     anti_num = 0
#     while anti_num != random_num: 
#         anti_num = int(input("Enter the number: \n"))

#         if anti_num > random_num:
#              print("You are too high! Go down!") 
#         else:
#             print("You are too low! Go up!")
#     print("You have successfully gussed the number. The number was {}.".format(anti_num))
# guess(10)            

# # Guess a number:
# import random 

# def guess(num):
#     random_num = random.randint(1, num)
#     anticipation = 0
#     while anticipation != random_num:
#         anticipation = int(input("Guess the number: ")) 
#         if anticipation > random_num:
#             print("You are too high. Go down!") 
#         else:
#             print("You are too low. Go up!") 
#     print("You have successfully guessed the number.\nThe number was {}.".format(anticipation)) 
# guess(10)

# ### Guess a number:
# import random 
# def guess(num):
#     random_num = random.randint(1, num)
#     anticipation = 0 
#     while anticipation != random_num:
#         anticipation = int(input("Guess the number: ")) 
#         if anticipation > random_num:
#             print("You are too high. Go down!") 
#         else: 
#             print("You are too low. Go up!") 
#     print("You have successfully guessed the number.\nThe number was {}.".format(anticipation)) 

# guess(10)

# # Printing a number which is the greatest among the three numbers: ######################
# num1 = int(input("Enter the first number: ")) 
# num2 = int(input("Enter the second number: ")) 
# num3 = int(input("Enter the third number: ")) 
# if num1 > num2 and num1 > num3:
#     print("The number {} is greater.".format(num1)) 
# elif num2 > num1 and num2 > num3:
#     print("The number {} is greater.".format(num2)) 
# else: 
#     print("The number {} is greater.".format(num3)) 


# # A cake costs 75 taka, chocolate 45 for each(1) piece,
# # I have 900 taka in total without any expence, 
# # cake = 8 piece purchased. How many candy can you buy with the rest of the money?
# # How much money would I have after the expense.

# def account(total_money, cake_price, cake_quantity, candy_price):
#     cake_expense = cake_quantity * cake_price 
#     remaining_money = total_money - cake_expense 
#     candy_number = remaining_money // candy_price 
#     money_left = remaining_money % candy_price 
#     return candy_number, money_left 

# total_money = 900 
# cake_price = 75 
# cake_quantity = 8 
# candy_price = 45 

# candy_number, money_left = account(total_money, cake_price, cake_quantity, candy_price) 
# print("So, I can buy {} candies and {} money left.".format(candy_number, money_left)) 

# #Exercise: 2
# print("I will count my chickens.") 
# print("Hens", (30 + 40) / 5.0)
# print("Roosters", 100 - 25 * 3 % 4)
# print(75 % 4)
# print(100 - 25 * 3 / 4)
# print("Now I will count the eggs: ") 
# print(round(3 + 2 - 3 / 5 * 2))

# from sys import argv 
# script, file_name = argv 

# target = open(file_name, 'w')
# print("Truncating the file: ") 
# print("Hit enter to continue: ") 
# input('> ') 
# target.truncate() 
# target.close() 

# #To convert an image to pdf:
# from PIL import Image 
# #open the image file:
# img = Image.open("cl.jpg") 
# #Convert the image to pdf:
# img.save("topucliff.pdf","PDF")

# ## Constract a pyramid: 
# for i in range(6):
#     for j in range(i + 1):
#         print("*", end=' ')
#     print()

# #Converting an image into pdf:
# from PIL import Image
# in_data = input("Enter the file name to convert into pdf: ") 
# img = Image.open(in_data)
# save_file = input("Name the pdf file: ") 
# img.save(save_file, "PDF")

# i = 0
# while i <= 3:
#     print("Infinite")
#     i -= 1

# #Guessing the number game:
# def guess(x):

#     import random 
#     random_number = random.randint(1, x)
#     guess = 0 

#     while guess != random_number:

#         guess = int(input("Guess the number: ")) 

#         if guess > random_number:
#             print("You are to high. Guess again.") 
#         else:
#             print("You're too low. Guess again.") 

#     print("You have successfully guessed the number {}.".format(guess))

# guess(10)

# # Wishing Happy birthday using def function:
# def birthday(name):
#     print("Happy Birthday {}.".format(name))
# birthday('Roy')

# # Enter your password:

# password = 123456
# x = 0 

# while x != password:
#     x = int(input("Enter your password: "))
    
#     if x != password:
#         print("Incorrect password!") 

# # print("You've successfully logged in.") 
    
# from sys import argv
# script, file_name = argv

# txt = open(file_name) 
# print("{} is the file that you want to read.".format(file_name)) 
# print(txt.read()) 
# ## Another way of taking input:
# text_file = input("Enter the name of the file: ") 
# txt1 = open(text_file) 
# print(txt1.read()) 

# #A simple text editor:
# from sys import argv
# script, file_name = argv 

# #First we truncate the file:
# target = open(file_name, 'w') 
# print("We are going to truncate the file: ")
# print("To abort hit Ctrl-C (^C).") 
# print("To continue hit enter.") 

# input('? ')

# target.truncate() 
# input1 = input("Line 1: ") 
# input2 = input("Line 2: ") 
# input3 = input("Lin3 3: ")

# target.write(f"{input1}\n{input2}\n{input3}\n")
# print("And finally we close the file since we opened it.") 
# target.close() 

# ## A Simple Text Editor:
# from sys import argv
# script, file_name = argv

# target = open(file_name, 'w') 

# input1 = input('Line1: ') 
# input2 = input('Line2: ') 
# input3 = input('Line3: ') 

# input4 = input('Line4: ') 
# input5 = input('Line5: ')

# #write into the file:
# target.write(f"{input1}\n{input2}\n{input3}\n")
# target.write("{}\n{}\n".format(input4, input5)) 
# #And finally we are going to close the file: 
# target.close() 

# #copying a file :
# from sys import argv
# script, from_file, to_file =argv 

# in_file = open(from_file, 'r')
# in_data = in_file.read() 
# in_file.close() # .close() method is a must when a file is opened

# out_data = open(to_file, 'w')
# out_data.write(in_data) 
# out_data.close() # close is necessary 
# print("Your file has been successfully copied.")  

# from sys import argv
# script, from_file, to_file = argv

# # Open the input file, read its contents, and close it automatically
# with open(from_file, 'r') as in_file:
#     in_data = in_file.read()

# # Open the output file, write the contents, and close it automatically
# with open(to_file, 'w') as out_file:
#     out_file.write(in_data)

# # Use of with and as keyword: 
# from sys import argv
# script, from_file, to_file = argv

# #Open the input file, read its contents, and close it automatically
# with open(from_file, 'r') as in_file:
#     in_data = in_file.read() 

# #Open out file, read its contents, and close it automatically
# with open(to_file, 'w') as out_file:
#     out_file.write(in_data) 

# #let's truncate a file:
# file_name = input("File name to truncate: ") 
# #open the file, read its contents, and close it automatically
# with open(file_name, 'w') as target:
#     target.truncate() 
# print("The file has been truncated successfully.") 

# #Encoding a text:
# text = "I love to do it."

# garbled_text = text.encode('utf-8').decode('utf-16', errors='ignore') 
# print(garbled_text)
# print("Original_text = {}".format(text))

# from PIL import Image 
# img_name = input("File name to convert into pdf: ")
# img = Image.open(img_name)
# new_name = input("Name the pdf file use '.pdf' at the end: ")
# img.save(new_name, "PDF")
# print("The file has been converted into pdf successfully.")

# from sys import argv
# script, input_file = argv 

# def print_all(f):
#     print(f.read()) 

# def rewind(f):
#     f.seek(0) 

# def print_a_line(line_count, f):
#     print(line_count, f.readline()) 

# current_file = open(input_file, 'r') 

# print("First let's print the whole file: \n") 

# print_all(current_file) #printing the whole file

# print("Now let's rewind kind of like a tape.") 

# rewind(current_file)

# print("Let's print three lines:") 

# current_line = 1
# print_a_line(current_line, current_file)
# current_line = 2
# print_a_line(current_line, current_file) 
# current_line = 3 
# print_a_line(current_line, current_file) 

# ###Read the whole file using variables:
# input_file = input("Enter the file name to read its content: ") 

# # in_file = open(input_file, 'r') 
# # result = in_file.read()
# # in_file.close()
# with open(input_file, 'r') as in_file: # new style
#     result = in_file.read() 
# print("Here you go read the content of the file {}:".format(input_file)) 
# print(result)

# #now using def function to read a file's content:
# def read_whole_file(f):
#     print(f.read()) 
# # takes the user input: 
# input_file = input("Enter file name to read the whole content:")
# target = open(input_file, 'r') 
# read_whole_file(target)
# target.close() #close the file since it was opened

# # Let's print some lines of a file:
# input_file = input("Enter file name: ") 

# def rewind(f):
#     f.seek(0)

# def print_a_line(line_count, s):
#      print(line_count, s.readline(), end='')

# current_file = open(input_file, 'r') 
# rewind(current_file)

# for line_count in range(1, 11):
#     print_a_line(line_count, current_file)
# current_file.close()
# print("\n")

# # line_count = 1
# # print_a_line(line_count, current_file) 
# # line_count += 1
# # print_a_line(line_count, current_file) 

# # Print a file's text one by one:
# from sys import argv
# script, input_file = argv

# def rewind(f):
#     f.seek(0) 

# def print_a_line(line_count, x):
#     print(line_count, x.readline(), end='') 

# target = open(input_file, 'r') 

# rewind(target) 

# for line_count in range(1, 11):
#     print_a_line(line_count, target)

# target.close()

# original_text = "I want to know you more."

# garbled_text = original_text.encode('utf-8').decode('utf-16', errors='igonre') 

# print(garbled_text) 

# #read a file:
# from sys import argv
# script, input_file = argv

# # with open(input_file, 'r') as target:
# #     result = target.read() 

# # print(result)

# target = open(input_file, 'r')
# print(target.read()) 
# target.close() 

# #Copying a file:
# from_file = input("Enter file name which you want to copy from: ") 
# to_file = input("Enter the file name which you want to copy it to: ")

# in_file = open(from_file, 'r') 
# in_data = in_file.read() 
# in_file.close() 

# out_file = open(to_file, 'w')
# out_file.write(in_data)
# out_file.close() 
# print("The file has been successfully copied to {}.".format(to_file))

# def greeting(name, age):
#     print(f"Hello, {name}! You are {age} years old.")

# greeting('John', 30)

# # Write a function sum_numbers that takes two numbers as arguments and returns their sum.
# def sum_numbers(num1, num2):
#     sum = num1 + num2
#     return sum 
# result = sum_numbers(3, 4)
# print(f"The sum of the two numbers is {result}.")

# # Write a function is_even that takes a number as an argument and returns
# #  True if the number is even, and False if it’s odd.

# from sys import argv
# script, input_num = argv

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# result = is_even(int(input_num)) 

# print(result)
# if result == True:
#     print("The number is True because the number was an even number.") 
# else:
#     print("The number is False because the number was an odd number.")

#  Write a function celsius_to_fahrenheit that converts a 
# temperature from Celsius to Fahrenheit. The formula is F = C * 9/5 + 32.

# from sys import argv
# script, number = argv

# def celsius_to_fahrenheit(celsius):
#     Fahrenheit = celsius * 9 / 5 + 32
#     return Fahrenheit

# result = celsius_to_fahrenheit(int(number))
# print(result)


# Write a function find_maximum that takes three numbers as 
# arguments and returns the largest of the three.
# from sys import argv
# script, first, second, third = argv

# def find_maximum(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     elif c >= a and c >= b:
#         return c

# result = find_maximum(int(first), int(second), int(third))

# print(result)       

# Write a function count_vowels that takes a string as an argument and 
# returns the number of vowels (a, e, i, o, u) in the string.
# from sys import argv
# script, str = argv

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count 
# # text = "I love it doing."
# result = count_vowels(str)

# print(f"There are {result} vowels in the string.")

# 6. Reverse a String
# Write a function reverse_string that takes a string as an 
# argument and returns the string in reverse order.

# def reversed_string(s):
#     return s[::-1] 
    

# result = reversed_string('hello') 
# print(result) 

# #Slicing a string:
# def reversed_string(s):
#     return s[::-1]
# string = "Hellow world!"
# result = reversed_string(string) 
# print(result)

# #Slicing a String:
# def reversed_string(s):
#     return s[::-1] 

# result = reversed_string('hello world!') 
# print(result) 


# Write a Python function named count_vowels that takes a string as input 
# and returns the number of vowels (a, e, i, o, u) in the string.
# def count_vowels(s):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count 

# string = input("Write something to see how many vowels there are: ") 
# # string = "helo"
# result = count_vowels(string) 
# print(f"There are {result} vowels in your sentence.") 
# from sys import argv
# script, input = argv 

# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count 

# result = count_vowels(input) 
# print("There are {} vowels in your sentence.".format(result)) 

# # 3. Write a Python function called calculate_sum that takes a list of numbers as input 
# # and returns the sum of all the numbers in the list.

# def calculate_sum(list):
#     return sum(list) 
    

# list_num = [1, 2, 3, 4, 5, 6]
# result = calculate_sum(list_num) 
# print("The sum of the numbers from the list is {}.".format(result))

#  #Write a Python function called is_even that takes an integer as input and returns True if the number is even, 
# # #and False if the number is odd.
# from sys import argv
# script, input = argv 

# def is_even(integer):
#     if integer % 2 == 0:
#         return  True
#     else:
#         return False
    
# result = is_even(int(input)) 
# print(result)

# #1. #Create a Python function called greeting that takes two arguments: a person's name (a string) and
# #their age (an integer). The function should return a string that says "Hello, [name]! You are [age] years old.

# def greeting(name, age):
#     string = f"Hello, {name}! You are {age} years old."
#     return string
# result = greeting('John', 12)
# print(result) 

# #Encoding a text:
# original_text = "This is my home."

# garbled_text = original_text.encode('utf-8').decode('utf-16', errors='ignore') 
# print(f"Garbled_text = {garbled_text}")

# ##Use of 'open' and 'as' instead of using variables:
# #Open a file like: cat/type command:
# from sys import argv
# script, input_file = argv

# with open(input_file, 'r') as target:
#     print(target.read()) #special thing is you don't need to close() it while using with and as

# #now opening the same file using variables:
# targeted_file = open(input_file, 'r') 
# print(targeted_file.read()) 
# targeted_file.close() 

# #Use of 'with' and 'as' instead of using variables:
# #Copy a file from a file:
# from sys import argv 
# script, from_file, to_file= argv

# with open(from_file, 'r') as in_file:
#     out_data = in_file.read()

# with open(to_file, 'w') as out_file:
#     out_file.write(out_data) #.close() method is not necessary here. 
# print("The file has been successfully copied.")

# # in_file = open(from_file, 'r') 
# # in_data = in_file.read() 
# # in_file.close()

# # out_file = open(to_file, 'w')
# # out_data = out_file.write(in_data) 
# # out_file.close() 

# print("The file has been successfully copied.")

# # Exercise 2: Sum of Two Numbers
# # Write a function that takes two numbers as input and returns their sum.

# def sum_two(a, b):
#     return a + b

# a = input("Enter the first number: ")
# b = input("Enter the second number: ") 

# result = sum_two(int(a), int(b)) 
# print(f"The sum of the two numbers is {result}.") 

# def sum_two(a, b):
#     return a + b

# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
    
#     result = sum_two(a, b)
#     print(f"The sum of the two numbers is {result}.")
    
# except ValueError:
#     print("Please enter valid numbers.")

# ##Use of try and except ValueError:
# def sum_of_two(a, b):
#     return a + b

# try:
#     a = int(input("Enter a number:")) 
#     b = int(input("Enter another number:"))

#     result = sum_of_two(a, b) 
#     print(f"The sum of the two numbers is {result}.")

# except ValueError:
#     print("Please enter valid numbers.")

# # Exercise 2: Sum of Two Numbers
# # Write a function that takes two numbers as input and returns their sum.

# def sum_of_two(a, b):
#     return a + b

# try:
#     a = int(input("Enter the first number: ")) 
#     b = int(input("Enter the second number: "))

#     result = sum_of_two(a, b) 

#     print("The sum of the two numbers is {}.".format(result)) 

# except ValueError:
#     print("Enter valid integers.")

# Exercise 3: Find Maximum Number
# Create a function that takes three numbers and returns the largest one.

# def maximum_number(a, b, c):
#     if a >= b and a >= c:
#         return f"{a} is the largets."
#     elif b >= a and b >= c:
#         return f"{b} is the largest."
#     else:
#         return f"{c} is the largest." 

# #User input:
# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     num3 = int(input("Enter the second number:")) 

#     # assign the function as being called to a varible :
#     result = maximum_number(num1, num2, num3) 

#     print(result) 

# except ValueError:
#     print("You didn't enter a valid number.") 

# Exercise 4: Factorial Function
# Write a function that takes a number and returns its factorial.

# def factorial(n):
#     result = 1
#     for num in range(1, n + 1):
#         result *= num 
    
#     return result 
# try:
#     a = int(input("Write a number for its factorial: ")) 
#     print(f"The factorial of {a} is {factorial(a)}.") 

# except ValueError:
#     print("You didn't enter any valid number.") 

# finally:
#     print("Execution completed!")

# #Recursive Factorial using def function:
# def recursive_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * recursive_factorial(n - 1)

# print(recursive_factorial(5))

# #Fabonicci Function:
# def fibonocci(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibonocci(n - 1) + fibonocci(n - 2) 
# print(fibonocci(5))

# from PIL import Image

# in_data = input("Enter the file name that you want to convert into pdf: ")
# img = Image.open(in_data) 
# file_name = input("Rename your file and use '.pdf' after the name: ") 
# img.save(file_name, 'PDF') 

# print("The file has been successfully converted into {}.".format(file_name)) 

# from PIL import Image
# input_file = input("Enter the name of the file: ")
# img  = Image.open(input_file, 'r') 
# save_file = input("Rename the file and use '.pdf' after the name:" )
# img.save("save_file", 'PDF') 
# print("Your file has been converted successfully into {}.".format(save_file))


# #  Create a for loop that countss the numbers of even and odd
# # integers in the list below. It should return two strings on
# # seperate lines that prints sentences. And what would
# # be the sum of even and odd integers write them seperately.
# def even_odd(list):
#     even_count = 0
#     odd_count = 0 
#     even_sum = 0 
#     odd_sum = 0
#     for char in list:
#         if char % 2 == 0: # Counts if the numbers are even
#             even_count += 1
#             even_sum += char
#         else: #Otherwise, the numbers are odd
#             odd_count += 1
#             odd_sum += char
#     return even_count, odd_count, even_sum, odd_sum

# list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_count, odd_count, even_sum, odd_sum = even_odd(list_numbers)

# print(f"There are {even_count} even numbers and the sum of them is {even_sum}.")

# # 2. Print trinangles and squares/retangles using loops. 

# # Printing a triangle:
# for i in range(7):
#     for j in range(i, 7):
#         print(" ", end=' ') 

#     for j in range(i + 1):
#         print("*", end=' ') 
    
#     for j in range(i):
#         print("*", end=' ') 
#     print()
# #making the hill into a diamond:
# for i in range(7):
#     for j in range(i + 2):
#         print(" ", end=' ')
#     for j in range(i, 5):
#         print("*", end=' ')
#     for j in range(i, 6):
#         print("*", end=' ')
#     print()

#     # 3. Write 4 seperate for loops that prints every elements
# # from the following 4 lists: (i) list = ['apple', 'cherry',..]
# # (ii) numbers = [1, 2, 3, 4, 5] (iii) city_Name = ['Dhaka',
# # 'Gazipur', 'Melbourne',....] (iv) people = ['Rony', 'David',
# # 'Joy', 'Jody']
# list = ['apple', 'cherry', 'mango', 'blueberry', 'lichi']
# for i in list:
#     print(i, end=', ' + '\n')

# num = [1, 2, 3, 4, 5, 6]
# for numbers in num:
#     print(numbers)

# # 4.  Write a for loop that prints the integers from the 
# # following/a list, but only if they are even.
# list = [1, 2, 3, 4, 5, 18, 20, 30, 19, 17, 59]

# #choose onlyl the even numbers:
# list = [1, 2, 3, 4, 5, 6]
# even_num = []
# for num in list:
#     if num % 2 == 0:
#         even_num.append(num) 

# print(even_num)

# #Infinite loops: ########################## Infinite loops: #####################
# # while True:
# #     print("I live it.")

# # i = 0
# # while i <= 3:
# #     print("hold on!") 

# # i = 0 
# # while i <= 3:
# #     print("hello!") 
# #     i -= 1
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = []
# for i in n:
#     if i % 2 == 0:
#         numbers.append(i) 
#     elif i == 5:
#         break
# print(numbers) 

# #Write a while loop that prints 1 to 10 numbers:
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # Exercise 2: Sum of Natural Numbers
# # Write a program to calculate the sum of the first n natural numbers using a while loop./
# #  The value of n should be provided by the user.
# number = int(input("Enter a number: ")) 
# i = 0
# sum = 0
# while i <= number:
#     sum += i
#     i += 1

# print("The sum of the numbers is {}.".format(sum))

# # Exercise 3: Guess the Number
# # Write a program where the user has to guess a secret number between 1 and 10.?
# #  The program should keep asking for guesses until the correct number is guessed.
# import random 
# secret_number = random.randint(1, 10) 
# guess_num = 0
# while guess_num != secret_number:
#     guess_num = int(input("Guess the number: ")) 
#     if guess_num  > secret_number:
#         print("Guess again! You are too high.") 
#     elif guess_num < secret_number:
#         print("Guess again! You are too low.") 

# print("You have successfully anticipated the number.\nThe number was {}.".format(guess_num)) 

# #A small editor:
# from sys import argv 
# script, input_file = argv

# #Writing over a file:
# #Print the whole file first
# def whole_file(f):
#     print(f.read()) 

# def rewind(f):
#     f.seek(0) #read/write the location to the begining of the file

# def print_a_line(current_line, current_file):
#     print(current_line, current_file.readline(), end=' ') 

# print("Let's print the whole file first.") 

# target = open(input_file, 'r')

# whole_file(target) 

# #read/write the location to the begining of the file
# rewind(target) 

# #now let's read the line one by one:

# for i in range(1, 5):
#     print_a_line(i, target)

# # Exercise 5: Reverse a Number
# # Write a program that takes an integer input from the user 
# # and reverses the digits of the number using a while loop.
# # Get user input and convert it to an integer
# number = int(input("Enter a number: "))  
# reverse_number = 0  # Initialize the reversed number to 0

# # Make sure to handle negative numbers as well
# #if the number is positive it becomes negative and if negative become positive
# is_negative = False  # Initially assume the number is not negative

# if number < 0:  # Check if the number is negative
#     is_negative = True  # If the number is negative, set is_negative to True
#     number = -number  # Convert the number to positive for the reversal process
# # is_negative = True: This means the original input number was negative.
# # is_negative = False: This means the original input number was positive or zero.
# # No, True in this context does not mean that is_negative is a negative number. It simply means that 
# # the variable is_negative is acting as a flag to indicate that the original number was negative.

# # Reverse the digits using a while loop
# while number > 0:
#     remainder = number % 10  # Get the last digit
#     reverse_number = reverse_number * 10 + remainder  # Append it to the reversed number
#     number //= 10  # Remove the last digit from the original number. ###So, x //= y is the same as x = x // y.

# # Restore the negative sign if necessary
# if is_negative:
#     reverse_number = -reverse_number

# # Output the reversed number
# print("Reversed number:", reverse_number)

# # Exercise 5: Reverse a Number
# # Write a program that takes an integer input from the user 
# # and reverses the digits of the number using a while loop.

# number = int(input("Enter a number to reverse it: "))
# reverse_number = 0 

# is_negative = False 

# if number < 0:
#     is_negative = True
#     number = -number

# while number > 0:
#     remainder = number % 10 
#     reverse_number = reverse_number * 10 + remainder 
#     number //= 10 

# if is_negative:
#     reverse_number = -reverse_number 

# # print("The reversed number of {} is {}.".format(number, reversed_number)) 
# print("Reversed_number: {}".format(reverse_number))


# number = int(input("Enter a number: ")) 
# reversed_number = 0

# is_negative = False

# if number < 0:
#     is_negative = True
#     number = - number 

# while number > 0:
#     remainder = number % 10 #Remains the last number every time
#     reversed_number = reversed_number * 10 + remainder #Append the number one by one
#     number //= 10 #Removes the last number from the original number

# if is_negative:
#     reversed_number = - reversed_number

# print(f"Reversed number: {reversed_number}")

# Factorial of a number:
# number = int(input("Enter a number to know its factor: ")) 

# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i

# print(factorial) 

# #Recursive Approach: A function calls itself
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))

# #Factorial of n number using for loop:
# n = int(input("Enter a number: ")) 
# result = 1
# for i in range(1, n + 1):
#     result *= i #the variable holds the current value on each iteration

# print(result)

# #Pass:
# for i in range(5):
#     if i == 3:
#         pass
#     print(i)

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100 
#     return jelly_beans, jars, crates 

# start_point = 10000 
# beans, jars, crates = secret_formula(start_point) 
# #using f"" string
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# start_point = start_point / 10

# result = secret_formula(start_point) 

# print("We'd have {} beans, {} jars, and {} crates.".format(*result))

# A man has 900 Taka. He wants to purchase 3 ice-creams each costs 55 Taka.
# A chocolate costs 18 Taka. How many chocolates can he buy with the rest of the money?
# And how much money would be left?

# def choco_money_left(total_money, ice_cream_quantity, ice_cream_cost,  each_choco):
#     total_ice_cream_cost = ice_cream_quantity * ice_cream_cost
#     remaining_money = total_money - total_ice_cream_cost
#     purchased_choco_quantity = remaining_money // each_choco 
#     money_left = remaining_money % each_choco 
#     return purchased_choco_quantity, money_left 

# total_money = 900 
# ice_cream_quantity = 3
# ice_cream_cost = 55
# each_choco = 18 

# result = choco_money_left(total_money, ice_cream_quantity, ice_cream_cost, each_choco) 

# print("He can buy {} chocolates with the rest of the money. And {} bucks will be left.".format(*result)) 

# #Factorial of a number: Using both for loop and recursive approach:
# #Using for loop:
# n = int(input("Enter a number: "))
# result = 1
# for i in range(1, n + 1):
#     result *= i 
# print(result)

# #Recursive Approach:
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5)) 

# . Create a for loop that countss the numbers of even and odd
# integers in the list below. It should return two strings on
# seperate lines that prints sentences. And what would
# be the sum of even and odd integers write them seperately.


# def eve_odd(list):
#     even_count = 0
#     odd_count = 0 
#     even_sum = 0
#     odd_sum = 0
#     for i in list:
#         if i % 2 == 0:
#             even_count += 1
#             even_sum += i 
#         else:
#             odd_count += 1
#             odd_sum += i  
#     return even_count, even_sum, odd_count, odd_sum 


# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = eve_odd(num_list) 
# print("There are {} even numbers and the sum of them is {}.\nAlso, there are {} odd numbers and\
#  the sum of them is {}.".format(*result))

# #Factorial of a number:
# # Using for loop:
# factorial = 1
# for i in range(1, 6):
#     factorial = factorial * i 

# print(factorial) 

# #Recursing approach:

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5)) 

# #Reverse a number using while loop:
# #Take an user input
# number = int(input("Enter a number: ")) 
# reversed_number = 0 

# #if the number was a negative number:
# is_negative = False

# if number < 0:
#     is_negative = True 
#     number = -number #making the number positive

# while number > 0:
#     remainder = number % 10 
#     reversed_number = reversed_number * 10 + remainder 
#     number //= 10 

# if is_negative:
#     reversed_number = -reversed_number 

# print(reversed_number)

# #Reversing a String:
# def reverse_str(s):
#     return s [::-1] 

# print(reverse_str("hello! how are you?"))


# #Reverse a number:
# def reverse_number(num):
#     return int(str(num) [::-1]) 

# result = reverse_number(123) 
# print(result) 

# #Exercise 34:

# def start():
#     print("You are in a dark room.") 
#     print("It has two doors to your left and right.")
#     print("Which one do you choose?")

#     choise = input("> ") 
    
#     if choise == "left":
#         bear_room() 
#     elif choise == 'right':
#         Cthulhu_room() 
#     else:
#         dead("You stumble around the room until you starve.")

# def dead(why):
#     print(why, "Good job!")  

# def bear_room():
#     print("There is a bear in here.")
#     print("The bear has a bunch of honey.")
#     print("There is a fat bear infront of another door.") 
#     print("How are you gonna move the bear?:") 

#     bear_moved = False
#     choice = input("> ") 

#     while True:
#         if choice == "take honey":
#             dead("The bear looks at you and then slap your face off.")
#         elif choice == "taunt bear" and not bear_moved:
#             print("The bear has moved from the door.")
#             print("You can go through it now.")
#             bear_moved = True
#         elif choice == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your legs off.")
#         elif choice == "door open" and bear_moved:
#             gold_room() 
#         else:
#             print("I got no idea what that means.") 

# def gold_room():
#     print("This room is full of gold. How much do you take?")

#     choice = input("> ") 

#     if 0 in choice or 1 in choice:
#         how_much = int(choice) 
        

# #The sum of natural numbers using RECURSION:
# def recursion(number):
#     if number == 1:
#       return 1
#     else:
#         return number + recursion(number - 1) 

# num = int(input("Enter a number: ")) # taking the input from user

# result = recursion(num) #passing the argument 
# print("The sum of the natural number from 1 to {} is {}.".format(num, result)) 

# #The factorial of 5 in recursion:
# def factorial(n):
#    if n == 1:
#       return 1
#    else:
#       return n * factorial(n - 1) 

# number = int(input("Enter a number: "))
# print("The factorial of 5 is {}.".format(factorial(number)))

# #Reverse a string:
# def reverse_str(str):
#    return str[::-1]

# string = "Hi!" 
# print(reverse_str(string)) 

# #Reverse a number:
# def reverse_num(num):
#    return int(str(num)[::-1])

# number = 123
# print(reverse_num(number))
# print(type(reverse_num(number)))

# print("Printing the data type: ") 
# word = 'type'
# print(type(word))

# #Reverse a number without using the built-in-features: 
# def reverse_number(num):
   
#    is_negative = False 
#    reversed_number = 0

#    if num < 0:
#          is_negative = True 
#          num = -num 

#    while num > 0:

#       remainder = num % 10 
#       reversed_number = (reversed_number * 10) + remainder 
#       num = num // 10 

#    if is_negative: 
#          reversed_number = -reversed_number

#    return reversed_number 

# number = -123 
# print("The reversed number is {}.".format(reverse_number(number))) 

# #Reversing a number without using a built-in-features:
# def reverse_number(num):

#       #when the number is negative:
#       is_negative = False
#       if num < 0:
#             is_negative = True 
#             num = -num #making the number positive

#       #when the number is positive:
#       reversed_number = 0 
#       while num > 0:
#             remainder = num % 10 #keeps the last number only
#             reversed_number = reversed_number * 10 + remainder 
#             num = num // 10 #drops the last digit  

#       if is_negative:
#             reversed_number = -reversed_number 

#       return reversed_number 

# number = int(input("Enter a number except one digit: ")) 
# result = reverse_number(number) 
# print(f"The reversed number would be {result}.") 

# #now reversing a number using built-in-features:
# def reverse_number(num):
#       return int(str(num)[::-1]) 

# number = input("Built-in-Features: ")
# result = reverse_number(number) 
# print("The reversed number is {}.".format(result)) 
# print(type(result)) 

# #sum of all natural numbers using recursion:
# def sum(n):
#       if n == 1:
#         return 1
#       else:
#         return n + sum(n - 1) 

# number = 5
# result = sum(number) #argument passed
# print("The sum of 1 to {} is {}.".format(number, result))

# #Sum of all natural numbers:
# def sum(num1, num2):
#   return num1 + num2 

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: ")) 

# result = sum(num1, num2) 
# print("The sum of the given numbers is {}.".format(result)) 

# #n! factorial using recursion:
# def factorial(n):
#   if n == 1:
#     return 1
#   else:
#     return n * factorial(n - 1) 

# number = int(input("Enter a number: ")) 
# result = factorial(number)
# print("The factorial of {} is {}.".format(number, result)) 

# #factorial of a number using for loop:
# factorial = int(input("Enter a number: "))

# result = 1
# for i in range(1, factorial + 1):
#   result = i * result 

# print(result) 

# #Factorial of a number using def function and for loop:
# def factorial(n):
#   result = 1 
#   for i in range(1, n + 1):
#     result *= i 

#   return result 

# num = int(input("Enter a number for factorial: ")) 
# print("The factorial of {} is {}.".format(num, factorial(num)))

# #Guess the number:
# number = 3
# guess = 0
# while number != guess:
#   guess = int(input("What is the number?: ")) 
#   if guess > number:
#     print("You are too high. Go down.") 
#   elif guess < number:
#     print("You are too low. Go up.") 

# print("You have successfully guessed the number which was {}.".format(number)) 


# # 1.	Write a function to calculate the sum of all digits in a given number.
# # For this input: 12345 and the result should be: 15. 

# def sum(n):
  
#   sum_of_numbers = 0 
#   while n > 0:
#     remainder = n % 10 #to get the last digit
#     sum_of_numbers = remainder + sum_of_numbers
#     n = n // 10 #to ommit the last digit

#   return sum_of_numbers

# result = sum(12345)
# print("The sum of the numbers is {}.".format(result)) 

# #Factorial of a number using for loop:
# def factorial(n):
#     result = 1 
#     for i in range(1, n + 1):
#         result *= i 
#     return result 

# number = int(input("Enter a number: ")) 
# print("The factorial of {} is {}.".format(number, factorial(number))) 
# #2.	Write a function to find the most common character in a given string.
# #  Return the most common character in the string. Note: In case of more than one character, 
# # return the first most common character. For this input: ‘hello world’ and the result should be ‘l’. 
# # def most_common_character(s):
# #     b=0
# #     for i in s:
# #         if (s.count(i)>b):
# #             b=s.count(i)
# #             a=i
# #     return a

# from collections import Counter

# def most_common_char(string):
#     # Remove spaces from the string
#     string = string.replace(" ", "")
    
#     # Count the frequency of each character using Counter
#     char_count = Counter(string)
    
#     # Find the character with the maximum frequency
#     most_common = char_count.most_common(1)
    
#     # Return the most common character
#     return most_common[0][0] if most_common else None

# # Example usage
# input_string = 'python programming'
# result = most_common_char(input_string)
# print(f"The most common character is: '{result}'")

# #Print the first random occured character of a string.
# from collections import Counter 

# def most_common_char(string):

#     #remove spaces from the string
#     string = string.replace(" ", "") 

#     #count the frequency of each character 
#     count_frequency = Counter(string) 

#     #count the most common frequency of each character 
#     most_common_frequency = count_frequency.most_common(3) 

#     #return the most common character 
#     return most_common_frequency if most_common_frequency else None 


# string = "Hi! This is Sam Davis with Business Funding Network."
# result = most_common_char(string) 
# print("The most common string is '{}'.".format(result)) 

# from collections import Counter

# def is_full_house(hand):
#     # Count the frequency of each card rank using Counter
#     rank_count = Counter(hand)
    
#     # Get the counts of the ranks
#     counts = list(rank_count.values())
    
#     # Check if we have both a three of a kind and a pair (i.e., counts are [3, 2])
#     return sorted(counts) == [2, 3]

# # Example usage:
# hand = ['2', '2', '3', '3', '3']
# result = is_full_house(hand)
# print(result)  # Output: True


# ###Lists:
# #empty list
# list = [] 

# #list of integers:
# list = [1, 2, 3] 

# #list with mixed data types:
# list_1 = ['mango', 3.2, 3, 8]

# #nested list:
# list_2 = ['mouse', ['man', 8, 'berry'], 2, ['choice'], [list_1]]
# print(list_2[1]) 
# print(list_2[-1])

# #Slicing a list:
# list_3 = ['p', 'y', 't', 'h', 'o', 'n'] 

# #2nd elements to 5th element:
# print(list_3[2:], '\n')
# print(list_3[0:3]) 

# #Change the elements using '=' sign:
# # list_4

# ### Coping a file from a file:
# from sys import argv
# script, from_file, to_file = argv 

# target1 = open(from_file, 'r') 
# # target1.truncate() # You only can use these two files if you only want to trancate the file.
# # print("The file has been erased successfully.") 
# in_data = target1.read() 

# ##copy the file:
# input1 = input("Do you want to copy the file. Write Yes/No:") 
# if input1 == "yes":
#     out_file = open(to_file, 'w') 
#     out_data = out_file.write(in_data)

# elif target1 == 'no':
#     print("The file has not been copied.") 

# target1.close()
# out_file.close()


# ### 
# print("Bottle in his ass.") 

# ## You have 1000 taka. And you bought 2 ice-creams each costs 45 taka 
# # How many candies can you buy with the rest of the money, if the price of the candy is 18 taka each?
# ## And how much taka will be left?

# def candy_money_left(total_money, ice_cream_quantity, ice_cream_price, candy_price):
#     ice_cream_expenditure = ice_cream_quantity * ice_cream_price 
#     money_left_without_ice_cream = total_money - ice_cream_expenditure 
#     candy_expenditure = money_left_without_ice_cream // candy_price 
#     money_left = money_left_without_ice_cream % candy_price 

#     return candy_expenditure, money_left 

# total_money = 1000
# ice_cream_quantity = 2 
# ice_cream_price = 45 
# candy_price = 18 

# ## function in variables:
# candy_purchased, money_left = candy_money_left(total_money, ice_cream_quantity, ice_cream_price, candy_price)
# print(f"There are {candy_purchased} candies can be purchased with the rest of the money.") 
# print("{} Taka will be left.".format(money_left))  
 



#  ## You have 1000 taka. And you bought 2 ice-creams each costs 45 taka 
# # How many candies can you buy with the rest of the money, if the price of the candy is 18 taka each?
# ## And how much taka will be left?

# def candy_and_money(total_money, candy_price, ice_cream_quantity, ice_cream_price):
#     ice_creams_expenditure = ice_cream_quantity * ice_cream_price 
#     money_without_ice_cream = total_money - ice_creams_expenditure 
#     candy_expenditure = money_without_ice_cream // candy_price 
#     money_left = money_without_ice_cream % candy_price 

#     return candy_expenditure, money_left 

# total_money = 905
# candy_price = 18
# ice_cream_quantity = 2
# ice_cream_cost = 45 

# candy, money_left = candy_and_money(total_money, candy_price, ice_cream_quantity, ice_cream_cost) 

# print(f"There are {candy} candies can be purchased and {money_left} Taka is left in total.")


# ### Copying a file:
# from sys import argv 
# script, file_from, file_to = argv 

# # r+ helps a file to read and write at the same time: ###### amazinng
# target1 = open(file_from, 'r+')
# print("Wanna truncate the file:?")
# print("Press enter to continue or press ctrl-c to abort:")
# input("> ")
# target1.truncate() ### erase all contents of the file
# # in_data = target1.read() ### the file has been truncated

# #### But here we can fix the issue that the file can not be empty:
# ## Let's write three lines:
# Line1 = input("Line1: ")
# Line2 = input("Line2: ")
# Line3 = input("Line3: ") 
# ## Now let's write the file:
# target1.write(f"{Line1}\n{Line2}\n{Line3}\n")

# #move the cursor at beginning of the file:
# target1.seek(0) 
# ### Now read the content of the file:
# paste = target1.read()
# #Now open the destination to copy it to:
# target2 = open(file_to, 'r+') ### and that truncated (erased) file has been written to the 'file_to' file.
# target2.write(paste) 
# #Let's read the content first:
# print("So the content of the file is: ") 
# target2.seek(0)
# print(target2.read())
 
# ## Close both files which was opened:
# target1.close()
# target2.close() 



# #### Adding two numbers: ###
# a = int(input("Enter the first number: "))
# b = float(input("Enter the second number: ")) 
# sum = a + b
# print(f"The sum of the two numbers is {sum}.")


# from sys import argv
# #read the WYSS section for how to run this
# script, first, second, third =argv

# print(f"The script is called: {script}") 
# print(f"The first variable is: {first}") 
# print(f"The second variable is: {second}") 
# print(f"The third variable is: {third}") 


# ## sys is a module/libraries: 
# from sys import argv
# script, first, second, third = argv 

# print("The script is called:", script)
# print("The first variable is:", first) 
# print("The second variable is:", second)
# print("The third variable is:", third) 



# ### Variables: strings
# age = input("Enter your age: ") 
# height = input("Waht is your height:") 
# name = input("What is your name?: ") 

# print(f"So, your name is {name}. Your height is {height} and you are {age} years old.") 


# num1 = 'c'
# num2 = 'a'
# num3 = 't'
# num4 = 'm'
# num5 = 'o'
# num6 = 'u'
# num7 = 's'
# num8 = 'e'

# print(num1 + num2 + num3, end=' ') 
# print(num4 + num5 + num6 + num7 + num8) 


# ### Use of formatter:

# box = "{} {} {} {}" 

# val = input(f"Enter four values: {box}")

# print() 

# ########
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday'] 
# months = '\nJan\nFeb\nMar\nAprl\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec\n'
# print("The days are: {}".format(days)) 
# print("The months are: {}".format(months)) 



# ########### Change Items of a list: #############
# num1 = [1, 63, 64, 88] 
# num1[3] = 78 
# print(num1) 

# ######### Add only an element at the end of a list: #@#############
# num2 = ['Two', 3, 'Bill', 99, 3, 'Bob'] 
# num2.append('Robbin') 
# print(num2) 


# ############ Add many elements at the end of a list: ############
# num3 = [86, 'Eight', 'Demons', 76]

# num3.extend([8, 5, 'two', 'ten'])
# print(num3)

# ###### Removing Elements with '.remove()' method ##############
# num3.remove('two')
# print(num3)

# ### del ###
# del num3[:3] 
# print(num3)

# #### single element at the end: ###########
# num3.append('twenty')
# print(num3)

# ####### Adding many elements using '.extend()' method: @#############
# num3.extend([74, 83, 'tiger'])
# print(num3)


# ### Change items #########
# num3[:4] = [1, 2, 'three', 'four'] 
# print(num3)


# ### You have 2000 Taka. You want to purchase 3 cakes with 75 taka each and with the rest of the 
# ### money is gonna be used for purchasing football each cost 400 taka. 
# ## How many footballs can be purchased and how much money will be left?

# def how_many(total_money, cake_quantity, cake_price, football_price):
#     cake_cost = cake_quantity * cake_price 
#     money_left_without_cake = total_money - cake_cost 
#     football_purchased = money_left_without_cake // football_price 
#     money_left = money_left_without_cake % football_price 
#     return football_purchased, money_left 

# total_money = 2000
# cake_quantity = 3 
# cake_price = 75 
# football_price = 400 

# football_purchased, money_left = how_many(total_money, cake_quantity, cake_price, football_price) 

# print(f"{football_purchased} footballs can be purchased and {money_left} Taka will be left.") 


# ##### PDF from pictures:::::: ##########
# from PIL import Image
# img = Image.open("cl.jpg") 
# img.save("pl.pdf", 'PDF')


# ##1. Create a for loop that countss the numbers of even and odd
# # integers in the list below. It should return two strings on
# # seperate lines that prints sentences. And what would
# # be the sum of even and odd integers write them seperately.

# def count_even_odd(numbers):
#     even_count = 0 
#     odd_count = 0 
#     even_sum = 0 
#     odd_sum = 0 
#     for i in numbers:
#         if i % 2 == 0:
#             even_sum += i
#             even_count += 1 
        
#         else:
#             odd_sum += i # adds the odds numbers only.
#             odd_count += 1 #counts the odd numbers from the list.

#     even_result = f"There are {even_count} even numbers and the sum of them is {even_sum} in the list."
#     odd_result = f"There are {odd_count} odd numbers and the sum of them is {odd_sum} in the list." 
    
#     return even_result, odd_result  

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 

# even_sentence, odd_sentence = count_even_odd(list) 

# print(even_sentence)
# print(odd_sentence) 



# ##1. Create a for loop that countss the numbers of even and odd
# # integers in the list below. It should return two strings on
# # seperate lines that prints sentences. And what would
# # be the sum of even and odd integers write them seperately.

# def count_even_odd(num):
#     even_sum = 0 
#     odd_sum = 0 
#     even_count = 0 
#     odd_count = 0 

#     for i in num:
#         if i % 2 == 0:
#             even_sum += i
#             even_count += 1 
        
#         elif i % 2 != 0:
#             odd_sum += i
#             odd_count += 1 

#     odd_result = f"There are {even_count} even numbers and the sum of them is {even_sum}."
#     even_result = "There are {} odd numbers and the sum of them is {}.".format(odd_count, odd_sum) 
#     return odd_result, even_result 

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 

# odd, even = count_even_odd(list) 
# print(odd)
# print(even) 

# # 2. Print trinangles and squares/retangles using loops.

# ## Triangles: ###
# for i in range(7):
#     for j in range(i + 1):
#         print("*", end=' ') 
#     print() 

# print("*" * 20) 
# ###############
# num = 7
# for i in range(num):
#     for j in range(i):
#         print(" ", end=' ') 
    
#     for j in range(num - i):
#         print("*", end=' ') 
#     print() 

# print("*" * 20) 

# ############
# for i in range(num):
#     for j in range(num - i):
#         print("*", end=' ') 
#     print() 


# ############
# print("*" * 20) 

# ## DIAMOND SHAPE: ##############
# for i in range(num - 1):
#     for j in range(num - i):
#         print(" ", end=' ') 
    
#     for j in range(i + 1):
#         print("*", end=' ') 

#     for j in range(i):
#         print("*", end=' ')
#     print()
    
#     ################### Next Portion ##########

# for i in range(num):
#     for j in range(i + 1):
#         print(" ", end=' ') 

#     for j in range((num - 1) - i):
#         print("*", end=' ') 

#     for j in range(num - i):
#         print("*", end=' ')
#     print() 

# print("*" * 30)


# # ########## A pdf file: ############
# # from PIL import Image
# # from sys import argv 
# # script, file_name, pdf_file = argv 
# # img = Image.open(file_name)
# # svg = img.save(pdf_file, "PDF") 

# # #### Taking input from the user #########
# # from PIL import Image
# # existing_file = input("Enter the file name: ") 
# # creating_file = input("Name the file with \".pdf\": ")

# # img = Image.open(existing_file) 
# # svg = img.save(creating_file, "PDF") 
# # print("The file has been converted successfully.") 


# # 1. Create a for loop that countss the numbers of even and odd
# # integers in the list below. It should return two strings on
# # seperate lines that prints sentences. And what would
# # be the sum of even and odd integers write them seperately.

# def count_even_odd(number):
#     even_count = 0 
#     odd_count = 0 
#     even_sum = 0 
#     odd_sum = 0 
#     for num in number:
#         if num % 2 == 0:
#             even_count = even_count + 1 #counts the number of even numbers
#             even_sum += num ## sums up the even numbers 

#         elif num % 2 != 0:
#             odd_count += 1 
#             odd_sum += num ### sum up the odd numbers 

#     even_result = f"There are {even_count} even numbers and the sum of them is {even_sum}."
#     odd_result = "There are {} odd numbers and the sum of them is {}.".format(odd_count, odd_sum) 

#     return even_result, odd_result 

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 

# even, odd = count_even_odd(list) 

# print(even) 
# print(odd) 


# ### Squarees ###
# print("Square:") 
# n = 7
# for j in range(n):
#     for a in range(n):
#         print("*", end=' ') 
#     print() 

# print("\n\ntriangle: 1")
# ### triangle:1 ###
# for j in range(n):
#     for a in range(j + 1):
#         print("*", end=' ') 
#     print() 

# print("\n\nTriangle: 2") 
# ### triangle:2 #### 
# for j in range(n):
#     for a in range(j + 1):
#         print("*", end=' ') 
#     print() 

# print("\n\nTriangle: 3")
# ### triange: 3 ####
# for j in range(n):
#     for a in range(n - j):
#         print(" ", end=' ')
#     for a in range(j + 1):
#         print("*", end=' ') 
#     print() 

# print("\n\nTriangle: 4") 
# ### Triangle: 4 #### 
# for j in range(n + 1):
#     for a in range(n - j):
#         print("*", end=" ") 
#     print() 

# print("\n\nTriangle: 5") 
# ### Triangle: 5 ### 
# for j in range(n):
#     for a in range(j + 1):
#         print(" ", end=' ') 
#     for a in range(n - j):
#         print("*", end=' ')
#     for a in range((n-1) - j):
#         print("*", end=' ')
#     print() 

# ### Remaining Half: 
# for j in range(n):
#     for a in range(n - j):
#         print(" ", end=" ") 
#     for a in range(j + 1):
#         print("*", end=" ")
#     for a in range((j - 1) + 1):
#         print("*", end=" ") 
#     print() 


# # 4.  Write a for loop that prints the integers from the
# # following/a list, but only if they are even.

# def even_number(list):
#     even_count = 0 
#     even_sum = 0
#     for a in list:
#         if a % 2 != 0:
#             even_count += 1
#             even_sum += a 
#     even_result = f"There are {even_count} even numbers in the list."
#     even_sum_result = "The sum of the even numbers is {}.".format(even_sum)
#     return even_result, even_sum_result 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
# even, even_sum_result = even_number(numbers) 
# print(even)  
# print(even_sum_result) 


# for _ in range(4):
#     print("###")

# # for _ in iter(int, 1):
# #     print("Hello!")

# # while True:
# #     print("Hi!")

# ### Encoding strings: ##########
# text = "Ei je dunya"
# encoded_text = text.encode("utf-8") ## text has been encoded
# print(encoded_text) ## converted into bytes 

# text = """
# Do you love me now?
# I wanna love you
# More than you can say.
# """

# encoded_text = text.encode("utf-8", errors='replace') 
# print(encoded_text) 

# ### Reverse a number:

# num = int(input("Enter a number to reverse: ")) ## taking input from the user

# is_negative = False 
# if num < 0:
#     is_negative = True 
#     num = -num 

# reverse_number = 0 
# while num > 0:
#     remainder = num % 10 ### Get the last digit
#     reverse_number = reverse_number * 10 + remainder 
#     num = num // 10 

# if is_negative:
#     reverse_number = -reverse_number 
# print("The reversed number is {}.".format(reverse_number)) 


# ### # Write a Python function named count_vowels that takes a string as input 
# # and returns the number of vowels (a, e, i, o, u) in the string.

# def count_vowels(string):
#     vowels = 'AEIOUaeiou'
#     count_vowel = 0 

#     for str in string:
#         if str in vowels:
#             count_vowel += 1

#     vowel_number = "The number of vowels is {}.".format(count_vowel) 
#     return vowel_number 

# text = "I have a hope and I have a future."
# encoded_text = text.encode("utf-16", errors='replace')
# number_of_vowel = count_vowels(text) 
# print(number_of_vowel) 
# print("Garbled text:", encoded_text) 


# 1. Create a for loop that countss the numbers of even and odd
# integers in the list below. It should return two strings on
# seperate lines that prints sentences. And what would
# be the sum of even and odd integers write them seperately.


# def count_even_odd(list):
#     even_count = 0 
#     odd_count = 0 
#     even_sum = 0 
#     odd_sum = 0 

#     for number in list: 
#         if number % 2 == 0:
#             even_count += 1 
#             even_sum += number 

#         elif number % 2 != 0:
#             odd_count += 1
#             odd_sum += number 

#     even_result = "There are {} even numbers and the sum of them is {}.".format(even_count, even_sum) 
#     odd_result = "There are {} odd numbers and the sum of them is {}.".format(odd_count, odd_sum) 

#     return even_result, odd_result 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
# even, odd = count_even_odd(numbers) 
# print(even) 
# print(odd)  


# ###### square: ###
# num = 7
# for i in range(num):
#     for j in range(num):
#         print("*", end=' ') 
#     print() 

# print("\n\nTriangle:1")
# ##### Triangle: 1 ###
# for i in range(num):
#     for j in range(i + 1): 
#         print("*", end=' ') 
#     print() 

# print("\n\nTriangle: 2") 
# ##### Triangle:2 #########
# for i in range(num):
#     for j in range(i + 1):
#         print(" ", end=' ') 
#     for j in range(num - i):
#         print("*", end=' ') 
#     print() 

# print("\n\nTriangle: 3") 
# ##### Triangle: 3 ####### 
# for i in range(num):
#     for j in range(num - i):
#         print(" ", end=' ') 
#     for j in range(i + 1):
#         print("*", end=' ') 
#     for j in range(i):
#         print("*", end=' ') 
#     print() 

# print("\n\nDiamond Shape: ") 
# #######Diamond shape: ############
# for i in range(num - 1):
#     for j in range(num - i):
#         print(" ", end=' ') 
#     for j in range(i + 1):
#         print("*", end=' ') 
#     for j in range(i):
#         print("*", end=' ') 
#     print() 

# ####### Remaining portion ##########
# for i in range(num):
#     for j in range(i + 1):
#         print(" ", end=' ') 
#     for j in range(num - i):
#         print("*", end=' ') 
#     for j in range((num - 1) - i):
#         print("*", end=' ') 
#     print() 


# ###### Printing a list: #############
# fruits = ['apple', 'cherry', 'mango', 'lichi'] 
# print(fruits, "\n\n")

# print("Adding an item at the end of the list using '.append()' method: ")
# fruits.append('berry') ## adding an item at the end of the list 
# print(fruits, '\n\n')

# print('Removing the item "mango" using remove:')
# fruits.remove('mango') ### remove an item 
# print(fruits, "\n\n")

# print("Expanding the list: .expand()") 
# fruits.extend(['lichi', 'bananna', 'jackfruit'])
# print(fruits, "\n\n") 



# ########### Reverse a list using SWAP: ############## 
# def reverse_sequence(sqc):
#     left = 0
#     right = len(sqc) - 1

#     while left < right:

#         sqc[left], sqc[right] = sqc[right], sqc[right] 
        
#         left += 1 
#         right -= 1

# my_list = [1, 2, 3, 4, 5, 54] 

# reverse_sequence(my_list)
# print(my_list, '\n\n')


# ######### Reverse number: #####
# def reverse_sqc(num):
    
#     left = 0 
#     right = len(num) - 1

#     num[left], num[right] = num[right], num[left] 

#     left += 1 
#     right -= 1 

# fruits = ['lichi', 'mango', 'jackfruit', 'cherry', 'banana'] 
# reverse_sqc(fruits)
# print(fruits) 


# #### reverse a single digit: ############
# def reverse_single_digit(num):
#     is_negative = False 
#     if num < 0:
#         is_negative = True  
#         num = -num 
#     reverse_number = 0 
#     while num > 0:
#         remainder = num % 10 #### keeps the last digit ## remainder ###
#         reverse_number = reverse_number * 10 + remainder 
#         num = num // 10  ### quotient 
        
#     return reverse_number
# number = 554 
# result = reverse_single_digit(number) 
# print("The number has been reversed:", result) 


# ## Remove 'blue from the list below and print the updated list.
# colors = ['red', 'yellow', 'brown', 'blue', 'grey'] 
# colors.remove('blue') 
# print("The colors are without 'blue' now: {}".format(colors), '\n')

# #6. Given the list below, print the first three elements using slicing.
# colors = ['red', 'blue', 'green', 'brown', 'balck'] 
# colors1 = colors[:3] 
# print(colors1, '\n') 


# #7. Write a for loop to print each element of the list below.
# people = ["James", "Robert", "Ben", "Peter", "Aron"] 
# for man in people:
#     print(man) 

# # 8. Check if 'apple' exists in the list below and print True or False.
# fruits = ['apple', 'goava', 'pineapple', 'cherry'] 
# print("Is the apple in the list fruits", 'apple' in fruits)


# # 9. Sort the list below in asscending order and print it.
# numbers = [23, 2, 18, 44, 3, 50, 100, 64, 48] 
# numbers.sort() 
# print(numbers) 

# ### Using 'while loop' and join() method#########

# food = []
# foods = input("Enter food's name to eat and 'q' to quit: ").title() 

# while foods != 'Q':
#     food.append(foods)
#     foods = input("Enter the food's name to eat and 'q' to quit: ").title() 
      
# print("You like {}.".format(", ".join(food)))


# ## 11. Write a Python program to reverse a list without using reverse() or
# # slicing. (Bonus Challenge)


# def reverse_lst(lst):
#     left = 0 
#     right = len(lst) - 1 
        
#     lst[left], lst[right] = lst[right], lst[left] 

#     left += 1 
#     right -= 1 

# my_list = [1, 2, 3, 4, 5, 6]
# reverse_lst(my_list) 
# print("The list has been reversed successfully: {}".format(my_list)) 


# ## PDF from .jpg 3###########
# from PIL import Image 
# img = Image.open("cl.jpg") ## open the image
# svg = img.save("top.pdf", "PDF") 
# print("The image has been converted into pdf successfuly.") 


# ### 12. Write a Python program to remove duplicate elements from the list
#     # below and print the updated list. numbers = [1, 2, 2, 3, 4, 4, 5]
# numbers = [1, 2, 2, 3, 4, 4, 5] 
# num = list(set(numbers)) 
# print(type(num), num, '\n\n') 

# ## 12. Do it manually: #####
# unique_numbers = [] 

# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)  

# print(unique_numbers, '\n\n')

# ##13. Write a Python program to find and print the largest number from the
#     # list below. values = [10, 45, 2, 99, 23, 78]

# values = [10, 45, 2, 99, 23, 78] 

# largest = values[0] 

# for num in values:
#     if num > largest:
#         largest = num 

# print(largest) 

# ## Using buit-in function max(): ###########
# values = [10, 45, 2, 99, 23, 78] 

# largest = max(values) 
# print("The largest number is: {}".format(largest)) 


# ## Find the smallest number from the following list: ###########
# lst = [34, 83, 23, 44, 8, 4] 

# smallest = lst[0] 

# for num in lst:
#     if num < smallest:
#         smallest = num 

# print("The smallest number from the list is: {}".format(smallest)) 

# #### Set: Set:  ############################################################
# ## unordered, immutable, and no duplication: ####################
# my_set = {1, 4, 2, 4, 3} 
# print(my_set) 
# 
# ## add() #####
# add = my_set | {9}  
# print("Add", add) 
# 
# add.add(10) 
# print("Adding 10:", add) 
# 
# add.remove(2) 
# print("2 is removed:", add) 
# 
# ## discard()  ###########
# add.discard(10)
# print("10 is discarded", add) 
# 
# ## updated() ## to add multiple elements #
# add.update({14, 13})
# print("13 and 14 have been updated:", add) 
# 
# ### pop() #### remove a random number 
# add.pop() 
# print("Removes a random number:", add) 
# 
# ## clear() ## clears the whole set ##
# add.clear() 
# print("add variable is empty now:", add) 
# 
# ############# Union Set: (|) OR union() #####################
# num1 = {1, 3, 8, 6} 
# num2 = {8, 9, 2, 6} 
# 
# my_union = num1 | num2 
# print("Prints all the elements of num1 and num2 except duplication: ", my_union) 
# 
# ########## Set Intersection: (&) OR intersection() ######################
# my_intersection = num1 & num2 
# print("Prints only the common elements: ", my_intersection) 
# 
# 
# ########### Set difference: (-) OR difference() ############### 
# my_difference = num1 - num2 
# print("Prints the elements which are subtracted from num2: ", my_difference) 
# 
# 
# ####### Symmetric difference (^) or symmetric_difference ##############
# my_symmetric_difference = num1 ^ num2 
# print("Prints all the elements except the common ones: ", my_symmetric_difference) 
# 
# ten_things = "Apples Oranges Crows Telephone Light Sugar"
# print("Wait there are not 10 things in that list. Let's fix that.") 
# 
# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# 
# while len(stuff) != 10:
#     next_one = more_stuff.pop() 
#     print("Adding:", next_one) 
#     stuff.append(next_one) 
#     print("There are {} items now.".format(len(stuff))) 
# 
# print(f"There we go: ", stuff) 
# print('Let\'s do something with stuff.') 
# 
# print(stuff[1]) 
# print(stuff[-1]) 
# print(stuff.pop()) 
# print(' '.join(stuff)) 
# print('#'.join(stuff[3:5])) 
# 
# 
# 
# #
# words = "Apple Bananna Cherry Goava Phone Laptop"
# my_words = words.split(' ') 
# 
# more_words = ['headphone', 'page', 'stickynote', 'cat', 'Larry'] 
# 
# while len(my_words) != 10:
#     stuff = more_words.pop() 
#     print("Adding: ", stuff) 
#     my_words.append(stuff) 
#     print(f"There are {len(my_words)} items now.") 
#      
# print(f"The 10 items are: ", my_words) 
# print(my_words[1]) 
# print(my_words[-1]) 
# print(my_words.pop()) 
# print(f"There are {len(my_words)} items now as we poped: {words}") 
# print(' '.join(my_words)) 
# print('#'.join(my_words[2:7])) 
# 
# 
# #Exercise 38: 
# some_words = "Phone Notepad Earphone Car Rat"
# words = some_words.split() 
# more_words = ["Ball", "Girl", "Party", "Book", "Most", "Hit"] 
# 
# while len(words) != 10:
#     stuff = more_words.pop() 
#     print("Adding: ", stuff) 
#     words.append(stuff) 
#     print(f"There are {len(words)} item now.") 
# 
# print("The {} words are {}.".format(len(words), words))
# print(words[1]) 
# print(words[-1]) 
# print(words.pop()) 
# print(' '.join(words)) 
# print(' #'.join(words[2:7])) 
# #Extracting a .zip file:
# import zipfile 
# file_name = input("File name to extract: ") 
# 
# with zipfile.ZipFile(file_name, 'r') as archive: 
#     archive.extractall()

#create a mapping of state to abbreviation 
states = {
    'Oregon': 'OR',
    'Florida': 'FL', 
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them 
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville' 
}

#add some more cities 
cities['NY'] = 'New York' 
cities['OR'] = 'Portland' 

#print out some cities 
print('-' * 10) 

print("NY State has:", cities['NY']) 
print("OR State has:", cities['OR']) 

#print some states 
print('-' * 10) 
print("Michigan's abbreviation is: ", states['Michigan']) 
print("Florida's abbreviation is: ", states['Florida']) 

#do it by using the state then cities dict 
print('-' * 10) 
print("Michigan has: ", cities[states['Michigan']]) 
print("Florida has: ", cities[states['Florida']]) 

#print every state abbreviation 
print('-' * 10) 
for state, abbrev in list(states.items()): 
    print(f"{state} is abbreaviated {abbrev}")  

#print every city in state 
print('-' * 10) 
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}") 

#now do both at the same time
print('-' * 10) 
for state, abbrev in list(states.items()): 
    print(f"{state} state is abbreviated {abbrev}") 
    print(f"and has city {cities[abbrev]}")

print('-' * 10) 
# safely get a abbreviation by state that might not be there 
state = states.get('Texas') 

if not state:
    print("Sorry, no Texas.") 

#get a city with a defaoult value 
city = cities.get('TX', 'Does Not Exist') 
print(f"The city for the state 'TX' is: {city}") 

#make a dictionary:
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}.")
    print(f"{state}: {abbrev}")   