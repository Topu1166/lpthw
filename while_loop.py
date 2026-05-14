# ##### Bro Code: ############
# name = input("Enter your name: ").title()

# while name == "":
#     print('You did not enter your name: ') 
#     name = input("Enter your name: ").title() 

# print("You name is {}.".format(name)) 

# #### Age ####
# age = int(input("Enter you age: ")) 

# while age < 1:
#     print("Age can not be negative.") 
#     age = int(input("Enter you age: ")) 

# print('You are {} years old.'.format(age)) 

# ########### Numbers from 1 - 10 ###############
# num = int(input("Enter your number (1 - 10): ")) 

# while num <= 0 or num > 10:
#     print("The number {} is not valid.".format(num)) 
#     num = int(input("Enter your number (1 - 10): ")) 

# print('Your number is {}.'.format(num)) 

# #### Food ################################ Food ##################
# food = input("Enter a food you like (q to quit): ").title() 
# foods = []

# while not food == 'Q':
#     foods.append(food)
#     print("You like {}.".format(food)) 
#     food = input("Enter a food name you like (q to quit): ").title()

# ####### Applying f-string using .join() method ################
# print(f"So, you said you like {', '.join(foods)}")

# ######### Applying .format() method using .join() method ##########
# print("So, you said you like {}.".format(', '.join(foods)))

# print("Bye!") 

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

# # Guess the Number-Game: #########################################################
# import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0 
#     while guess != random_number:
#         guess = int(input("Enter a number: "))
#         if guess < random_number:
#             print("Sorry! Guess again. Too low.")
#         elif guess > random_number:
#             print("Sorry! Guess again. Too high.") 
#     print("The number {} is correct.".format(guess))

# guess(10) 

# Enter your password:

# def result(password):

#     x = 0 

#     while x != password:

#         x = int(input("Enter your password: "))

#         if x != password:
#             print("Incorrect password. Try again!") 

#     print("You have successfully logged in.") 

# result(123456)

# # Encoding a text
# # text = "This is the text to encode."
# from sys import argv
# script, file_name = argv
# in_file = open(file_name, 'r', encoding='utf-8') 

# read_file = in_file.readline()
# in_file.close()

# garbled_text = read_file.encode("utf-8").decode("utf-16", errors='ignore') 

# print("Garbled_text= {}".format(garbled_text))


