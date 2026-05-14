# ### Set: ##########
# my_set = set({1, 83, 19, 43}) 
# print("\n1. set() built-in-function used: {} \n".format(my_set)) 
# 
# ### add() ###
# my_set.add(7) ## add a single item 
# print("2. An item's been added: {}\n".format(my_set)) 
# 
# 
# ### def() function: ###
# def addition(num1, num2):
#     # addition: 
#     
#     sum = num1 + num2 
#     return sum 
# 
# num1 = int(input("Enter the first number: ")) 
# num2 = int(input("Enter the second number: ")) 
# result = addition(num1, num2) 
# print(f"The sum of the two numbers is {result}") 
# 

### Guess the number : ####
# # 
# def guess_num(num):
#     
#     guess = input("Guess the number: ") 
#     while guess != num:
# 
#         guess = input("Guess the number: ") 
#         if guess == num:
#             print("You are correct!") 
# 
# number = 3
# guess_num(number) 
#
### Guess the number : ####
# 
# guess = int(input("Enter the number: ")) 
# number = 3
# 
# if number == guess:
#     print("You guessed the number correctly.")
# 
# elif number != guess:
#     print("You couldn't guess the number.") 
# 
# 
## Let write the same code using 'while loop': ################

#guess = int(input("Enter a number: ")) 

def guess_num(num):

    guess = 0  
    while guess != num: 
        guess = int(input("Guess the number: ")) 
        print("You are not correct.") 
        print("Try again: ") 

    print("You have correctly guessed the word.") 

number = 3
guess_num(number)


# 
# ## Now, using random libery: ###############
# import random 
# def guess_num():
#     
#     random_num = random.randint(1, 10) 
#     guess = 0 
#     while guess != random_num:
#         guess = int(input("Enter a number: ")) 
#         
#         #Condition:
#         if guess < random_num:
#             print("Go up! Still a small number.") 
#         
#         elif guess > random_num:
#             print("Go down! Still a big number.") 
# 
#     print("You have guessed the number {} correctly.".format(random_num))  
# 
# guess_num() 



#### practicing set: ####
# A set is always unordered, immutable, and no duplicates
people = {"Rony", "Kevin", "Manuel"}
print(type(people), "Names of people: ", people)

## let's add a single element: ###
people.add("John") 
print("John is addeded to the list.", people) 

### let's remove items: 
people.remove("Kevin") #removes an item only 
print("Kevin removed:", people) 

### let's discard items: ###
people.discard("Rony") # removes an item only 
print("Discarded: ", people) 


########## Set: ############################################
# Creat a set from a list: #####
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list) 
print(f"Type: {type(my_set)}") 
print(f"The elements of my_set: {my_set}")

## Add and remove element: ####
my_set.add(8) 
print(f"8 is added: {my_set}") 

## remove an element: ####
my_set.remove(2) 
print("2 is removed from my_set:{}".format(my_set))

## Set Union and Intersection: ### all elements except duplication 
num1 = {1, 2, 8, 5}
num2 = {6, 5, 2, 1} 

## using pipe (|):
#set_union = num1 | num2
set_union = num1.union(num2) 
print(f"set_Union: {set_union}")  

## Intersection: ### except the common ones
#intersection = num1 & num2 
intersection = num1.intersection(num2)
print(f"Intersection: {intersection}")

## 4. set difference: ### 
dif1 = num1.difference(num2)
# sum = num1 - num2
dif2 = num2.difference(num1) 
print(f"Set Difference: num1 - num2: {dif1}") 
print(f"Set Difference: num2 - num1: {dif2}") 

## 5. ###
# Remove duplicates from a sentence: ####
sentence = "hello world!"
unique_chars = set(sentence) 
print(f"Duplication has been removed: {unique_chars}") 

# 6. Find Common elements in two lists: ###
list1 = [1, 2, 3, 4] 
list2 = [3, 4, 5, 6] 

common = set(list1).intersection(list2) ## or set(list1) & set(list2)

print("The common elements are : {}".format(common)) 
except_duplication = set(list1) | set(list2) # or list1.union(list2) 
print("Set Union: print all items except duplication: {}".format(except_duplication)) 

## 1. Create a set from a list of numbers with duplicates. ######
my_list = [1,2, 2, 3, 4, 4, 5] 
my_set = set(my_list) ## creates a set using set function
print("A set's been created: {}".format(my_set))

## 2. Find the union of two sets: ###
A = {1, 2}
B = {2, 3, 4} 
my_union = A | B ## or my_union = A.union(B) 
print("The union of A and B is {}".format(my_union)) 

# 3. Add an element to a set: 
my_set = {1, 2, 3} 
my_set.add(4) 
print("An element (4) is added: {}".format(my_set)) 

# 4. Remove an element from a set: 
my_set.remove(2) 
print("2 is removed from my_set: {}".format(my_set)) 

# 5. Check if a value exists in a set: 
print("Does 3 exist in my_set?", 3 in my_set)

# 6. Convert a string to a set of unique characters. 
fruit = 'banana'
my_str = set(fruit) 
print("The string is converted into a set. {}".format(my_str)) 

# Intermediate Level: 
# 7. Find the intersection of two sets: 
A = {1, 2, 3} 
B = {2, 3, 4} 
intersection = A & B #or A.intersection(B) 
print("The common digits are {}".format(intersection)) 

# 8. Find the union of two sets: 
A = {1, 2} 
B = {3, 4} 
union = A | B #or A.union(B) 
print("All the elements of A and B: {}".format(union))

# 9. Find the difference between two sets. 
A = {1, 2, 3, 4}
B = {3, 4, 5} 
defference = A.difference(B) #or A - B 
print("The difference between A from B is {}".format(defference)) 

# 10. Check if a set is a subset of another. 
A = {1, 2, 3, 4} 
B = {3, 4, 5} 
subset = B.issubset(A) 
print("Is B a subset of A? {}".format(subset))

# 11. Check is a set is a superset of another. 
A = {1, 2, 3, 4}
B = {2, 3} 
superset = A.issuperset(B) 
print("Is A a superset of B? {}".format(superset)) 

#Check if a set is a bubset of another. 
A = {1, 2, 4} 
B = {2, 4, 8, 1} 
subset = A.issubset(B) 
superset = B.issuperset(A) 
print("Is A subset of B?:", subset)
print("Is B superset of A?:", superset)

# Difference: 
difference = A - B 
print("The difference is {}".format(difference))

# Check if the value exists in a set. 
print("Does 3 exist in A?:", 3 in A) 

#Guess the number:
import random

def guess_num():
    
    random_num = random.randint(1, 10)  
    guess_int = 0 

    while guess_int != random_num:
        guess_int = int(input("Guess the number: "))
        
        if guess_int > random_num:
                    print(f"The number is lower than {guess_int}.Try again:") 
        
        elif guess_int < random_num:
                    print(f"The number is higher than {guess_int}. Try again:") 
    
    print("Hurray! You have anticipated the number ({}) correctly.".format(guess_int)) 


guess_num()


