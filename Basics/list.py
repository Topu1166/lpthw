# #Exercise: 1
# print("Hello World!") 
# print("Hellow Again") 
# print("I like typing this.")
# print("This is fun.")
# print('Yay! Printing.')
# print("I'd much rather you 'not'.") 
# print('I "said" do not touch this.') 

# #Exercise: 2 
# def grettings(name, age):
#     print("Hello, {} you are {} years old.".format(name, age)) 

# name = "Alice"
# age = 30 
# grettings(name, age)

# print("Hens", 100 / 25 + 50) 
# print("Rooters", 100 - 25 * 3 % 4) 


# cars = 100
# space_in_car = 5 
# passengers = 280 
# drivers = 45
# cars_driven = drivers 
# cars_not_driven = cars - cars_driven 
# carpool_capacity = space_in_car * cars_driven 
# average_passengers_per_car = passengers / drivers 

# print(f"There are {cars} cars available.")
# print(f"Each can can pool {space_in_car} passengers.")
# print(f"There are {passengers} passengers in total.") 
# print(f"There are {drivers} drivers are available.")
# print(f"{cars} cars are going to be driven.")
# print(f"We have {carpool_capacity} carpool today.") 
# print(f"We need to put about {round(average_passengers_per_car)} in each car.")


# ## Empty list
# list1 = []

# ## list of integers
# list2 = [] 

# ## list with mixed data types
# list3 = [1, 3, 'hello', '3.4']

# ### Nested list
# list4 = ['102', 'mixed', [2, 'hey', 102, 3.4], 8, 'mouse'] 
# print(list4[2])
# print(list4[-3]) 


# #Accessing elements from a list:
# fruits = ['lichi', 'mango', 'apple', 'orange'] 
# print(fruits[1:5])

# ## Change one Elements of a list:
# fruits[1] = 'cherry'
# print(fruits)

# ###Slicing a list:
# word = ['P', 'Y', 'T', 'H', 'O', 'N'] 

# print(word[0:3]) 
# print(word[:]) 
# print(word[3:6]) 



# ## Change item of a list:
# word = ['F', 'A', 'T', 'H', 'E', 'R'] 

# word[:-5] = 'M'
# print(word[:]) 

# word[2:8] = ['N', 'H', 'A', 'T', 'T', 'A', 'N']
# print(word[:]) 

# word1 = word[0:3] #Slicing and assigning 
# print(word1)

# ## Change an Item of a list:
# ## Using append() 
# name = ['Lisa', 'Matt', 'Sherry'] 
# name.append('Kerry') 
# print(name) 


# ## For Individual Item:
# ## Use extend() 
# animal = ['cat', 'dog', 'parrot'] 
# animal.extend(['whale', 'ant', 'robbin']) 
# print(animal * 3)


# add = name + animal 
# print(add) 


# ### Delete Item from a list:
# del add[0]
# print(add) 

# ######## Use of Some Methods for Lists: #############
# list = [1, 2, 3, 1, 4, 3, 8, 23, 10] 

# list.append(7) ### Add a element at the end of a list 
# print(list) 

# list.extend([28, 2, 4]) 
# print(list) 


# ####### 
# colors = ['Red', 'Black', 'brown', 'white', 'Red', 'Green']
# print('Original List:', colors)

# # change the first item to 'Purple'
# colors[2] = 'Purple'

# # change the third item to 'Blue'
# colors[2] = 'Blue'

# print('Updated List:', colors)

# ###
# colors.remove('Red') #removes the first occurance of a list ###
# print('remove the first occurance=', colors)

# ## 
# colors.pop(2) 
# print('white as White=', colors) 


# ###
# fruit = ['apple', 'banna', 'cherry', 'pineapple']

# fruit.pop(1) 
# print('pop result =', fruit) 


# ##
# my_list = [1, 2, 3, 4, 5, 6, 7]

# # my_list.remove(1)
# # print('remove(1)=', my_list) 

# my_list.pop(1) ##removes and returns the removed data when 'pop()' is in the print

# print(my_list) 

# my_list.extend([23, 88, 2]) ## extend at the end
# print(my_list)

# my_list.insert(2, 6) ## insert an element/elements at the specific place
# print(my_list)

# my_list.append(7) ## adds an element at the end 
# print('append(7)=', my_list) 

# your_list = my_list.copy() ## Shallow copy
# print("your list = ", your_list) 

# ## 
# your_list.clear() ## Clears the list
# print("An empty list =", your_list)


#### bro code: using: help, dir, and len function for the lists: #############
# list = ['lichi', 'mango', 'goava', 23, [23, 48, 'tem', 'cat'], 2.3, 'tom'] 
# # print(dir(list)) 
# print(help(list))



########## BRO CODE: ############ 
## Collection = single "variable" used to store multiple values
## list = [] ordered and changeable. Duplicates OK
## set = {} unordered and immutable, but add/remove OK, No Duplicates
## Tuple = () ordered and unchangeable. Duplicates OK, Faster  

# fruits = ["apple", "orange", "bananna", 'coconut']
#print(dir(fruits)) 
#print(help(fruits)) 
#print(len(fruits)) 
#print("pineapple" in fruits) 

# fruits[0] = "pineapple"
# fruits.append("pineapple") 
# fruits.remove("apple") 
# fruits.insert(0, "pineapple") 
# fruits.sort() 
# fruits.reverse() 
# fruits.clear() 
# print(fruits.index("apple")) 
# print(fruits.count("pineapple"))


#### Sets: #################################################################
#  set = {} unordered and immutable, but add/remove OK, No Duplicates

# fruits = {"apple", "orange", "bananna", "coconut"} 
# dir, help, len, print("apple" in fruits), 
# fruits.add("pineapple") 
# fruits.pop() = removes the first item 
# print(fruits[0]) ## can not be done indexing because they are unordered
# We can't change the values of a set but we add or remove elements 

## fruits.add("pineapple") 
## fruits.remove("apple") 
## fruits.pop() 
## fruits.clear() 
 
## TUPLE: ###########################################################
## Tuple = () ordered and unchangeable. Duplicates OK, Faster  
#print(fruits.counts("coconut")) # and 
#print(fruits.index("apple")) # two methods for tuple


# tuple = (1, 2, 3, 8, 2, 4, 8, 2) 
# print(tuple) 
# print("Let's count how many twos there are. There are {} twos in the list called tuple.".format(tuple.count(2)))
# print("Let's find the indexing of the list 'tuple': ")
# print("The index of 2 is: ", tuple.index(2)) 


# # ## Sets ##: 
# # #  set = {} unordered and immutable, but add/remove OK, No Duplicates
# fruits = {'apple', 'bananna', 'cherry', 'lichi'} 

# # print(dir(fruits)) 
# # print(help(fruits)) 
# print(len(fruits))

# # add = fruits.add("mango") 
# # print("Mango's been added: ", fruits.add('mango'))
# fruits.add('pineapple') 
# print(fruits)  

# fruits.remove('apple') 
# print("Apple is removed:", fruits) 

# fruits.pop() 
# print(fruits) 

# fruits.clear() 
# print(fruits) 

### List: Methods ##############

# 1. .append(), 2. .insert(), 3. .remove(), 4. .clear(), 5. .extend() 6. .pop(), 7. .copy()
names = ['Jerry', "Mary", "Carry", "Curtis", "Carol"] 

print("First print the 'name' variable without changing/duplicating: ") 
print(names, "\n\n") 

## 1. .append() 
print("Let's .append(), means adding an element at the end of the list: ") 
print("They are ordered, changeable and duplicate is Ok: ") 
names.append("Mary") 
print(names, "\n") 


### 2. .insert()
print("Insert an element at a specified index in a list: ") 
names.insert(2, 'Peter') 
print(names, "\n") 


## 3. .remove() 
print("Remove the first occurance of a specified element of a list: ") 
names.remove('Mary')
print(names, "\n")


## 4. .pop()  ## remove and return an element at a specific index (default is the last element) 
print("Remove and return an element at a specific index (default is the last element)")
names.pop(0)  ## removes the first element
names.pop() ## removers the last element by default 
print(names, '\n')

## 5. .copy() 
copy_names = names.copy() # creates a shallow copy of the list 
print("Names  has been copied by copy_names: ") 
print(copy_names, "\n") 

## 6. .extend() ## add each element from an iterable at the end of a list
name1 = ['Sharry', "Larry", "Kirk", "Paul"] 
copy_names.extend(name1)
print(copy_names, '\n') 

## 7. .clear() ## removes/clears all the elemenents of a list
print("The variable copy list is cleared: ") 
print("Let's see its elements after using the .clear() methon.")
print(copy_names.clear())

fruits = ['lichie', 'mango', 'cherry', 'apple'] 
print(dir(fruits)) 

mango_cont = fruits.count('mango')
mango_index = fruits.index('mango') 
print("The index of the mango: ", mango_index)  
print("There are {} mangoes in the list.".format(mango_cont)) 
print(fruits)


## 1.
###  Write a Python program to create a list with the numbers 1 to 5 and print it.
my_list = [1, 2, 3, 4, 5] 
print(my_list)

## 2.
#Given the list below, print the third element.
fruits = ['apple', 'bananna', 'cherry', 'date'] 
print(fruits[2]) 

## 3.
#Change the second element of the list below to "grape" and print the updated list.
fruits = ['apple', 'bananna', 'cherry'] 
fruits[1] = 'grape'  
print(fruits) 

## 4.
#Add "orange" to the end of the list below.
colors = ['red', 'blue', 'green'] 
colors.append('orange') 
print(colors) 

# 5.
# Remove "blue" from the list below and print the updated list.
colors = ['red', 'blue', 'green'] 
colors.remove('blue') 
print(colors) 


# 6. 
# Given the list below, print the first three elements using slicing.
numbers = [10, 20, 30, 40, 50] 
first_three = numbers[0 : 3] 
print(first_three) 

# 7.
# Write a for loop to print each element of the list below.
animals = ['cat', 'dog', 'elephant'] 
for animal in animals:
    print(animal)

# 8.
# Check if "apple" exists in the list below and print True or False.
fruits = ['banana', 'cherry', 'date'] 
print('apple' in fruits) 

# 9.
# Sort the list below in ascending order and print it.
numbers = [5, 3, 8, 1, 2] 
numbers.sort() 
print(dir(numbers)) 


# 10. 
# Create a new list containing the squares of numbers from 1 to 5 using list comprehension.
# List Compression:
numbers = [1, 2, 3, 4, 5] 

squared_numbers = [x ** 2 for x in numbers] #list compression 
print(squared_numbers) 

## Printing odd number using list compression:
numbers1 = [x * 2 for x in numbers]
print(numbers1)

### Reverse a list: ##########
numbers = [1, 2, 3, 4, 5]
numbers.reverse() 
print(numbers) 


#Reverse a list without using method/function:

def reverse_numbers(lst):
    left = 0 
    right = len(lst) - 1 
    while left < right:

        lst[left], lst[right] = lst[right], lst[left] ## swap  
        
        left += 1
        right -= 1

numbers = [1, 22, 23, 24, 25] 
reverse_numbers(numbers) 
print(numbers) 



### Reverse a number of a list using def function: ###########
def reverse_number(num):
    left = 0 
    right = len(num) - 1 

    while left < right:

        num[left], num[right] = num[right], num[left] 

        left += 1
        right -= 1 

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
reverse_number(lst) 
print(lst) 

### reverse a string using method: ##
lst.reverse() 
print("The list:", lst) 

### Concatination (+) and (*) Repeatation: #######
odd = (1, 2, 3) 
print("The concatination:", odd + (4, 5, 6)) 
odd1 = ("ten", "ben", [2, 3, 'cat']) 
result = odd + odd1
print("The second concatination:", result) 

## If you want to repeat something use (*):
my_tuple = ('a', 'b', 'c') 
repeat = my_tuple * 3
print("It has been repeated for three times:", repeat)


####### try to delete an item of a tuple: #####
##del odd[0]

#### Why the theme on Vim is so ugly: ##############
print("The theme in Vim is so ugly.") 


#### There I go! The Vim is successfully installed into Vscode: ###########################



#Reverse a list without using method/function:

#let's reverse a list: ###

def reverse_list(lst):
    left = 0 
    right = len(lst) - 1

    lst[left], lst[right] = lst[right], lst[left]  

    left += 1
    right -= 1 

number = [1, 2, 3, 4, 5, 6] 
result = reverse_list(number) 
print("The reversed number is: ", number)  
print(f"The reverse technique worked very well. \n")

### Set : ###############################
# The elements of a set is unmutable, unordered, and not duplicable: ######
my_set = set([38, 1, 48, 3]) ##### using set() a built-in-function 
print(f"The set is a built-in-function: {my_set}")

#subset the house list to get the floar 9.5
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50, 23.5]]

#subset the house list
ele = house[-1][2]
print(ele) 

#Sort the list below in asscending order and print:

def accending_order(numbers):

    for number in numbers:

