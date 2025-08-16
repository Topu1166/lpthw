# ################## Rtading from a file using argv and input function: ###################
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
#     right = len(num) - 1] = num[right], num[left] 
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


# #Given the list below, print the third element.
# my_list = [1, 2, 3, 4] 
# print(my_list[2]) 

# #Change the second element of the list below to "grape" and print the
# #    updated list.

# fruits = ['apple', 'berry', 'banana', 'orange', 'pineapple'] 
# fruits[1] = 'grape' 
# print("The second element is", fruits[1],'.') ## this is a bad practice  
# print("The second element is {}.".format(fruits[1])) ## this is a good practice using formats 

###Add 'orange' to the end of the list below.
#fruits = ['apple', 'berry', 'banana', 'orange', 'pineapple'] 
#print(fruits) 
#fruits.append('orange')
#print("There is an orange at the end. {}".format(fruits, '\n'))
#
#
#### Let's extend the list using .extend() method: ####################
#fruits.extend({"mango", "goava", "malta", "orenge"})
#print("The list has been extended: )", fruits)
#
##fruits.clear() 
##print("All the items have been removed:", fruits) 
#
#fruits.remove('mango')
#print("The mango has been removed: ", fruits) 
#
#
## Write a function that takes a sentence, and returns the 
## longest even-length word in the sentence. Or if it has no 
## even-length words, return "00".
## It means: 
##1. Take a sentence (a string of words).
##2. Check each word in the sentence. 
##3. Find the longest word that has an even number of character.
##4. Return that word.
##5. if there's no word with even length, then return "00". 
#
##from sys import argv 
##script, text = argv #taking an input 
## 1.
#def longest_even_word(text):
#    
#    words = text.split() 
#    longest = "" 
#
#    for word in words:
#        if len(word) % 2 == 0:
#            if len(word) > len(longest):
#                longest = word   
#
#    if longest == "":
#        return "00"
#    
#    else:
#        return longest  
#
#sentence = input("Enter a sentence: ") 
#result = longest_even_word(sentence) 
#
#print(result) 
#
#
## Write a function that takes a sentence, and returns the 
## longest even-length word in the sentence. Or if it has no 
## even-length words, return "00".
## It means: 
##1. Take a sentence (a string of words).
##2. Check each word in the sentence. 
##3. Find the longest word that has an even number of character.
##4. Return that word.
##5. if there's no word with even length, then return "00". 
#
## 2. 
#def longest_even_word(text):
#
#    words = text.split() 
#    longest = "" 
#    
#    for word in words: 
#        if len(word) % 2 == 0 and len(word) > len(longest): 
#            longest = word 
#
#    
#    if longest == "":
#        return "00"
#    else: 
#        return longest 
#
#sentence = input("Enter a sentence: ") 
#result = longest_even_word(sentence) 
#print(result) 
#


# # Write a function that takes a sentence, and returns the 
# # longest even-length word in the sentence. Or if it has no 
# # even-length words, return "00".
# # It means: 
# #1. Take a sentence (a string of words).
# #2. Check each word in the sentence. 
# #3. Find the longest word that has an even number of character.
# #4. Return that word.
# #5. if there's no word with even length, then return "00". 
# 
# # 3.
# def longest_even_word(text):
# 
#     words = text.split() 
#     longest = "" 
# 
#     for word in words:
#         if len(word) % 2 == 0 and len(word) > len(longest):
#                 longest = word  
# 
#     if longest == "":
#         return '00'
#     else: 
#         return longest 
# 
# sentence = input("Enter a sentence: ") 
# result = longest_even_word(sentence) 
# print(result) 
# 
# #Find the sum of a number using recursion:
# 
# def sum_recursion(number):
#     if number == 1:
#         return 1
#     
#     else: 
#         return number + sum_recursion(number - 1) 
# 
# num = int(input("A sum of a number: ")) 
# result = sum_recursion(num) 
# print(f"The sum of the number is {result}.")
# 
# 
# ## Find the factorial of a number: 
# 
# def factorial(x):
#    if x == 1:
#        return 1 
# 
#    else:
#        return x * factorial(x - 1) 
# 
# integer = int(input("Enter a number to see the factorial: ")) 
# result = factorial(integer) 
# print(f"The factorial of {integer} is {result}.")
# 
# ## Find the greatest number from a list:
# 
# 
# def greatest_num(numbers):
# 
#     greatest = 0 
# 
#     for number in numbers:
#         
#         if number > greatest:
#             greatest = number 
# 
#         return greatest  
# 
# 
# numbers = [33, 83, 35, 234, 95] 
# result = greatest_num(numbers) 
# print("The greatest number from the list is {}.".format(result))
# 
# 
# #Find the sum of a number usning recursion:
# 
# def sum_recursion(number):
# 
#     if number == 1:
#         return 1
# 
#     else:
#         return number + sum_recursion(number - 1) 
# 
# integer = int(input("Enter a number to see its sum: ")) 
# result = sum_recursion(integer) 
# print(f"The sum of the number is {result}.") 
# 
# 
# #Find the factorial of a number:
# 
# def factorial(num):
# 
#     if num == 1:
#         return 1 
#     
#     else:
#         return num * factorial(num - 1) 
# 
# number = int(input("Enter a number for its factorial: ")) 
# result = factorial(number) 
# print(f"The factorial of a number is {result}.")


# #Print the largest number from a list.
# 
# def largest_number(numbers):
# 
#     largest = 0
#     for number in numbers:
#         if number > largest:
#             largest = number
# 
#     return largest 
# 
# integers = [23, 23, 98, 89, 53, 98, 8] 
# result = largest_number(integers) 
# print("The largest number is {}.".format(result)) 
# 
# 
# #let's remove the duplicate elements :
# remove_duplicate = set(integers) 
# print(f"There are no duplicates here: {remove_duplicate}") 
# 
# 
# #Find the average of a list. 
# 
# numbers = [10, 20, 30, 40, 50] 
# 
# def average(my_list):
# 
#     avg = sum(my_list) / len(my_list) 
#     return avg
# 
# result = average(numbers) 
# print(f"The average number is {result}.") 
# 
# #Find the average of a list using lambda function: 
# 
# averg = lambda lst: sum(lst) / len(lst) #lambda function 
# 
# result = averg(numbers) 
# print("The average of the number is {}.".format(result))
# 
# 
# # Find the square of the numbers of a list:
# 
# num = [2, 4, 8, 16, 32] 
# 
# def square_num(sqr):
#     squared = [] 
# 
#     for number in sqr:
#         squared.append(number ** 2) 
# 
#     return squared 
# 
# result = square_num(num) 
# print("The squared numbers are {}.".format(result)) 
# 
# 
# #Find the square of the numbers of a list using lambda
# 
# sqr_number = map(lambda number: number ** 2, num) 
# print(f"The squared of the numbers are {list(sqr_number)}.") 
# 
# 
# 
# #Find the square of the numbers of a list.
# 
# numbers = [2, 4, 5, 8, 32] 
# 
# def square_num(my_list):
# 
#     squared_number = [] 
#     
#     for num in my_list:
#         squared_number.append(num ** 2) 
# 
#     return squared_number 
# 
# result = square_num(numbers) 
# print(f"The square of the numbers are {result}.")
# 
# #Make an accending order of a list. 
# 
# numbers = [23, 88, 54, 2, 8, 6, 11]  
# accending_order = [] 
# 
# def accending(num):
#     greater = 0  
#     for number in num:
# 
#         if number > greater:
#             greater = number 
#             
#             if greater > number:
#                 accending_order.append() 
# 
#     return accending_order 
# 
# result = accending(numbers) 
# print(f"The accending order would be {result}.") 

# #Exercise 8:
# formatter = "{} {} {} {}" 
# 
# print(formatter.format(3, 4, 5, 8))
# print(formatter.format("two", "three", "four", "five")) 
# print(formatter.format(True, False, False, True)) 
# print(formatter.format(formatter, formatter, formatter, formatter)) 
# print(formatter.format(
#     "There was a king",
#     "who was so cruel and unkind.",
#     "One day a wise man came to him",
#     "and said how you doing? The king..."
# ))
# 
# #Exercise 9:
# # Here's some new strange stuff, remember type it exactly.
# days = "Mon Tue Wed Thu Fri Sat Sun" 
# Months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec\n" 
# 
# print("Here are the days", days) 
# print("Here are the months", Months) 
# 
# print(""" 
# There is something going on here.
# with the three double-quotes.
# We'll be able to type as much as we lie. 
# Even 4 lines if we want, or5, or 6. 
#  """)
# 
# #Exercie 10:
# 
# tabby_cat = "\tI'm tabbed in." 
# persian_cat = "I'm split\non a new line."
# backslash_cat = "I'm \\ a \\ cat." 
# 
# fat_cat = """
# I'll do a list: \n
# \t*Cat Food
# \t*Fishies
# \t*Catnip\n\t*Grass
# """
# print(tabby_cat) 
# print(persian_cat) 
# print(backslash_cat) 
# print(fat_cat) 
# 
# 
# # Let's read a file: 
# from sys import argv 
# script, file_name = argv 
# 
# target = open(file_name, 'r') 
# print(target.read()) 

## seek(0) and read_line() 

# from sys import argv 
# script, file = argv 
# 
# file_name = open(file)
# 
# def rewind(f):
#     f.seek(0) 
# 
# def read_line(current_line, f):
#     print(current_line, f.readline()) 
# 
# #call the function:
# rewind(file_name)  
# 
# for current_line in range(10):
#     read_line(current_line, file_name)    

# 
# #Find the average number from a list: 
# 
# numbers = [1, 2, 3, 4, 5] 
# 
# def average_num(num):
# 
#     average = sum(num) / len(num) 
#     return average 
# 
# result = average_num(numbers) 
# print("The average of a number is {}.".format(result)) 
# 
# 
# #Write a python grogram to find and print the 
# #largest number from the list below. 
# # values = [10, 45, 2, 99, 23, 78] 
# 
# values = [10, 45, 2, 99, 23, 78] 
# 
# def largest_num(num):
#     largest = 0 
#     for number in num: 
#         if number > largest:
#             largest = number 
# 
#     return largest 
# 
# result = largest_num(values) 
# print("The largest number from the list is {}.".format(result)) 
# 
# 
# #Write a Python program to reverse a list without 
# #using reverse() or slicing. (Bonus Challenge) 
# 
# def reverse_lst(num):
# 
#     left = 0 
#     right = len(num) - 1 
# 
#     num[left], num[right] = num[right], num[left] 
# 
#     left += 1 
#     right -= 1 
# 
#     return num 
# 
# result = reverse_lst(values) 
# print("The actual values {}".format(values)) 
# print(result)
# 
# 
# #Create a new list containing the squares of numbers
# #from 1 to 5 using list comprehension. 
# 
# #First without using a list comprehension: 
# values = [2, 3, 4, 8, 9] 
# squared = [] 
# 
# def square_val(num):
# 
#     for number in num:
#         squared.append(number ** 2) 
# 
#     return squared 
# 
# result = square_val(values) 
# print("Actual values: {}".format(values)) 
# print("The squared values are {}.".format(result)) 
# 
# 
# #Using list of comprehension: 
# values = [2, 3, 4, 8, 9]
# 
# square_value = [x ** 2 for x in values]
# 
# print("Actual value: {}".format(values)) 
# print("Squared values: {}".format(square_value)) 
# 
# 
# #if I had used other approaches for square value:
# 
# def square_val(val):
#     square = [] 
#     for value in val: 
#         square.append(value ** 2)
# 
#     return square 
# 
# result = square_val(values) 
# print("The second approach of the same thing is {}.".format(result))
# 
# 
# #Find the even number using a list comprehension:
# values = [2, 3, 23, 88, 27, 4, 28, 3] 
# 
# even_num = [x for x in values if x % 2 == 0] 
# print(even_num) 
# 
# #square the even number: 
# square_even_val = [x ** 2 for x in even_num] 
# print("Squared the even number: {}.".format(square_even_val))
# 
# #Let's print the same thing in a traditional way:
# 
# def square_even_value(lst):
#     square_even_num = [] 
#     for x in lst: 
#         square_even_num.append(x ** 2) 
# 
#     return square_even_num 
# 
# result = square_even_value(even_num)
# print("Another approach to square a list: {}.".format(result)) 
# 
# 
# #Find the longest word from a sentence: 
# sentence = input("Enter a sentence: ") 
# 
# def longest_word(sentence):
#     words = sentence.split() 
#     longest = ""
# 
#     for word in words: 
#         if len(word) > len(longest):
#             longest = word  
#         
#     return longest 
# 
# result = longest_word(sentence) 
# print("The longest word is '{}'.".format(result))
# 
# #:
# sentence = input("Enter a sentence: ")  
# 
# def lengest_word(sentence):
#     longest = "" 
#     words = sentence.split() 
#     for word in words:
#         if len(word) > len(longest):
#             longest = word 
# 
#     return longest 
# 
# result = lengest_word(sentence) 
# print("The longest word is {}.".format(result)) 

# def break_words(sentence):
#     words = sentence.split() 
#     return words 
# 
# def sort_words(words):
#     return sorted(words) 
# 
# def print_first_word(words):
#     word = words.pop(0) 
#     return word 
# 
# def print_last_word(words):
#     word = words.pop(-1) 
#     return word 
# 
# def sort_sentence(sentence):
#     words = sort_words(sentence) 
#     return sort_words(words) 
# 
# def print_first_and_last(sentence):
#     words = break_words(sentence) 
#     print_first_word(words) 
#     print_last_word(words) 
# 
# def print_first_and_last_sorted(sentence):
#     words = sort_sentence(sentence) 
#     print_first_word(words) 
#     print_last_word(words) 
# 
# my_list = ["Will", "you", "marry", "me", "Anna?"] 
# sorted_words = sorted(my_list) 
# print(sorted_words) 

# # Functions Within a function: 
# # 1. Break/split the words of a sentence/paragraph.
# def break_words(sentence):
#     words = sentence.split(' ') 
#     return words 
# 
# # 2. Sort those broken words : 
# def sort_words(words):
#     words = sorted(words) 
#     return words 
# 
# # 3. print the first word:
# def print_first_word(words):
#     word = words.pop(0) 
#     print(word) 
# 
# # 4. print the last word:
# def print_last_word(words):
#     word = words.pop(-1) #functions/methods can be returned directly. 
#     print(word) 
# 
# # 5. Sort a sentence: #break_words then sort
# def sort_sentence(sentence):
#     words = break_words(sentence)
#     return sort_words(words) 
# 
# # 6. Print the first and the last word of sentence.
# def first_and_last_word(sentence):
#     words = break_words(sentence) 
#     print_first_word(words) 
#     print_last_word(words) 
# 
# # 7. Print first and last after sorted:
# def first_and_last_sorted(sentence):
#     words = sort_sentence(sentence) 
#     print_first_word(words) 
#     print_last_word(words) 

# Functions within a function:
# 1. Break_words of a function 
def break_words(sentence):
    words = sentence.split() 
    return words
# 2. Sort_words: 
def sort_words(sentence):
    words = sorted(sentence) 
    return words 
# 3. Print the first word:
def print_first_word(word):
    first_word = word.pop(0) 
    print(first_word) 
# 4. Print the last word: 
def print_last_word(word):
    last_word = word.pop(-1) 
    print(last_word) 
# 5. Sorted_sentence:
def sort_sentence(sentence):
    words = break_words(sentence) 
    return sort_words(words) 
# 6. Print the first and last words altogether:
def print_first_and_last(sentence):
    word = break_words(sentence) 
    print_first_word(word) 
    print_last_word(word)
# 7. Print the first and last sorted words: 
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence) 
    print_first_word(words) 
    print_last_word(words) 


# # pdf images:
# from sys import argv 
# script, file_name = argv 
# from PIL import Image 
# img = Image.open(file_name) 
# svg = img.save("top.pdf", "PDF") 
# print(svg) 

# #Converting into pdf:
# from PIL import Image 
# file_name = input("Enter a file name: ") 
# rename = input("Rename the file using .pdf: ") 
# img = Image.open(file_name) 
# svg = img.save(rename, 'PDF') 
# print("The file has been successfully saved as {}.".format(rename)) 

# # Change the second element of the list below 
# # to "grape" and print the updated list.
# my_list = ['banana', 'pineapple', 'apple', 'cherry'] 
# my_list[2] = 'grape'
# print("The updated list is {}".format(my_list)) 
# 
# my_list.append('orange') 
# print("Orange at the end: {}".format(list)) 
# 
# #Remove 'blue' from the list below and print 
# # the updated list. 
# my_list = ['green', 'red', 'yellow', 'blue', 'black'] 
# my_list.remove('blue') 
# print("Without blue: {}".format(my_list)) 
# 
# print("Does apple exist in my_list?", 'apple' in my_list) 
# 
# # Given the list belo, print the first three
# # elements using slicing.
# print("First three items:", my_list[:3])
# 
# #Sort the list below in ascending order:
# my_list = [20, 2, 3, 88, 4, 9] 
# in_order = sorted(my_list)  
# print("They are in ascending order now: {}".format(in_order))
# 
# 
# #Create a new list containing the squares of numbers
# #from 1 to 5 using list comprehension. 
# my_list = [1, 2, 3, 4, 5] 
# list_comp = [x ** 2 for x in my_list] 
# print("The squares of numbers are: {}".format(list_comp)) 
# 
# #Write a Python program to reverse a list without
# #using reverse() or slicing.(Bonus Challenge) 
# def reverse_list(lst):
#     left = 0 
#     right = len(lst) - 1 
#     
#     while left < right: 
#         lst[left], lst[right] = lst[right], lst[left] 
#         left += 1 
#         right -= 1 
# 
# reverse_list(my_list)
# print("The reversed list is {}".format(my_list)) 
# 
# # #Write a Python program to remove duplicate elements
# # #from the list below and print the updated list. 
# duplicate = [2, 8, 1, 2, 4, 2, 5] 
# # no_duplicate = list(set(duplicate))  
# # # my_list = no_duplicate.list()  
# # print("No duplicates: {}".format(no_duplicate))
# 
# #know about constant/global:
# dup = duplicate 
# 
# carry = []
# def remove_dup(lst):
#     for x in lst:
#         if x not in carry:
#             carry.append(x)
#         
#     return carry 
# 
# rslt = remove_dup(dup)
# rslt1 = sorted(rslt) #ascending order 
# print("No duplicate: {}".format(rslt1))
# 
# #Doing the same thing using built-in-function:
# #remove the duplicate:
# my_list = [1, 22, 2, 22, 4, 88, 4] 
# remv_dup = list(set(my_list)) 
# print("No duplicate: {}".format(remv_dup)) 

# # Write a Python program to find and print the 
# # largest number from the list below. 
# # values = [10, 45, 2, 99, 23, 78] 
# values = [10, 45, 2, 99, 23, 78] #global variable
# 
# def largest_num(lst):  
#     largest = 0 
#     for x in lst: 
#         if x > largest: 
#             largest = x
# 
#     return largest 
# 
# rslt = largest_num(values)
# print("Therefore, the largest number is {}.".format(rslt)) 
# 
# #Find the average number of a list using def and
# #lambda functions. 
# my_list = [2, 8, 7, 19, 40] 
# 
# average = sum(my_list) / len(my_list) 
# print("The average number is {}.".format(round(average))) 
# 
# # use the lambda function below:
# 
# 
# # Find the even numbers from a list.
# my_list = [2, 3, 8, 4, 33, 88, 99, 100] 
# 
# new_list = [] 
# def even_num(lst):
#     for num in lst:
#         if num % 2 == 0: 
#             new_list.append(num) 
# 
#     return new_list 
# 
# rslt = even_num(my_list) 
# print("The even numbers are {}".format(rslt)) 
# 
# #Find the even numbers from a list a list comprehension.
# lst = my_list 
# 
# even_number = [num for num in lst if num % 2 == 0]
# print("The even numbers are {}".format(even_number))
# 
# # From C:\ 
# # List comprehension even or odd:
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# even = [num for num in number if num % 2 == 0]
# odd = [num for num in number if num % 2 != 0] 
# print("The even numbers are {}".format(even)) 
# print("The odd numbers are {}".format(odd)) 
# 
# # From E:\ JakeWrite :
# #Find the prime number from the list: 
# 
# #while loop:
# i = 0 
# numbers = [] 
# 
# while i < 6:
#     print("The value of i is {}.".format(i)) 
#     numbers.append(i) 
#     print("The value of numbers is {}.".format(numbers)) 
#     i += 1 
#     print("Now, the value of i is {}.".format(i)) 
# 
# print("The numbers: ") 
# for i in numbers:
#     print(i)
# 
# # Do the same thing using a def function.
# 
# def print_value(test):
#     numbers = [] 
#     for i in test: 
#         print("The value of i is {}.".format(i))
#         numbers.append(i) 
#         print("The value of numbers is {}".format(numbers)) 
#         i += 1 
#         print("Now the value of i is {}.".format(i))
# 
# value = range(0, 6)  
# rslt = print_value(value) 
# print(rslt)
# 
# #Making Decision: 
# print("""
# You entered in a dark room. 
# There are two rooms in it.
# Do you go through door #1 or door #2?
# """)
# door = input("> ") 
# if door == "1":
#     print("There is a bear here eating cheese.") 
#     print("What do you do?") 
#     print("Press 1 to take the cheese.") 
#     print("Press 2 screem at the bear.") 
# 
#     bear = input("> ") 
#     if bear == "1": 
#         print(f"The bear eats your face off. Good job!") 
#     elif bear == "2": 
#         print(f"The bear eats you legs off. Good job!") 
#     else:
#         print("Well, doing {} is probably better.".format(bear)) 
#         print("Bear runs away.") 
# 
# elif door == "2":
#     print("There is a ghost giving you a choice:") 
#     print("Press 1 to take the magic ball.") 
#     print("Press 2 to take the jellaries.") 
#     print("Press 3 to escape out of the room.")
#     ghost = input("> ") 
#     if ghost == "1" or ghost == "2":
#         print("The ghost takes your soul off of your body.")
# 
#     else:
#         print("You get a new life.") 
#         print("You are safe now.") 
# 
# else:
#     print("Stumble around and fall on a knife and die.") 
# 
# #Now let's print something new here. 
# # Guess the number:
# 
# 
# def guess_num(number):
#     
#     guess = 0 
#     while guess != number:
#         guess = int(input("Guess the number for 1-10: ")) 
#         if guess > number:
#             print(f"The number is less than {guess}.") 
#         elif guess < number:
#             print(f"The number is greater than {guess}.") 
# 
#         else:
#              print(f"Your guess {guess} is correct!") 
# 
# rslt = guess_num(3)
# print(rslt) 
# 
# 
# #Branches and Functions:
# from sys import exit 
# 
# # gold room 
# def gold_room():
#     print("This room is full of gold.") 
#     print("How much do you take?") 
# 
#     choice = input("> ") 
#     if '0' in choice or '1' in choice:
#         how_much = int(choice) 
#     else:
#         dead("Man, learn to type a number.") 
#     if how_much < 50:
#         print("Nice! You're not gredy, you win!") 
#         exit(0) 
#     else:
#         dead("You gready bastard!") 
# 
# #bear room 
# def bear_room():
#     print("""There is a bear here.
#           The bear has a bunch of honey.
#           The fat bear is in front of another door.
#           How are you going to move the bear.""")
#     
#     bear_moved = False 
#     
#     while True:
#         choice = input("> ") 
# 
#         if choice == "take honey":
#             dead("The bear looks at you and slaps your face off.") 
#         
#         elif choice == 'taunt bear' and not bear_moved:
#             print("The bear has moved from the door.") 
#             print("You can go through it now.") 
#             bear_moved = True 
#         elif choice == 'taunt bear' and bear_moved:
#             dead("The bear gets pissed of and chews your legs off.") 
#         elif choice == "open door" and bear_moved:
#             gold_room()  
# 
# #cthulhu
# def cthulhu_room():
#     print("Here you see the greatd devil Cthulhu.") 
#     print("He, it, whatever stares at you and you go insane.") 
#     print("Do you flee for your life or eat your head?") 
# 
#     choice = input("> ") 
# 
#     if "flee" in choice:
#         start() 
#     elif "head" in choice:
#         dead("Well that was tasty!") 
#     else:
#         cthulhu_room()  
# # dead 
# def dead(why):
#     print(why, "Good job!") 
#     exit(0) 
# 
# 
# def start():
#     print("You are in a dark room.") 
#     print("There is a door to your right and left.") 
#     print("Which one do you take?") 
#     
#     choice = input("> ") 
# 
#     if choice == "left":
#         bear_room() 
# 
#     elif choice == "right":
#         cthulhu_room() 
# 
#     else:
#         dead("You stumble in a room until you starve.") 
# 
# start() 

#Branches and Functions:

# #gold room:
# def gold_room():
#     print("This room is full of gold.") 
#     print("How much do you take?") 
#     choice = input("> ") 
#     if choice == "0" or choice == "1":
#         how_much = int(input("> "))  
#     else:
#         print("Man, learn to type a number.") 
#     if how_much < 50:
#         print("Nice, you're not gready, you win!") 
#         exit(0) 
#     else:
#         dead("You gready bastard!") 
# 
# #Cthulhu room:
# def cthulhu_room():
#     print("Here you see the great evil Cthulhu.") 
#     print("He stares at you and you go insane.") 
#     print("Do you flee for your life or eat your head?") 
#     flee = False  
#     choice = input("> ") 
#     if "flee" in choice and not flee: 
#         start() 
#     elif "head" in choice or flee:
#         dead("Well that was tasty!") 
#     else:
#         cthulhu_room() 
# #bear room:
# def bear_room():
#     print("There is a bear here.")
#     print("The bear has a bunch of honey.") 
#     print("The fat bear is in front of the door.") 
#     print("How are you going to move the bear?") 
# 
#     bear_moved = False 
#     
#     while True:
#         choice = input("> ") 
#         
#         if choice == "take honey":
#             dead("The bear looks at you and slaps your face off.")
#         elif choice == "taunt bear" and not bear_moved:
#             print("The bear has moved from the door.") 
#             print("You can go through it now.")
#             bear_moved = True 
#         elif choice == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your legs off.")
#         elif choice == "open door" and bear_moved:
#             gold_room() 
# 
# def dead(why):
#     print(why, "Good job!") 
# 
# #start function:
# def start():
#     print("You are in a dark room.") 
#     print("There is a door to the right and left.") 
#     print("Which one do you take?") 
# 
#     choice = input("> ") 
# 
#     if choice == "left":
#         bear_room() 
#     elif choice == "right":
#         cthulhu_room() 
#     else:
#         dead("You stumble in a room until you starve.") 
# 
# start() 
# 
# # Find the Prime Numbers form 1 to 50:
# 
#  
# prime_num = []  
# for num in range(2, 51):
#     is_prime = True 
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False 
#             break
# 
#     if is_prime: 
#         prime_num.append(num) 
# 
# print(prime_num)   
# 
# #range(2, 2): let's see what happens:
# for i in range(2, 3):
#     print("I will do that for you.") 

# #Write a program that asks the user to enter a 
# #number and jprints whether it is even or odd.
# 
# number = int(input("Enter a number to check even or odd: ")) 
# 
# if number % 2 == 0:
#     num = f"The number {number} is an even number." 
# 
# else:
#     num = f"The number {number} is an odd number." 
# 
# print(num) 
# 
# #Sum of Number from 1 to N:
# N = int(input("Enter a number for the sum of it: ")) 
# 
# def sum_num(N):
#     if N == 1:
#         return 1 
#     else:
#         return N + sum_num(N - 1)
# 
# rslt = sum_num(N)  
# print("The sum of the {} is {}.".format(N, rslt))
# 
# # Another aproach for sum of a number:
# number = int(input("Enter a number for the sum of it: ")) 
# 
# sum = 0
# for num in range(1, number + 1):
#     sum += num 
# print("The sum of {} is {}.".format(number, sum))
# 
# # 3. Find the largest Number: 
# # Given a list of numbers [4, 9, 1, 22, 17], 
# # write code to find the largest number. 
# 
# numbers = [-4, -9, -1, -48, -22, -17] 
# 
# def largest_num(numbers):
#     largest = numbers[0]   
#     for num in numbers: 
#         if num > largest: 
#             largest = num  
#     
#     return largest 
# 
# rslt = largest_num(numbers) 
# print("The largest number is {}.".format(rslt))
# 
# #Another approach to find out the largest number.
# #Using max() function: 
# 
# print(f"The largest number is {max(numbers)}.") 

# #4. Check for Prime Number
# #Write a number that takes an integer as an input
# #and checks whether it's a prime number. 
# number = int(input("Enter a number to check whether it's a prime number: ")) 
# 
# if number < 2:
#     print(f"{number} is not a prime number.") 
# else:
# 
#     is_prime = True 
#     for num in range(2, int(number ** 0.5) + 1):
#         if number % num == 0:
#             is_prime = False 
#             break 
# 
#     if is_prime:
#         print(f"{number} is a prime number.") 
#     else:
#         print(f"{number} is not a prime number.")  
# 
# #5. Reverse a String
# #Write a function that takes a string and returns
# #it reversed (e.g., "hello" "olleh") 
# 
# string = input("Enter a word to reverse: ") 
# 
# def reverse_str(string):
#     return string[::-1] 
# 
# rslt = reverse_str(string)
# print(f"Reversed form is \"{rslt}\".")
# 
# # Let's do it manually:
# rev_str = input("Enter a word or sentence to reverse: ") 
# 
# def reversed_str(string):
#     empty_str = " "
#     for char in string:
#         empty_str = char + empty_str 
#         
#     return empty_str 
# 
# rslt = reversed_str(rev_str) 
# # print(f"The reversed string is \"{int(rslt) + 1}\".") 
# print(f"The reversed string is \"{rslt}\".")
# #6. Count Vowels 
# #Write a program to count the number of vowels 
# #in a given string. 
# 
# def count_vowels(sentence):
#     vowels = "AEIOUaeiou"
#     count = 0  
#     for char in sentence: 
#         if char in vowels: 
#             count += 1 
#         
#     return count 
# 
# sen = input("Enter a sentence to count vowels: ") 
# rslt = count_vowels(sen)
# if rslt == 0 or rslt == 1:
#     print(f"There is only {rslt} vowel in the sencente.") 
# else:
#     print("There are {} vowels in the sentence.".format(rslt)) 
# 
# 
# #7. Fibonacci Sequence :
# #Write a function to print the first n numbers
# #of the Fibonacci sequence. 
# 
# def fibonacci(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1 
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2) 
# 
# number = 10 
# print("Fibonacci Sequence: ") 
# for i in range(number + 1):
#     print(fibonacci(i), end=' ') 

# #8. Factorial of a Number 
# #Write a program to calculate the factorial of a 
# #given number using a for loop. 
# 
# n = int(input("Enter a number for its factorial: "))
# fac = 1 
# for i in range(1, n + 1):
#     fac = i * fac 
# 
# print(f"The factorial of the number {n} is {fac}.")  
# 
# #Another approach:
# number = int(input("Enter a number for its factorial: ")) 
# def fac_recurse(num):
#     if num == 1:
#         return 1 
#     else:
#         return num * fac_recurse(num - 1) 
#     
# rslt = fac_recurse(number) 
# print("The factorial of the number {} is {}.".format(n, rslt))


# #9. List of Prime Numbers (1 - 50)
# # Use a loop and logic to store all prime numbers 
# # between 1 and 50 in a list. 
# 
# my_list = [] 
# for number in range(2, 51):
#     is_prime = True 
# 
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break  
# 
#     if is_prime:
#         my_list.append(number) 
# 
# print(my_list) 
# 
# #Given a number N and an array A of N numbers.
# #Print the array in a reversed order. 
# 
# 
# 
# #9. List of Prime Numbers (1 - 50)
# # Use a loop and logic to store all prime numbers 
# # between 1 and 50 in a list. 
# prime_num = [] 
# for num in range(2, 51):
#     is_prime = True 
# 
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False 
#             break 
#     
#     if is_prime:
#         prime_num.append(num) 
# 
# print(f"The prime numbers are {prime_num}.")
# 
# #open a file 
# file_name = input("Ener a file name to read: ") 
# 
# target = open(file_name, 'r') 
# print(f"{file_name}: ")
# content = target.read()  
# print(f"The content of the file:\n{content} ") 
# target.close() 
# 
# #with-as 
# file_name = input("Enter a file name to read: ") 
# 
# with open(file_name, 'r') as target:
#     content = target.read() 
# 
# print(content) 


# #9. List of Prime Numbers (1 - 50)
# # Use a loop and logic to store all prime numbers 
# # between 1 and 50 in a list. 
# prime_numbers = []
# for num in range(2, 51):
#     is_prime = True 
# 
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False 
#             break  
#     
#     if is_prime:
#         prime_numbers.append(num)
# 
# print("The prime numbers are {}.".format(prime_numbers)) 
# 
# #Find the Largest Number
# #Given a list of numbers: [4, 9, 1, 22, 17], write
# #code to find the largest number 
# my_list = [4, 9, 1, 22, 17] 
# 
# largest_num = max(my_list) 
# print(f"The largest number is {largest_num}.")
# 
# #Largest Number with Different approach: manually 
# my_list1 = [4, 9, 1, 22, 17] 
# 
# def largest_num(lst):
#     largest = my_list1[0] 
# 
#     for num in lst: 
#         if num > largest:
#             largest = num 
# 
#     return largest 
# 
# result = largest_num(my_list1) 
# print("The largest number is {}.".format(result)) 

##Count Vowels
##Write a program to count the number of vowels in 
##a given string. 
#a_string = input("Enter a number to see how many\nvowels there are: ") 
#
#def count_vowels(given_str):
#    vowels = "AEIOUaeiou"
#    count = 0 
#    for char in given_str:
#        if char in vowels:
#            count = count + 1 
#
#    return count 
#
#result = count_vowels(a_string)
#print(f"There are {result} vowels in the sentence.") 
#
##Find the prime numbers from 1 to 50: 
#prime_num = []  
#
#for num in range(2, 51):
#    is_prime = True  
#    for i in range(2, int(num ** 0.5) + 1):
#        if num % i == 0:
#            is_prime = False 
#            break 
#    
#    if is_prime:
#        prime_num.append(num) 
#    
#print("The prime numbers from 1 - 50 are {}.".format(prime_num)) 

##Write a fibonacci number sequence:
#user_input = int(input("Enter a number: ")) 
#
#def fibonacci(num):
#    if num == 0: 
#        return 0 
#    if num == 1:
#        return 1 
#    else:
#        return fibonacci(num - 1) + fibonacci(num - 2) 
#
#for i in range(user_input + 1):
#    print(fibonacci(i), end=' ') 
##result = fibonacci(user_input) 
##print("The {}th Fibonacci number is {}.".format(user_input, result))

# #Fibonacci Sequence Another Approach:
# user_input = int(input("Enter a number: ")) 
# 
# def fibonacci_seq(num):
#     sequence = [] 
#     a, b = 0, 1 
#     for i in range(num): 
#         sequence.append(a) 
#         a, b = b, a + b 
# 
#     return sequence 
# result = fibonacci_seq(user_input) 
# print("The fibonacci sequence from 0 to {} is {}.".format(user_input, result)) 
# 
# #reverse a string 
# def reverse_str(word):
#     return word[:: -1]  
# 
# input_word = input("Enter a sentence to reverse: ")
# result = reverse_str(input_word) 
# print("Reversed string: ", result) 
# 
# #reverse a sentence; another approach
# reverse_word = input("Enter a sentence to reverse: ") 
# 
# def reverse(word):
#     reversed_word = " "
#     
#     for char in word: 
#         reversed_word = char + reversed_word  
# 
#     return reversed_word 
# 
# result = reverse(reverse_word) 
# print(result)
# 
# #reverse a big number 
# number = int(input("Enter a number: ")) 
# 
# def reverse_num(num): 
#     reversed_number = 0 
#     while num > 0: 
#         remainder = num % 10 
#         reversed_number = reversed_number * 10 + remainder 
#         num = num // 10 
#     return reversed_number 
# 
# result = reverse_num(number) 
# print(f"The reversed number is {result}.") 

##Extracting a .zip file:
#import zipfile 
#file_name = input("File name to extract: ") 
#
#with zipfile.ZipFile(file_name, 'r') as archive: 
#    archive.extractall()
#
#import os 
#print('Your current working directory: ') 
#print(os.getcwd()) 
#print(os.listdir()) 
#print('.git' in os.listdir())
#
##Check the current working directory and check if
##the folder exists, it not create one. 
#print("Current Folder:", os.getcwd())#print the current directory 
#
#current_folder = input("Name the current folder: ")
#if not os.path.exists(current_folder):#
#    file_name = input("Name the folder: ")
#    os.makedirs(file_name)
#    print("The directory has been created.") 
#
#else:
#    print("The directory already exists.") 

# my_list = ['red', 'black', 'blue', 'green'] 
# my_list.remove('blue') 
# print(my_list) 
# 
# print("Print the first three elements.") 
# my_list.append("yellow") 
# print(my_list[:3]) 
# 
# print("Write a for loop to print each element..:") 
# for i in my_list:
#     print(i, end=', ') 
# print("\n")
# print('apple' in my_list) 
# 
# #Sort the list below in acending order:
# number = [23, 4, 23, 8, 48, 22, 3] 
# num = sorted(number) 
# print(num) 
# 
# #Manually, Bubble Sort:  
# for i in range(len(number)):
#     for j in range(len(number) - i - 1):
#         if number[j] > number[j + 1]:
#             #swap 
#             number[j], number[j + 1] = number[j + 1], number[j] 
# 
# print(number) 
#
##Guess the number:
#import random  
#
#def guess_num(num):
#    random_num = random.randint(1, num) 
#    number = 0 
#    while number != random_num:
#        number = int(input("Guess the number form 1 - 10: ")) 
#        if number < random_num:
#            print(f'{number} is less than the expected number.') 
#        elif number > random_num:
#            print(f"{number} is more than the desired number.") 
#
#    print(f"Congratulations!\n{number} is the correct number.\nYou've guessed it correctly.") 
#
#guess_num = 10 

##Guess the number:
#import random
#def guess_number(x):
# 
#    random_num = random.randint(1, x) 
#    guess_num = 0  
#
#    while guess_num != random_num:
#        guess_num = int(input("Guess the number: ")) 
#        if guess_num < random_num:
#            print(f"It's more than {guess_num}.") 
#        elif guess_num > random_num:
#            print(f"It's less than {guess_num}.")
#
#    print(f"Congratulation! {guess_num} is the correct number.") 
#
#guess_number(10)
#
##let computer guess the number:
#def computer_guess(x):
#    low = 1 
#    high = x 
#    feedback = ''
#    while feedback != 'c':
#        if low != high:
#            guess = random.randint(low, high) 
#        else:
#            guess = low #could also be high 
#        feedback = input(f'Is {guess} too high (H), too low (L), or correct? (C)').lower() 
#
#        if feedback == 'h':
#            high = guess - 1 
#        elif feedback == 'l': 
#            low = guess + 1 
#             
#    print(f"Yay! The computer guessed your number, {guess}, correctly!") 
#
#computer_guess(10)
#
##Computer guesses the number:
#def computer_guess(x):
#    low = 1 
#    high = x 
#    feedback = ''
#    
#    while feedback != 'c': 
#        if low != high:
#            guess = random.randint(low, high) 
#        else:
#            guess = low #it could also be high 
#        
#        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?: ").lower() 
#
#        if feedback == 'h':
#            high = guess - 1 
#        elif feedback == 'l':
#            low = guess + 1 
#
#    print(f"Yay! The computer guessed your number, {guess}, correctly!") 
#
#computer_guess(10) 

##Guess the number:
#import random 
#def guess_number(x):
#    random_number = random.randint(1, x)
#    guess = 0 
#    
#    while guess != random_number:
#        guess = int(input("Guess the number: ")) 
#        if guess > random_number: 
#            print(f"The number is smaller than {guess}.") 
#        elif guess < random_number:
#            print(f"The number is bigger than {guess}.") 
#        
#    print(f"Yay! You have guessed the number, {guess}, correctly.") 
#
#guess_number(10)
#
##let the computer guess the number.
#def computer_guess(x):
#    low = 1
#    high = x 
#    feedback = ''
#
#    while feedback != 'c':
#        if low != high:
#            guess = random.randint(low, high) 
#        else:
#            guess = low 
#        
#        feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)?: ").lower() 
#
#        if feedback == 'h':
#            high = guess - 1 
#        elif feedback == 'l':
#            low = guess + 1 
#
#    print(f"Yay! The computer guessed your number, {guess}, correctly.") 
#
#computer_guess(1000) 


##Sort the list below in asscending order and print it.
#my_list = [22, 8, 43, 23, 3, 18, 5] 
#my_list.sort() 
#print(my_list) 
#
##Using Bubble Sort Method:
#def bubble_sort(lst):
#    item_len = len(lst) - 1 
#
#    for i in range(item_len):
#        for j in range(item_len - i):
#            if lst[j] > lst[j + 1]:
#                lst[j], lst[j + 1] = lst[j + 1], lst[j] 
#            print(lst) 
#
#numbers = [5, 3, 1, 2, 4] 
#bubble_sort(numbers) 
#
##Create a new list containing the squares of numbers
##from 1 to 5 using list comprehension 
#square_num = [x ** 2 for x in numbers] 
#print("The squares of the numbers are: ", square_num) 
#
##Alternative way:
#def square_number(lst):
#    squared = []  
#    for i in lst:
#        squ = i ** 2 
#        squared.append(squ) 
#    return squared 
#
#print(numbers) 
#square = square_number(numbers) 
#print(f"Alternate way: {square}")
#
##Write a Python program to remove duplicate elements 
##from the list below and print the updated list. 
#my_list = [3, 1, 5, 3, 2, 1, 8] 
#rm_dup = list(set(my_list)) 
#print("Duplicates are removed: ", rm_dup) 
#
##Write a python program to find and print the 
##largest number from the list below.
##[10, 45, 2, 99, 23, 78]
#my_list = [10, 45, 2, 99, 78] 
#largest_num = max(my_list) 
#print("The largest number is {}.".format(largest_num)) 
#
##Alternative approach:
#
#def largest_number(num):
#    largest = 0  
#    for i in num:
#        if i > largest:
#            largest = i 
#    return largest 
#
#lar_num = largest_number(my_list) 
#print("Second Approach: {}.".format(lar_num)) 
#
##Find the average number of alist using def and 
##lambda function. 
#
#def average_num(num):
#    average = sum(num) / len(num)
#    return average 
#lst = [2, 22, 14, 18, 88, 3] 
#average_number = average_num(lst) 
#print("The average number is {}.".format(average_number))
#
##Alternate Approach:
#import statistics 
#ave = statistics.mean(lst)
#print("Alter nate approach: {}".format(ave))
#
##lambda function 
#num1 = int(input("Enter the first number: ")) 
#num2 = int(input("Enter the second number: "))
#sum = lambda num1, num2: num1 + num2 
#print(f"The sum of the numbers is {sum(num1, num2)}.") 

# #Find the average number of a llist using def
# # and lambda functions.
# import statistics 
# numbers = [10, 20, 30, 40, 50] 
# average = statistics.mean(numbers) 
# print("The average number is {}.".format(average)) 

# #Alternet Approach 
# def average_number(lst):
#     average = sum(lst) / len(lst) 
#     return average 

# ave = average_number(numbers) 
# print("Second Approach: {}.".format(round(ave))) 

# #Thrid Approach: lambda 
# ave_lam = lambda numbers: round(sum(numbers) / len(numbers))
# print("Third Approach: {}".format(ave_lam(numbers))) 


# #sum of n numbers:
# def sum_n(n):
#     sum = 0 
#     for i in range(1, n + 1):
#         sum += i 
#     return sum 
# result = sum_n(5) 
# print(f"The sum of the 5 is {result}.")


# #Check for prime numbers 

# prime_number = []  
# for num in range(2, 51):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1): 
#         if num % i == 0:
#             is_prime = False 
#             break 
    
#     if is_prime:
#         prime_number.append(num)

# print(prime_number) 

##print even or odd numbers
#def even_odd(num):
#    if num % 2 == 0:
#        print(f"The number {num} is an even number.")
#    elif num % 2 != 0:
#        print(f"The number {num} is an odd number.")
#
#number = int(input("Enter a number for even/odd: ")) 
#even_odd(number) 
#
##Sum of Numbers from 1 to N.
#def sum_numbers(nums):
#    sum = 0
#    for num in range(1, nums + 1):
#        sum += num 
#    return sum 
#number = int(input("Enter a number for a sum of Nth number: "))
#result = sum_numbers(number)
#print("The sum of the numbers of {} is {}.".format(number, result))
#
#
##Find the largest number from a list.
#my_list = [22, 23, 88, 23, 8, 99]
#largest = max(my_list) 
#print(f"The largest number is {largest}.")
#
##Manually:
#def largest_number(num):
#    largest = 0 
#    for number in num:
#        if number > largest:
#            largest = number  
#    return largest 
#
#ints = [22, 23, 88, 23, 8, 99]
#result = largest_number(ints)
#print("The largest number is {}.".format(result))

# #List of Prime Numbers 
# #Use a loop and logic to store all prime numbers between 
# #1 and 50 in a list.
# 
# prime_num = []
# for num in range(2, 51):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False 
#             break
# 
#     if is_prime:
#         prime_num.append(num) 
# 
# print("Prime numbers = {}".format(prime_num))  
# 
# #List of Prime Numbers:
# #Use a loop and logic to store all prime numbers between
# #1 ad 50 in a list.
# 
# prime_num = []
# for num in range(2, 51):
#     is_prime = True 
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0: #if remainders 0, not prime
#             is_prime = False 
#             break 
# 
#     if is_prime:
#         prime_num.append(num)
# 
# print("The Prime Numbers: {}".format(prime_num))
# 
# #Write a program that takes an integer as input and checks
# #whether it's a prime number.
# prime_number = int(input("Enter a number to check whether it is a prime or not: "))
# 
# is_prime = True 
# for num in range(2, int(prime_number ** 0.5) + 1):
#     if prime_number % num == 0:
#         is_prime = False 
#         break 
# 
# if is_prime:
#     print("{} is a prime number.".format(prime_number)) 
# 
# if not is_prime:
#     print("{} is not a prime number.".format(prime_number))
# 
# #Reverse a String
# #Write a function that takes a string and returns it reversed.
# my_str = input("Enter something to reverse: ")
# 
# rever = my_str[::-1]
# print(rever) 
# 
# #Count Vowels
# #Write a program to count the 
# #number of vowels in a given string.
# 
# word = input("Enter a sentence to count vowels: ")
# 
# def count_vowels(vol):
#     vowels = "AEIOUaeiou"
#     count = 0
#     for char in vol:
#         if char in vowels:
#             count += 1
# 
#     return count 
# 
# result = count_vowels(word)
# print("There are {} vowels in the given sentence.".format(result))

##Fibonacci Sequence:
##Write a function to print the first n numbers of the 
##Fibonacci sequence.
#def recursion(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#
#    else:
#        return recursion(n - 1) + recursion(n - 2) 
#
#num = int(input("Enter a number for Febonacci Sequence: "))
##result = recursion(num)
##print("Febonacci sequence: {}".format(result))  
#for i in range(num + 1):
#    print(recursion(i), end=' ')
#print("\n")

##Recursion Method 
##Sum of a number:
#int_num = int(input("Enter an integer for the sum of it: "))
#def sum_num(num):
#    if num == 0:
#        return 0 
#    else:
#        return num + sum_num(num - 1) 
#
#for i in range(int_num + 1):
#    print(sum_num(i), end=' ')  
#
##Factorial of a Number:
## Write a program to calculate the factorial of a given
##number using a for loop.
#fact_num = int(input("\nEnter an integer to see its factorial: "))
#
#def factorial_num(num):
#    if num == 1:
#        return 1 
#    else:
#        return num * factorial_num(num - 1) 
#result = factorial_num(fact_num) 
#print("The factorial of {} is {}.".format(fact_num, result)) 
#
##List of Prime Numbers:
##Use a loop and logic to store all prime numbers between 1
## and 50 in a list.
#
#prime_num = []
#for num in range(2, 51):
#    is_prime = True 
#    for i in range(2, int(num ** 0.5) + 1):
#        if num % i == 0: #if divided by 0, not prime 
#            is_prime = False 
#            break 
#
#    if is_prime:
#        prime_num.append(num) 
#print("\nThe following are the prime numbers: \n{}".format(prime_num))

##Reverse a string:
#my_str = input("Enter anything to reverse: ") 
#def reverse_str(x):
#    return x[::-1] 
#
#result = reverse_str(my_str) 
#print("\nThe reversed thing: {}".format(result))
#
##swap two variables:
#a = 5
#b = 10
#a, b = b, a  
#print("a = {} and b = {}".format(a, b))
#
##Convert temperature from Celsius to Fahrenheit 
##Formula: F = C * 9/5 + 32 
#def celsius_to_fahrenheit(cel):
#    fehrenheit = cel * 9/5 + 32 
#    return fehrenheit 
#
#celsius = int(input("Enter Celsius to convert to Fahrenheit: "))
#result = celsius_to_fahrenheit(celsius)
#print("So, {} celsius = {} fahrenheit".format(celsius, result))

##Count Vowels in a string:
#val = input("Enter a sentence to count vowels: ")
#
#def count_vowels(x):
#    count = 0 
#    vowels = "AEIOUaeiou"
#    for char in x:
#        if char == vowels:
#            count += 1
#    return count 
#
#result = count_vowels(val) 
#print("There are {} vowels in the sentence.".format(result))  
#
##read a whole file then write to the file:
#from sys import argv 
#script, file_name = argv #user input 
#
#def read_whole_file(x):
#    print(x.read()) 
#
#def rewind(x):
#    x.seek(0) 
#
#def print_a_line(print_line, x):
#    print(print_line, x.readline()) 
#
#target = open(file_name, 'r') #first open a file 
#read_whole_file(target) 
#
#rewind(target) #take the cursor at the begining of the file
#
#for i in range(0, 6):
#    print_a_line(i, target) 

# #Find the average number of a list using def and lambda func.
# my_list = [10, 20, 30, 40, 50, 60]
# 
# def average(x):
#     ave = sum(x) / len(x)
#     return ave 
# 
# result = average(my_list) 
# print(result)  
# 
# #print the largest number from a list.
# def largest_num(f):
#     largest = max(f)
#     return largest 
# print(largest_num(my_list)) 
# 
# def lar(f):
#     largest = 0
#     for num in f:
#         if num > largest:
#             largest = num 
#     return num 
# 
# result = lar(my_list) 

#from sys import exit 
#
#def start():
#    print("""
#    You've entered in a dark room.
#    There is a door to your left and right.
#    Which one do you take?
#
#    """)
#    choice = input('> ') 
#
#    if choice == "left":
#        bear_room() 
#    elif choice == "right":
#        monster_room() 
#    else:
#        dead("You stumble around the dark room until you die.") 
#
#def dead(why):
#    print(why, "Good Job!") 
#    exit(0)
#
#def monster_room():
#    print("The monster, whoever sees it goes insane.") 
#    print("Do you flee from him or eat your head?")
#
#    choice = input("> ") 
#
#    if 'flee' in choice:
#        start()
#    elif 'head' in choice:
#        dead("That was tasty!")
#
#def bear_room():
#    print("""
#    There is a bear here.
#    The bear has a bunch of honey.
#    The fat bear is in front of another door.
#    How will you move the bear?
#    """)
#     
#    bear_moved = False 
#
#    while True: 
#        choice = input("> ")
#        if choice == "take honey":
#            print("The bear looks at you and slaps your face off.")
#        elif choice == "taunt bear" and not bear_moved:
#            print("The bear has moved from the door.")
#            print("You can go through the door now.") 
#            bear_moved = True 
#        elif choice == "taunt bear" and bear_moved:
#            dead("The bear gets pissed off and slaps you legs off.")
#        elif choice == "open door" and bear_moved:
#            gold_room() 
#        else:
#            dead("You stuck forever in the bear room.") 
#
#def gold_room():
#    print("""
#    The room is full of gold.
#    How much do you take?
#    """)
#    choice = input("> ") 
#
#    if '0' in choice or '1' in choice:
#        how_much = int(choice) 
#    else:
#        print("Man try to write something.") 
#    
#    if how_much < 50:
#        print("Nice, you're not gready, you win!") 
#        exit(0) 
#    else:
#        dead("You gready bastard!") 
#start()


#from sys import exit 
#
#def start():
#    print("""
#    You entered in a dark room.
#    There is a door to your left and right.
#    Which one do you take?
#    """)
#    choice = input("> ") 
#
#    if choice == "left":
#        bear_room()
#    elif choice == "right":
#        monster_room() 
#    else:
#        dead("You stumble in the dark room and die.") 
#
#def dead(why):
#    print(why, "Great job!")
#    exit(0) 
#
#def bear_room():
#    print("""
#    There is a bear in front of the door.
#    The bear has a bunch of honey.
#    How do you move the bear?
#    """)
#
#    bear_moved = False 
#    while True:
#        choice = input("> ")
#        if choice == "take honey":
#            dead("The bear looks at you and slaps your head off.")
#        elif choice == "taunt bear" and not bear_moved:
#            print("The bear moved and you can go through the door.") 
#            bear_moved = True 
#        elif choice == "taunt bear" and bear_moved:
#            dead("The bear gets pissed off and chews your legs off.") 
#        elif choice == "open door" and bear_moved:
#            gold_room() 
#        else:
#            print("You stay forever in front of the bear room.") 
#
#
#def monster_room():
#    print("""
#    You have entered into the monster's room, you look at him and go insane.
#    Do you flee or eats you head?
#    """)
#    choice = input("> ") 
#
#    if 'flee' in choice:
#        start()
#    elif 'eat head' or 'head' in choice:
#        dead("Tasty!") 
#
#def gold_room():
#    print("""
#    You have entered into a room that is full of gold.
#    How much do you take?
#    """)
#    choice = input("> ")
#    if '1' in choice or '0' in choice:
#        how_much = int(choice) 
#    else:
#        print("Man, try to enter a number.")
#    if how_much < 50:
#        dead("You are not gready. You successfully finish the game.")
#    else:
#        print("You gready bastard!") 
#        exit(0)
#start()
 
#from sys import exit
#
#def start():
#    print("""
#    You are in a dark room.
#    There is a door to your right and left.
#    Which one do you take?
#    """)
#    choice = input("> ") 
#
#    if choice == "right":
#        bear_room() 
#    elif choice == "left":
#        monster_room()
#    else:
#        dead("You stumble around the room and die starving.")
#
#def dead(why):
#    print(why, "Great job!")
#    exit(0) 
#
#def bear_room():
#    print("""
#    There is a bear in front of the door.
#    The bear has a bunch of honey.
#    How do you move the bear?
#    """)        
#
#    choice = input("> ") 
#    bear_moved = False
#    while True:
#        if choice == "take honey":
#            dead("The bear looks at you and slaps your face off.")
#        elif choice == "taunt bear" and not bear_moved:
#            print("The bear has moved.\nYou can go through it now.")
#            bear_moved = True 
#        elif choice == "taunt bear" and bear_moved:
#            dead("The bear gets pissed off and chews you legs off.") 
#        elif choice == "open door" and bear_moved:
#            gold_room()
#        else:
#            print("You are stuck and the bear may eat you up any time.") 
#
#start()

#from sys import exit 
#
#def gold_room():
#    print("""
#    The room is full of gold.
#    How much do you take?
#    """)
#    choice = input("> ") 
#
#    if '0' in choice or '1' in choice:
#        how_much = int(choice) 
#    else:
#        print("Man try to enter a number.") 
#    if how_much < 50:
#        print("Nice! You are not greedy. Well done!") 
#        exit(0) 
#    else:
#        dead("You gready bastard!") 
#
#def bear_room():
#    print("""
#    There is a bear in front of the room with a bunch of honey.
#    How do you move the bear?
#    """)
#    bear_moved = False  
#
#    while True:
#        choice = input("> ") 
#        if choice == "take honey":
#            dead("The bear looks at you and slaps your face off.") 
#        elif choice == "taunt bear" and not bear_moved:
#            print("The bear has moved from the door.")
#            print("You may go through it now.")
#            bear_moved = True
#        elif choice == "taunt bear" and bear_moved:
#            dead("The bear gets pissed off and chews your legs off.")
#        elif choice == "open door" and bear_moved:
#            gold_room() 
#        else:
#            print("""
#            You are stuck in the bear room the bear might kill you any time.
#            """)
#
#def monster_room():
#    print("""
#    There is a monster in the room, if he stares at you\n you go insane.\nDo you flee or eat you head?
#    """)
#    choice = input("> ")
#    emh = "eat my head"
#    eh = "eat head"
#    if choice == "head" or choice == emh or choice == eh:
#        dead("That was tasty.")
#    elif choice == "flee":
#        start()
#    else:
#        monster_room() 
#
#def dead(why):
#    print(why, "Great job!") 
#    exit(0) 
#
#def start():
#    print("""
#    You are in a dark room.
#    There is a room on your left and right.
#    Which one do you take?
#    """)
#    choice = input("> ") 
#    
#    if choice == "left":
#        bear_room()
#    elif choice == "right":
#        monster_room() 
#    else:
#        dead("You stamble in the room until you die.") 
#
#start() 

#from sys import exit 
#
#def start():
#    print("You are in a dark room./nThere is a door on you left and right.\nWhich one do you take?")
#    choice = input("> ")
#    
#    if choice == "left":
#        bear_room()
#    elif choice == 'right':
#        monster_room() 
#    else:
#        dead("You stumble in the room until you die.")
#
#def dead(why):
#    print(why, "Great job!")
#    exit(0)
#
#def bear_room():
#    print("There is a bear in front of the door with a bunch of honey.\nHow will you move the bear?")
#
#    bear_moved = False 
#    while True:
#        choice = input("> ")
#
#        if choice == "take honey":
#            dead("The bear looks at you and slaps you face off.")
#        elif choice == "taunt bear" and not bear_moved:
#            print("The bear moved and you can go through it now.")
#            bear_moved = True 
#        elif choice == "taunt bear" and bear_moved:
#            dead("The bear gets pissed off and chews you legs off.") 
#        elif choice == "open door" and bear_moved:
#            gold_room() 
#        else:
#            dead("The bear somehow eats you up.") 
#
#def gold_room():
#    print("The room is full of gold. How much do you take?")
#
#    choice = input("> ") 
#
#    if '1' in choice or '0' in choice:
#        how_much = int(choice) 
#    else:
#        dead("Man, try to enter a number.") 
#    
#    if how_much < 50:
#        print("Well done! You are not greedy. You win!") 
#        exit(0)
#    else:
#        dead("You greedy bastard!") 
#
#def monster_room():
#    print("There is a monster, if stares at you, you go insane.")
#    print("Do you flee or eat your head?")
#    choice = input("> ") 
#
#    if choice == "flee":
#        star()
#    elif choice == "eat head":
#        dead("That was tasty!") 
#    else:
#        monster_room()
#
#start()

# things = "Table phone glass pen eight"
# sp_things = things.split(" ")
# more_items = ['Goava', "Mango", "Vice", "Below", "Cabin", "Michael", "Molly"]
# 
# while len(sp_things) != 10:
#     new_item = more_items.pop() 
#     print("Adding: ", new_item)
#     sp_things.append(new_item)
#     print("We have {} item now.".format(len(sp_things))) 
# 
# print("There we go: ", sp_things)
# print("Let's do something with the \'sp_things\'.") 
# 
# print("The second element: {}".format(sp_things[1]))
# print("The first item: {}".format(sp_things[0]))
# print("A random element: {}".format(sp_things.pop()))
# print("Let\'s see the elements without brackets: {}.".format(", ".join(sp_things)))
# print("Let\'s use the same thing with a pound/hash sign (#): {}".format(sp_things[2:6])) 
# 
# 
# # Another approach of the above code:f
# words = "All things are new"
# split_words = words.split()
# more_words = ["time", "Cat", "bread", "Rony", "Peter", "orenge ", "mat", "bat", "lady"]
# 
# while len(split_words) != 10:
#     new_item = more_words.pop()
#     print("Adding: ", new_item) 
#     split_words.append(new_item)
#     print("There are {} items now.".format(len(split_words))) 
# 
# print("Let's do something with split_words: ")
# 
# print("Let's print the first element: ", split_words[0])
# print("Second 3rd element: {}".format(split_words[2])) 
# print("All elements: {}".format(", ".join(split_words))) 
# print("Some of the elements: {}".format(" #".join(split_words[2:6])))
# 
# 
# #10 examples of things in the real world that would 
# #fit in a list. 
# fruits = ["kiewi", "mango", "strawberry", "lichi"]
# for fruit in fruits:
#     print(f"I like {fruit}.")
# 
# #2. 
# tasks = ['read books', 'revision', 'goin to office', "listening to music"]
# for task in tasks:
#     print("Today's task: {}.".format(task))
# 
# #3.
# car_brands = ["Toyota", "Ford", "Tesla", "Honda", "Kia", "Audi", "Mercedes", "Nissan"]
# for brand in car_brands:
#     if brand.startswith("T"):
#         print("I use {}.".format(brand))
# 
# #4.
# colors = ["red", 'yellow', 'black', 'blue', 'green']
# for color in colors:
#     print(color) 
# 
# #5.
# favorite_songs = ["Litle Miss Muffet", "The World Between Us", "Perfect"]
# for song in favorite_songs:
#     print("My favorite song is {}.".format(song))
# 
# #6. 
# Book_title = ["Master Your Emotions", "How to read faster"]
# for title in Book_title:
#     print("Favorite book is {}.".format(title)) 
# 
# #7.
# city_name = ["Texas", "New York", "Missorrie", "Messachussets"]
# for city in city_name:
#     print(city) 
# 
# #8.
# grocery_list = ["Tomato", "eggplant", "okra", "spinach"]
# for veggi in grocery_list:
#     print(veggi)
# 
# #9.
# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fridy', "Saturday"]
# for day in days:
#     print(day)
# 
# #10.
# visit_country = ["USA", "Australia", "Germany", "Netherland", "China", "Japan"]
# for country in visit_country:
#     print("I want to visit {}.".format(country)) 
# 
# vegetables = ["eggplant", "cucumber", "onion", 'pumkin']
# veggi = 0
# 
# while veggi < len(vegetables):
#     print(f"I need to buy: {vegetables[veggi]}.") 
#     veggi += 1 
# 
# favorite_books = ["Time Magazine", "Master You Emotion", "Junior English"]
# books = 0 
# while books < len(favorite_books):
#     print(f"My favorite book is {favorite_books[books]}")
#     books += 1 

#mystuff = {'apples': "I am apples."} 
#print(mystuff['apples']) 
#
#
#import mystuff 
#mystuff.apple() 
#
#print(mystuff.tangerine) 
#
##7/26/2025 #Modules are like dictionaries #Classes are like dictionaries 
#class MyStuff(object):
#
#    def __init__(self):
#        self.tangerine = "And now a thousand years between" 
#
#    def apple(self):
#        print("I AM CLASSY APPLES.") 
#
#thing = MyStuff()
#thing.apple() 
#print(thing.tangerine) 
#
#
##Make of your own 
#class demo(object):
#
#    def __init__(self):
#        self.a_sentence = "I love to code."
#
#    def addi(self, num1, num2):
#        return num1 + num2 
#
#result = demo() #instantiate the class
#print(result.addi(3, 2)) # call the method
#print(result.a_sentence) #access the instance variable 
#
##let's create another one
#class fruits(object):
#    
#    def __init__(self):
#        self.fruit = "Mango is a name of a fruit."
#
#    def multiply(self, num1, num2):
#        return num1 * num2 
#
#rslt = fruits() #instantiate the class
#print(rslt.multiply(3, 4)) #called the method 
#print(rslt.fruit) #access the instance variable 
#
#class MyClass:
#    
#    def say_hello(self):
#        print("Hello!") 
#
#rslt = MyClass() #instantiation of the class
#print(rslt.say_hello()) #calls the method 
#
##Exercise: 40 
#class Song(object):
#
#    def __init__(self, lyrics): #__init__() carries the data
#        self.lyrics = lyrics 
#
#    def sing_me_a_song(self): #Method
#        for line in self.lyrics:
#            print(line) 
#        
#happy_bday = Song([
#    "Happy birthday to you",
#    "I don't want to get sued",
#    "So I'll stop right there"
#])
#
#bulls_on_parade = Song([
#    "They rally around tha family",
#    "With pockets full of shells"
#])
#
#happy_bday.sing_me_a_song() 
#bulls_on_parade.sing_me_a_song() 
#
#class Song(object):
#
#    def __init__(self):
#        self.lyrics = [
#            "There is a ship;",
#            "Floating in the sea.",
#            "Captain of the ship;",
#            "James Cook."
#        ]
#    
#    def sing_me_a_song(self):
#        for line in self.lyrics:
#            print(line) 
#
#sea = Song() #instantiate the class 
#sea.sing_me_a_song() 
#
##Exercise:40 
#class Song(object):
#
#    def __init__(self, lyrics):
#        self.lyrics = lyrics 
#
#    def sing_me_a_song(self):
#        for line in self.lyrics:
#            print(line) 
#
#happy_bday = Song([
#    "Happy birthday to you!",
#    "Happy birthday to you!",
#    "Happy birthday to you!", 
#    "Dear Mcanzie." 
#])
#wish = Song([
#    "Wish you a very long and happy life.",
#    "Wish you be a great coder someday."
#])
#
#happy_bday.sing_me_a_song() 
#wish.sing_me_a_song() 

#Write a python program to reverse a list without 
#using reverse() or slicing. (Bonus Challenge)
# def reverse_a_list(arg1):
#     length = len(arg1)
#     the_list = len(arg1)
#     for num in str(the_list):
#         for j in str(the_list) - num -1:
#             j[0], j[-1] = j[-1], j[0] 
# 
#     return arg1 
# 
# my_list = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# result = reverse_a_list(my_list)
# print("Original list: ", my_list)
# print("Reversed list: ", result) 

class my_class(object):
    def __init__(self):
        self.tangerine = "Are you there?"

    def apple(self):
        print("Learn Python The Hard Way 3.")

thing = my_class() #An object or instance  
thing.apple() 
print(thing.tangerine) 

#reverse a list:
def reverse_list(f):
    return f[:: -1] 

my_list = ['orange', 'cat', 'yellow', 'bag', 'rat', 'bat']
rslt = reverse_list(my_list) 
print(rslt)

print(reversed(my_list)) 

#Sum of Numbers from 1 to N
#Write a program that takes a number N and prints the sum 
#of all numbers from 1 to N.
a_num = int(input("Enter a number to know the sum of it: "))

def sum_num(num):
    sum = 0 
    for i in range(0, num + 1):
        sum += i 
    return sum 

reslt = sum_num(a_num) 
print(f"The sum of the number is {reslt}.")     

#Use a loop and logic to store all prime numbers between 
#1 and 50 in a list.

prime_numbers = [] 
is_prime = True 
for i in range(2, 51):
    for j in range(2, int(i ** 0.5) + 1):
        if i % 2 == 0:
            is_prime = False
            break 

if is_prime:
    prime_numbers.append(i)

print(prime_numbers)  