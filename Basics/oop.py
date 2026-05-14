#Composition in Python is a design principle where on 
#class is built from one or more other classes by including 
#their objects as attributes, rather than inheriting from them. 
#It represents a "has-a" relationship, as opposed 
#to inheritance, which represents an "in-a" relationship.

#class Engine:
#    def start(self):
#        print("engine starting...")
#
#class car:
#    def __init__(self):
#        self.engine = Engine() #car "has-a" engine
#
#    def drive(self):
#        self.engine.start() 
#        print("car is driving.") 
#
#thing = car() 
#thing.engine 
#print(thing.drive()) 
#
#
##Inheritance is when a class derives attributes and methods 
##from another class, representing an “is-a” relationship.
#class Vehicle:
#    def move(self):
#        print("Vehicle is moving.")
#
#class Car(Vehicle):  # Car inherits from Vehicle
#    def honk(self):
#        print("Car is honking.")
#
#my_car = Car()
#my_car.move()  # Inherited from Vehicle
#my_car.honk()  # Defined in Car
#
##make a class named x that is-a y
#class apple:
#    def fru(self):
#        print("I love apple.") 
#
#class fruit(apple): #fruit is-a apple
#    def sell(self):
#        print(f"Sell the apples.") 
#
#thing = fruit() 
#thing.sell() 

# # Make a class named X that is-a Y.
# class Cat():
#     
#     def __init__(self):
#         word = "Look! This is so tasty."
# 
#     def ant():
#         print("The ants live in the sand.")
# 
# class Animal(Cat): #Cat is-a Animal 
# 
#     def __init__(self):
#         self.catch = "Catch me the bird."
#     def fish():
#         print("Do you fish everyday?") 
# 
# thing = Animal() #instanciate/ object 
# print(thing.catch)
# #thing.fish()  
# 
# def apple():
#     print("I am apples!")
# 


##Exercise 40:
#class band(object):
#    
#    def __init__(self, lyrics):
#        self.lyrics = lyrics 
#
#    def sing_a_song(self):
#        for line in self.lyrics:
#            print(line) 
#
#first_song = band(["If you miss the train I'm on,",
#                   "You will know that I'm gone.",
#                   "You can hear the whistle blow,",
#                   "A hundred miles away."]) 
#
#second_song = band(["Every night in my dreams,",
#                    "I see you, I feel you.",
#                    "You have come to see me,", 
#                    "Go on!"]) 
#
#first_song.sing_a_song() 
#second_song.sing_a_song() 


# class x(object):
#     def __init__(self):
#         print("x is a class.") 
# 
# class y(object):
#     def __init__(self):
#         print('y is a class.') 
# 
# 
# class a(x): #a is-a x 
#     def __init__(self):
#         super().__init__() #calls x's construction 
#         self.y = y() #composition: a has-a x 
#         print('x is initialized.') 
# 
# 
# obj = a() 
# 
# #class 
# class Song(object):
# 
#     def __init__(self, lyrics):
#         self.lyrics = lyrics 
# 
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line) 
# 
# 
# first_song = Song(["If you miss the train I'm on",
#                    "You will know that I'm gone.",
#                    "You can hear the wistle blow,", 
#                    "A hundred miles."])  
# 
# second_song = Song(["One day I'm gonna fly away,",
#                     "One day when haven close my name,", 
#                     "I lay I close my eyes at night,", 
#                     "I can see moon and light."]) 
# 
# print("---" * 10) 
# first_song.sing_me_a_song()
# print("---" * 10) 
# second_song.sing_me_a_song() 
# 
# 
# #Dictionary 
# fruits = {'Cherry': 'Tastes delicious!'} 
# print('---' * 10) 
# print(fruits['Cherry'])  
# 
# 
# #Import 
# import mystuff 
# 
# print("---" * 10) 
# mystuff.apple() 
# print("---" * 10) 
# print(mystuff.tangerine) 
# 
# #Class #Doing the same thing 
# class mystuff(object):
# 
#     def __init__(self):
#         self.tangerine = "Is it gonna happen." 
# 
#     def orange(self):
#         print("It looks orange in color with a round shape.") 
# 
# result = mystuff()
# print('---' * 10)
# result.orange() 
# print('---' * 10) 
# print(result.tangerine) 
# 
# fruit_names = "Apple Mango Lichi Guava Jackfruit"
# 
# words = fruit_names.split(' ') 
# more_fruits = ["Banana", "Pineapple", "strawberry", "Kiwi", "Orange", "Berry"]
# 
# while len(words) != 11:
#     fruit = more_fruits.pop() 
#     print("Adding: ", fruit) 
#     words.append(fruit) 
#     print(f"There are {len(words)} items now.") 
# 
# print(f"The choosen 11 fruits are: {words}") 
# 
# print(type(words)) 
# print(words[1]) 
# print(words[-1])
# print(words.pop())
# print(' '.join(words)) ##
# print(', '.join(words)) 
# print(', '.join(words[2:]))
# print(', '.join(words[3:6]))
# print('\n\n')
# #Create a mapping of state to abbreviation
# states = {
#         'Oregon': 'OR',
#         'Texas': 'TX',
#         'Florida': 'FL',
#         'California': 'CA'
#         }
# states['Michigan'] = 'MI'
# states['Arizona'] = 'AZ'
# 
# #Create some cities in them
# cities = {
#         'OR': 'Jackson Valley',
#         'TX': 'Mutton Vally',
#         'FL': 'Hollywood',
#         'CA': 'Detroid',
#         'AZ': 'Amber Villey',
#         'MI': 'JutiBar'}
# 
# print('---' * 10,'\n')
# print('Oregon is abbreviated as', states['Oregon']) 
# print('Texas is abbreviated as', states['Texas']) 
# 
# print('---' * 10,'\n')
# print(f"{cities['CA']} is a city of California.")
# print(f"{cities['MI']} is a city of California.") 
# 
# print('---' * 10,'\n')
# for state, abbre in states.items():
#     print(f"{state} is abbreviated as {abbre}.") 
# 
# print('---' * 10,'\n')
# for state, abbre in states.items():
#     print(f"{state} is abbreviated as {abbre},")
#     print(f"and has a city {cities[abbre]}.") 
# print('---' * 10,'\n')
# 
# print('---' * 10,'\n')
# state = states.get('Texas')
# 
# if not state:
#     print("Sorry, no Texas")
# else:
#     print(f"Texas is there in the states dict.")
# 
# city = cities.get('IN', 'DOES NOT EXIST AT ALL.')
# print(f"The city for the state 'IN' is: {city}.") 

# #DICTIONIARIES 
# states = {
#         "California": 'CA',
#         'Texas': 'TX',
#         'Florida': 'FL', 
#         'Arizona': 'AZ',
#         'Michigan': 'MI'}  
# 
# cities = {
#         'CA': 'Detroid',
#         'TX': 'Jackson Ville',
#         'FL': 'Flow Ville',
#         'AZ': 'Azi Ville',
#         'MI': 'Michi Ville'} 
# 
# for state, abbre in states.items():
#     print(f"{state} is abbreviated {abbre},") 
#     print(f"and has a city {cities[abbre]}.") 
# 
# print("---" * 10)
# for state, abbrev in states.items():
#     print(f"{state} has: {cities[abbrev]}.") 
# 
# print("---" * 10)
# mystuff = {'apple': "I Am apples."} 
# print(mystuff['apple'])
# 
# print("---" * 10)
# import mystuff 
# mystuff.apple() 
# print(mystuff.tangerine) 
# 
# mystuff.calculation1()
# 
# import operator 
# 
# operators = {
#         '+': operator.add,
#         '-': operator.sub,
#         '/': operator.truediv,
#         '*': operator.mul}
# 
# num1 = int(input("Enter the first number: "))
# op = input("Enter the operator (-, +, /, *): ") 
# num2 = int(input("Enter the second number: "))
# 
# if op in operators:
#     result = operators[op](num1, num2)
#     print(result)
# else:
#     print("Invalid Operators!") 
# import mystuff 
# print(mystuff.tangerine) 
# 
# mystuff.calculation1()  

#Class
class MyStuff(object):

    def __init__(self):
        self.tangerine="This is an attribute which is a piece of data that belongs to an object."

    def apple(self):
        print("Who loves to eat apples?") 

thing = MyStuff()
thing.apple()
print(thing.tangerine) 

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics #initializaing lyrics attribute

    def sing_me_aSong(self):
        for line in self.lyrics:
            print(line)

happy_bDay = Song(["Who makes my heart beats like thunder",
                   "Who makes me happy in the morning", 
                   "I will spend all my life with her."])

happy_song = Song(["There is a ship",
                   "Floating on the sea",
                   "Captain of the ship",
                   "James Cook."]) 
print("----" * 10)
happy_bDay.sing_me_aSong() 

print("----" * 10)
happy_song.sing_me_aSong() 

#Class FROM CHATGPT 
class Dog(object):

    def __init__(self, name, age):
        self.name = name 
        self.age = age #self.name is the attribute is stored in age

    def Bark(self):
        print(f"{self.name} is the name of the dog.")
        print(f"And it is {self.age} years old.") 

dog1 = Dog("Rodger", 3) #dog1 is an object/instance  
dog2 = Dog("Roller", 8) 

print("----" * 10) 
dog1.Bark()
dog2.Bark()
print("----" * 10) 

#Class: FROM CHATGPT 
class Car(object):

    def __init__(self, make,  model, year):
        self.make = make
        self.model = model 
        self.year = int(year) 

    def change_year(self, new_year):
        self.year= new_year 

    def get_car_info(self):
        print(f"Year: {self.year}\nMake: {self.make}\nModel: {self.model}") 

car1 = Car("Toyota", "Corolla", 2025)

print("----" * 10) 
car1.get_car_info()

#Change year of the car 
car1.change_year(2026) 

#Now with the update data
print("-----" * 10) 
car1.get_car_info()

#Class 2026-03-10 
class doggie():

    #__init__ is a method
    def __init__(self, name, food):
        self.name = name 
        self.food = food #attribute (self.food) 

    def love(self):
        print(f"{self.name} likes {self.food}.")

dog1 = doggie("Roma", "chicken leg") #An Object 
dog2 = doggie("Chase", "Rabbit leg") 

print("----" * 10)
dog1.love() 
dog2.love()

#Class 
class Book(object):

    def __init__(self, title, author):
        self.title = title 
        self.author = author 

    def summary(self):
        print(f"The book \'{self.title}\' is written by {self.author}.")

book1 = Book("The Radiant Reading", "William Bowman") 
book2 = Book("Learn Python The Hard Way", "Zed A Shaw")

print("----" * 10)
book1.summary()
book2.summary() 

#Exercise from ChatGPT 
class Student:

    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade 

    def report(self):
        print(f"{self.name} has reveived a grade of {self.grade}.") 

student1 = Student('Rick', 'A') 
student2 = Student('Anna', 'B') 

print("----" * 10)
student1.report()
student2.report() 
