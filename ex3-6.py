# #Exercises 1 and 2 are printing and commenting out :
# # Exercise 3 : 
# print("I will count my chickens: ")
# print("Hens", (30 + 40) / 5.0)
# print("Roosters", 100 - 25 * 3 % 4)
# print("Now I will count the eggs: ")
# print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# print("Is it true that 3 +2 < 5 - 7?")
# print(3 + 2 < 5 - 7)
# print("What is 3 + 2?", 3 + 2)
# print("What is 5 - 7?", 5 - 7)
# print("Oh, that's why it's False.")
# print("how about some more")
# print("Is it greater?", 5 > -2)
# print("It it greater or equal?", 5 >= 2)
# print("Is it less or equal?", 5 <= -2)

# #Exercise 4 : 
# cars = input("How many cars are there? : ")
# drivers_available = input("How many drivers are there? : ")
# seats_per_car = 4.0
# passengers = input("How many passengers are there today? : ")
# car_driven = int(drivers_available)
# cars_not_driven = int(cars) - car_driven
# carpool_capacity = seats_per_car * car_driven
# average_passengers_per_car = int(passengers) / car_driven
# print("There are", cars, "cars available today.")
# print("There are", drivers_available, "drivers available today.")
# print(car_driven, "cars are going to be driven today.")
# print(cars_not_driven, "cars are not going to be driven today.")
# print("There are", passengers, "passengers available today.")
# print("But we can carpool", carpool_capacity, "passengers today.")
# print("We can put about", average_passengers_per_car, "people in each car.") 

# #Exercise 5:
# my_name = "Zed A. Shaw"
# my_age = 35 # not a lie
# my_height = 74 # inches 
# my_weight = 180 # lbs
# my_eye = "blue"
# my_teeth = "white"
# my_hair = "brown"
# print("Let's talk about", my_name)
# print(f"He is {my_height} inches tall.")
# print(f"He is {my_weight} pounds heavy.")
# print(f"Actually that's not too heavy.")
# print(f"He's got {my_eye} eyes and {my_hair} hair.")
# print(f"His teeth are usually {my_teeth} depending on the coffee.")
# #This line is tricky, try to get it exactly right
# total = my_age + my_height + my_weight 
# print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.") 

# #Exercise 6:
# types_of_people = 10
# x = f"There are {types_of_people} types of people."
# binary = "binary"
# do_not= "don't"
# y = f"Those who know {binary} and those who {do_not}."
# print(x)
# print(y)
# print(f"I said: {x}")
# print(f"I also said: {y}")
# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! {}"
# print(joke_evaluation.format(hilarious)) #.format() is a kind of format
# w = "This is the left side of..."
# e = "a string with a right side."
# print(w + e) 

# #Exercise 7:
# print("Mary had a little lamb.")
# print("Its fleece was white as {}.".format('snow'))
# print("And everywhere that Mary went.")
# print("." * 10) # what'd that do?
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r" 
# # watch end = ' ' at the end. Try removing it to see what happens 
# print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# print(end7 + end8 + end9 + end10 + end11 + end12)

# #Exercise 8:
# formatter = "{} {} {} {}"
# print(formatter.format(1, 2, 3, 4))
# print(formatter.format("one", "two", "three", "four"))
# print(formatter.format(True, False, False, True))
# print(formatter.format(formatter, formatter, formatter, formatter))
# print(formatter.format("Try your", "own text here", "Maybe a poem", "Or a song about fear.\n\n"))

# #Exercise 9: Page: 32
# #Here's some new strange stuff, remember type it exactly.
# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "\nJan.\nFeb.\nMar.\nApr.\nMay.\nJun.\nJul.\nAug.\nSept.\nOct.\nNov.\nDec."
# print("Here are the days: ", days)
# print("Here are the months: ", months)
# print("""
# There's something going on here.
# With the three doublepquotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.      
# """)

# #Exercise 10: Escape Sequences: 
# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split \non a line."
# backslash_cat = "I'm \\ a \\ cat."
# fat_cat = """
# I'll do a list:
# \t* Cat Food
# \t* Fishies
# \t* Catnip\n\t*  Grass
# """
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat) 

# Exercise: 11
# print("How old are you?", end=' ')
# age = input()
# print("How much do you weigh?", end=' ')
# weight = input()
# print("How tall are you?", end=' ')
# height = input()
# print(f"So, you're {age} years old, {weight} kg heavy, and {height} feet tall.")

# #Exercise 12:
# age = input("How old are you?: ")
# weight = input("How much do you weigh?: ")
# height = input("How tall are you?: ")
# print(f"So, you're {age} years old, {weight} kg heavy, and {height} feet tall.")

# #Exercise 13:
# from sys import argv
# # read the WYSS section for how to run this
# script, first, second, third = argv
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# #Exercise 14:
# from sys import argv
# script, user_name = argv
# prompt = '> '
# print(f"Hi {user_name}, I'm the {script} script.")
# print(f"I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)
# print(f"Where do you live {user_name}?")
# lives = input(prompt)
# print("What kind of computer do you have?")
# computer = input(prompt)
# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}. Not sure where that is.
# And you have a {computer} computer. Nice.      
# """)

# #Exercise 15: Reading from a file using argv and input :
# from sys import argv 
# script, filename = argv 
# txt = open(filename)
# print(f"Here's your file {filename}:")
# print(txt.read())
# print("Type the filename again:")
# file_again = input("> ")
# txt_again = open(file_again) 
# print(txt_again.read())

# #Exercise 16: Reading and Writing Files:   read, write, truncate, readline, close, seek(0):
# from sys import argv 
# script, filename = argv 
# print(f"I am going to erase the {filename}.")
# print("If you do not want that, hit Ctrl-C (^C)")
# print("If you do want that, hit RETURN/ENTER.")
# input("?")
# print("Opening the file....")
# target = open(filename, 'w')
# print("Truncating the file. Goodbye!")
# target.truncate()
# print("Now I'm going to ask you for three lines.")
# line1 = input("Line 1: ")
# line2 = input("Line 2: ")
# line3 = input("Line 3: ")
# print("Now I'm going to write these to the file.")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
## target.write(f"{line1}\n{line2}\n{line3}\n")
# print("And finally, we close it.")
# target.close()

# #Exercise 17: More Files: Copying a file from one to another:
# from sys import argv 
# from os.path import exists 
# script, from_file, to_file = argv 
# print("We are going to copy {from_fiel} to {to_file}.")
# in_file = open(from_file, 'r')
# in_data = in_file.read() 
# print(f"The input file is {len(in_data)} bytes long.")
# print(f"Does the input file exist? {exists(to_file)}.")
# print("Ready, hit Enter if you want to continue, hit Ctrl-c to abort.")
# input("?")
# out_data = open(to_file, 'w')
# out_data.write(in_data)
# print("Alright, all done!")
# out_data.close()
# in_file.close() 
# #Copying a file from one to another: ###########################
# from sys import argv
# from os.path import exists
# script, from_file, to_file = argv
# # Open the input file, read its contents, and close it
# with open(from_file, 'r') as in_file:
#     in_data = in_file.read()
# # Open the output file, write the contents, and close it
# with open(to_file, 'w') as out_file:
#     out_file.write(in_data)
# print(f"Does the file exist? {exists(to_file)}")

# #Exercise 18: Names, Variables, Code, Functions: 
# # this one is like your scripts with argv 
# def print_two(*args):
#     arg1, arg2 = args 
#     print(f"arg1: {arg1}, arg2: {arg2}")
# #ok, that *args is actually pointless, we can juest do this 
# def print_two_again(arg1, arg2):
#     print(f"arg1: {arg1}, arg2: {arg2}")
# # this just takes one argument 
# def print_one(arg1):
#     print(f"arg1: {arg1}")
# # this one makes no arguments 
# def print_none():
#         print("I got nothin'.")
# print_two("Zed", "Shaw")
# print_two_again("Zed", "Shaw")
# print_one("First!")
# print_none() 

#Exercise 19: Functions and Variables: 
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print(f"You have {cheese_count} cheeses!")
#     print(f"You have {boxes_of_crackers} boxes of crackers!")
#     print(f"Man that's enough for a party!")
#     print("Get a blanket.\n") 

# print("We can just give the function numbers directly: ") 
# cheese_and_crackers(20, 30) 

# print("OR, we can use variables from our script:") 
# amount_of_cheese = 10 
# amount_of_crackers = 50 

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)

# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# #Exercise 20: Functions and Files: (seek(), readline(), and read()): 
### Reading a file's lines one by one:
# from sys import argv 
# script, input_file = argv #########Taking input of a file
# def print_all(f):
#     print(f.read())  ####### prints the whole file.
# def rewind(f): #### rewind means starting point
#     f.seek(0)  ###### Moves the read/write location to the begining of the file
# def print_a_line(line_count, f):
#     print(line_count, f.readline())#we could use "end=''" to escape the gaps as by default there is \n for each line.
# current_file = open(input_file) 
# print("First let's print the whole file:\n") 
# print_all(current_file) 
# print("Now let's rewind, kind of like a tape.") 
# rewind(current_file) 
# print("Let's print three lines: ") 
# current_line = 1 
# print_a_line(current_line, current_file)
# current_line = current_line + 1 
# print_a_line(current_line, current_file)
# current_line = current_line + 1 
# print_a_line(current_line, current_file) 

# #Exercise 21: Functions Can Return Something: 
# def add(a, b):
#     print(f"ADDING {a} + {b}")
#     return a + b 
# def subtract(a, b):
#     print(f"SUBTRACTION {a} - {b}") 
#     return a - b 
# def multiply(a, b):
#     print(f"MULTIPLY {a} * {b}")
#     return a * b 
# def divide(a, b):
#     print(f"DIVIDING {a} / {b}") 
#     return a / b 
# print("Let's do some math with just functions!") 
# age = add(30, 5) #A function is stored in a string. 
# height = subtract(78, 4)
# weight = multiply(90, 2) 
# iq = divide(100, 2) 
# print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") 
# #A puzzle for the extra credit, type it in anyway. 
# print("Here is a puzzle.") 
# what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) 
# print("That becomes: ", what, "Can you do it by hand?") 

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

# # Math from Bob:
# # A cake costs 75 taka, chocolate 45 for each(1) piece,
# # I have 900 taka in total without any expence, 
# # cake = 8 piece purchased. How many candy can you buy with the rest of the money?
# # How much money would I have after the expense. 
# def calculate_candies(total_money, cake_price, cake_quantity, chocolate_price):
#     # Calculate total expense for cakes
#     cake_expense = cake_price * cake_quantity
    
#     # Calculate remaining money after purchasing cakes
#     remaining_money = total_money - cake_expense
    
#     # Calculate the number of candies you can buy with the remaining money
#     candy_quantity = remaining_money // chocolate_price
    
#     # Calculate the money left after buying candies
#     money_left = remaining_money % chocolate_price
    
#     return candy_quantity, money_left

# # Define the given values
# total_money = 900
# cake_price = 75
# cake_quantity = 8
# chocolate_price = 45

# # Call the function and get the results
# candy_quantity, money_left = calculate_candies(total_money, cake_price, cake_quantity, chocolate_price)

# # Print the results
# print("Number of candies you can buy:", candy_quantity)
# print("Money left after buying candies:", money_left)

# #Quize_game: 
# play = input("Do you like to play the game?: \n> ").title().strip() 
# if play == 'Yes':
#     print("Ok! Let's play it.") 
# else:
#     print("The game has been terminated.") 
#     quit() 
# score = 0
# #Question: 1
# answer = ("Lion") 
# question = input("Which animal is known as the king of the jungle?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1
# else: 
#     print("Incorrect!") 
# #Question: 2
# answer = ("Dhaka") 
# question = input("What is the capital of Bangladesh?: \n> ").title()
# if question == answer:
#     print("Correct!")
#     score += 1 
# else: 
#     print("Incorrect!") 
# #Question: 3
# answer = "Eight"  
# question = input("How many legs does a spider have?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1
# elif question == "8":  
#     print("Correct!") 
#     score += 1
# else: 
#     print("Incorrect!") 
# #Question: 4
# answer = ("Red And Green") 
# question = input("What are the colors of Bangladesh's flag?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1
# elif question == "Green And Red".title(): 
#     print("Correct!")
#     score += 1
# else: 
#     print("Incorrect!") 
# #Question: 5
# answer = ("Hot") 
# question = input("What is the opposite of cold?: \n> ").title()
# if question == answer:
#     print("Correct!")
#     score += 1  
# else: 
#     print("Incorrect!") 
# #Question: 6
# answer = ("Heart") 
# question = input("What beats in your body?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1
# else: 
#     print("Incorrect!") 
# #Question: 7
# answer = ("Brain") 
# question = input("What does make you think?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1
# elif question == "Mind":
#     print("Correct!") 
#     score += 1
# else: 
#     print("Incorrect!") 
# #Question: 8
# answer = ("Whale") 
# question = input("What is the biggest animal in the world?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1 
# elif question == "Blue Whale":
#     print("Correct!")
#     score += 1
# else: 
#     print("Incorrect!") 
# #Question: 9
# answer = ("Jackfruit") 
# question = input("What is the national fruit in Bangladesh?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1 
# elif question == "Jack Fruit":
#     print("Correct!") 
#     score += 1
# else: 
#     print("Incorrect!") 
# #Question: 10
# answer = ("Central Processing Unit") 
# question = input("What does CPU stand for?: \n> ").title()
# if question == answer:
#     print("Correct!") 
#     score += 1 
# else: 
#     print("Incorrect!") 
# print(f"You have got {score} marks out of 10.") 


# #Exercise 24:
# #Escapes:
# print("Let's practice everything.")
# print('You\'d need to know \'bout escapes with \\ that do:') 
# print('\n newlines and \t tabs.') 

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love nor comprehend passion from intuition 
# and requires an explanation
# \n\t\twhere there is none.
# """
# print("-------------------------")
# print(poem) 
# print("------------------------")
# five = 10 -2 +3 -6 
# print(f'This should be five: {five}')
# #def function:
# def secret_formula(started):
#     jelly_beans = started * 500 
#     jars = jelly_beans / 1000                               
#     crates = jars / 100 
#     return jelly_beans, jars, crates 
# start_point = 10000 
# beans, boiam, crates = secret_formula(start_point) 
# #4 ways to format a string
# #remember that is another way to format a string 
# print("With a starting point of {}".format(start_point)) 
# #it's just like an f"" string
# print(f"We'd have {beans} beans, {boiam} jars, {crates} crates.") 
# start_point = start_point / 10 
# print("We can also do that this way: ") 
# formula = secret_formula(start_point) #### Calling a function in a variable. 
# #this is an easy way to apply a list to a format string 
# print("We'd have {} beans, {} jars, {} crates.".format(*formula))

# #Exercise 25:
# def break_words(stuff):
#     """This function will break up words for us."""
#     words = stuff.split(' ') 
#     return words 
# def sort_words(words):
#     """Sorts the words."""
#     return sorted(words) 
# def print_first_word(words):
#     """Prints the first word after pooping it off."""
#     word = words.pop(0) 
#     print(word) 
# def print_last_word(words):
#     """Prints the last word after pooping it off."""
#     word = words.pop(-1) 
#     print(word) 
# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence) 
#     return sort_words(words) 
# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence) 
#     print_first_word(words) 
#     print_last_word(words) 
# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence) 
#     print_first_word(words) 
#     print_last_word(words) 

# #Exercise 29:###########################################################
# people = 20 
# cats = 30 
# dogs = 15 

# if people < cats:
#     print("Too many cats! The world is doomed!") 

# if people > cats:
#     print("Not many cats! The world is saved!")

# if people < dogs:
#     print("The world is drooled on!") 

# if people > dogs:
#     print("The world is dry!") 

# dogs += 5 

# if people >= dogs:
#     print("Peple are less than or equal to dogs.") 

# if people <= dogs:
#     print("People are less than or equal to dogs.") 

# if people == dogs:
#     print("People are dogs.") 

# #Exercise 30:###################################################################
# people = 30 
# cars = 40 
# trucks = 15 

# if cars > people:
#     print("We should take the cars.") 
# elif cars < people:
#     print("We should not take the cars.") 
# else:
#     print("We can't decide.") 

# if trucks > cars:
#     print("That's too many trucks.")
# elif trucks < cars:
#     print("Maybe we could take the trucks.") 
# else:
#     print("We still can't decide.") 

# if people > trucks:
#     print("Alright, let's just take the trucks.") 
# else:
#     print("Fine, let's stay home then.") 

# #Exercise 31:#####################################################
# print("""You enter a dark room with two doors.
#       Do you go through door #1 or door #2?""")
# door = input("> ")

# if door == "1":
#     print("There's a giant bear here eating a cheese cake.") 
#     print("What do you do?") 
#     print("1. Take the cake.") 
#     print("2. Scream at the bear.") 

#     bear = input("> ") 

#     if bear == "1":
#         print("The bear eats your face off. Great job!")
#     elif bear == 2:
#         print("The bear eats your legs off. Good job!") 
#     else: 
#         print(f"Well, doing {bear} is probably better.")
#         print("Bear runs away.") 

# elif door == "2": 
#     print("You starre into the endless abyss at Cthulhu's retina.") 
#     print("1. Blueberries.") 
#     print("2. Yellow jacket clothespins.") 
#     print("3. Understanding revolvers yelling melodies.") 

#     insanity = input("> ") 

#     if insanity == "1" or insanity == "2":
#         print("Your body survives powered by a mind of jello.") 
#         print("Good job!")
#     else:
#         print("The insanity rots your eyes into a ool of muck.") 
#         print("Good job!") 
# else:
#     print("You stumble around and fall on a knife and die. Good job!")  


# #Exercise 32:#################################################
# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quaters'] 

# #this first kind of for loop goes through a list

# for number in the_count:
#     print(f"This is count {number}.") 

# #same as above 
# for fruit in fruits:
#     print(f"A fruit of type: {fruit}")

# #also we can go through mixed lists too 
# #notice we have to use {} since we don't know what's in it 
# for i in change:
#     print(f"I got {i}.") 

# #we can also build lists, first start with an empty one 
# elements = [] 

# #then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print(f"Adding {i} to the list.") 
#     #append is a function that lists understand 
#     elements.append(i) 

# #now we can print them out too
# for i in elements:
#     print(f"The element was: {i}.") 

# #Exercise 33: 
# #while loop: 
# i = 0 
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}.") 
#     numbers.append(i) 

#     i = i + 1
#     print("Numbers now: ", numbers) 
#     print(f"At the bottom i in {i}.") 

# print("The numbers: ") 

# for num in numbers:
#     print(num) 

##### Exercise 35:
from sys import exit 

def gold_room():
    print("This room is full of gold. How much do you take?") 

    choice = input("> ") 
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:  
        dead("Man, learn to type a number.") 

    if how_much < 50:
        print("Nice you're not greedy, you win!") 
        exit(0) 

    else:
        dead("You greedy bastard!") 

def bear_room():
    print("There is a bear here.") 
    print("The bear has a bunch of honey.") 
    print("The fat bear is in front of another door.") 
    print("How are you going to move the bear?") 
    
    bear_moved = False 

    while True:
        choice = input("> ") 

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.") 
        elif choice == "taunt bear" and not bear_moved: 
            print("The bear has moved from the door.") 
            print("You can go through it now.") 
            bear_moved = True 
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.") 
        elif choice == "open door" and bear_moved:
            gold_room() 
        else:
            print("I got no idea what that means.") 

def cthulhu_room():
    print("Here you see the great evil Cthulhu.") 
    print("He, it, whatever stares at you and you go insame.") 
    print("Do you flee for your life or eat your head?") 

    choice = input("> ")

    if "flee" in choice:
        start() 
    elif "head" in choice:
        dead("Well that was tasty!") 
    else:
        cthulhu_room() 

def dead(why): 
    print(why, "Good job!") 
    exit(0) 

def start():
    print("You are in a dark room.") 
    print("There is a door to your right and left.") 
    print("Which one do you take?") 

    choice = input("> ")

    if choice == "left":
        bear_room() 
    elif choice == "right":
        cthulhu_room() 
    else:
        dead("You stumble around the room until you starve.") 


start() 