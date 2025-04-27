# # # def function(x):
# # #     print("Hello World!") 
# # #     print("Hello world!-2")
# # #     print(f"We are going to print {x}.")
# # #     return 2 * x 

# # # print("This line is outside the function.") 
# # # # function(3) 
# # # a = function(4) 
# # # print(a) 

# # ## BMI:
# # name1 = "Polash"
# # weight1 = 53
# # height1 = 2 #meters 

# # name2 = "Regan"
# # weight2 = 65 
# # height2 = 1 #meter 

# # def bmi_calculator(name, weight_kg, height_m):
# #     bmi = weight_kg / (height_m ** 2) 
# #     print("BMI: ") 
# #     print(bmi) 
# #     if bmi < 25:
# #         return name + " is not overweight."
# #     else: 
# #         return name + " is overweight." 
# # a = bmi_calculator(name1, weight1, height1) 
# # b = bmi_calculator(name2, weight2, height2) 
# # print(f"{a}\n{b}\n")

# #convert miles into kilometers:
# def covert_miles_into_kilo(x):
#     kilo = miles * 1.60934
#     print(f"\nSo we are going to convert {miles} miles into Kilometers that is {x}.")
#     return miles * 1.60934 
# miles = 5 
# x = covert_miles_into_kilo(miles)
# print(f"Therefore, {miles} miles equals {round(x)}.\n")  

# #Let's convert minutes to seconds:
# def minutes_into_second(minute): 
#     seconds = minute * 60
#     print(f"Here is the conversion of minutes into seconds: ") 
#     return minute * 60 
# minute = 50
# result = minutes_into_second(minute)
# print(f'Therefore, {minute} minute = {result} seconds.\n') 

# #Now we are going to convert seconds into minutes:
# def seconds_into_minutes(seconds):
#     minutes = seconds / 60  
#     print(f"Converting {seconds} seconds into minutes.")
#     return seconds / 60
# minutes = 5800 
# f = seconds_into_minutes(minutes) 
# print(f"Therefore, {minutes} seconds = approcimately {round(f)} minutes.") 

# #No we are going to try to use if-else statement in the def function.
# def get_the_job_or_not(age):
#     if age <= 25:
#         return(f"You get the job.")
#     else:
#         return("You do not get the job.\nBecause you are more than 25 years old.") 
# age = get_the_job_or_not(30)
# print(age)

# #Last but not the least:
# #Converting kilogram to gram: 
# def kilogram_to_gram(kilogram):
#     gram = kilogram * 1000
#     print(f"Let's print {kilogram} kg into grams.")
#     return kilogram * 1000 
# kilogram = 17.5 
# result = kilogram_to_gram(kilogram)
# print(f"{kilogram} kg = approximately {round(result)} grams.\n")

# #Convert meter to kilometer: 
# #And gram to kilogram:
# def gram_to_kg(gram):
#     kg = gram / 1000
#     print(f"Convert {gram} grams to kg:")
#     return gram / 1000 
# gram = 750
# result = gram_to_kg(gram) 
# print(f"{gram} grams = {result} kg.")  

# You have 900 taka in total. A piece of cake costs 75 taka, and you are going to purchase 8 of them. 
# A chocolate costs 45 taka, how many chocolate do you think you can buy with the rest of the money?
# And how much money do you think would be remaining?
# def money_left_and_candy_quantity(total_money, cake_price, cake_quantity, candy_price):
#     cake_expense = cake_price * cake_quantity
#     remaining_money = total_money - cake_expense
#     candy_quantity = remaining_money // candy_price 
#     money_left = remaining_money % candy_price 
#     return candy_quantity, money_left 
# #Difine the perimeters:
# total_money = 900 
# cake_price = 75 
# cake_quantity = 8 
# candy_price = 45 
# #Calling the function through assingment:
# candy_quantity, money_left = money_left_and_candy_quantity(total_money, cake_price, cake_quantity, candy_price)
# # Print the result:
# print(f"There will be {candy_quantity} which can be bought with the remainding money.")
# print(f"Money left: {money_left}.") 

# #Truncate a file and write the file:
# from sys import argv 
# script, file_name = argv 
# target_file = open(file_name, 'w') 
# print("The file is going to be truncated.\nHit Ctrl-C to quit.\nHit Enter to continue:")
# input("> ")
# target_file.truncate() 
# line1 = input("Line 1: ") 
# line2 = input("Line 2: ") 
# target_file.write(f"{line1}\n{line2}\n")
# target_file.close() 

# #Open a file:
# from sys import argv 
# script, file_open = argv 
# target = open(file_open, 'r') 
# print(f"{target.read()}", end='')

# #Finding average marks:
# def count_average(marks):
#     sum_of_marks = sum(marks)
#     quantity_of_marks = len(marks) 
#     average_marks = sum_of_marks / quantity_of_marks
#     return average_marks 
# marks = [80, 75, 93, 76, 95]
# average_marks = count_average(marks) 
# print(f"You have got {round(average_marks)} marks in average.") 
# #Let's count average_grade:
# def average_grade(average_marks):
#     if average_marks >= 90 :
#         grade = "A+" 
#     elif average_marks >= 80:
#         grade = "A" 
#     elif average_marks >= 70: 
#         grade = "B"
#     elif average_marks >= 60:
#         grade = "C" 
#     elif average_marks >= 50:
#         grade = "D"
#     else: 
#         grade = "F" 
#     return grade 
# grade = average_grade(average_marks) 
# print(f"You have got {grade} in average.")

# #Suppose you want to purchase 7 basketballs each costs 250 taka.
# # Each net costs 120 taka. You have 3000 taka in total. 
# #How many nets can you buy with the rest of the money? And how much money do you think would be left?
# def net_quantity_and_money_left(basketball_price, basketball_quantity, net_cost, total_money):
#     basketball_expense = basketball_price * basketball_quantity
#     remaining_money = total_money - basketball_expense 
#     net_quantity = remaining_money // net_cost
#     money_left = remaining_money % net_cost
#     return money_left, net_quantity
# #Difine the parameters:
# basketball_price = 250 
# basketball_quantity = 7 
# net_cost = 120 
# total_money = 3000 
# money_left, net_quantity = net_quantity_and_money_left(basketball_price, basketball_quantity, net_cost, total_money)
# print(f"You can purchase {net_quantity} nets with the remaining money.") 
# print(f"Money left: {round(money_left)}")

# #Finding the biggest number using def
# def biggest_num(n1, n2):
#     if n1 > n2:
#         return n1
#     else: 
#         return n2 
# #Difine the perimeters with arguments: 
# n1 = 87
# n2 = 89 
# print(f"Therefore, {biggest_num(n1, n2)} is the biggest.") 

# #Converting meters into kilometers:
# def convert_meters(meters):
#     kilometers = 1000 
#A hen lays 13 eggs after every 6 months. Two eggs wasted, rest (11) of the eggs become chicken. 
# takes 1 month from eggs to chicken. How many chickens will be there after 2 and half years? 
# A chicken becomes mature to lay eggs after 7 months after it is born.
def chikens_left_two(one_year): 
    two_and_half_years = one_year * 2.5
    
    return two_and_half_years
one_year = 12
two_and_half_years = chikens_left_two(one_year)
print(f"Two and half years equals {two_and_half_years} months..")

