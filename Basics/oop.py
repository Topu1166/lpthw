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

# Make a class named X that is-a Y.
class Cat():
    
    def __init__(self):
        word = "Look! This is so tasty."

    def ant():
        print("The ants live in the sand.")

class Animal(Cat): #Cat is-a Animal 

    def __init__(self):
        self.catch = "Catch me the bird."
    def fish():
        print("Do you fish everyday?") 

thing = Animal() #instanciate/ object 
print(thing.catch)
#thing.fish()  

def apple():
    print("I am apples!")



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


class x(object):
    def __init__(self):
        print("x is a class.") 

class y(object):
    def __init__(self):
        print('y is a class.') 


class a(x): #a is-a x 
    def __init__(self):
        super().__init__() #calls x's construction 
        self.y = y() #composition: a has-a x 
        print('x is initialized.') 


obj = a() 

#class 
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics 

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line) 


first_song = Song(["If you miss the train I'm on",
                   "You will know that I'm gone.",
                   "You can hear the wistle blow,", 
                   "A hundred miles."])  

second_song = Song(["One day I'm gonna fly away,",
                    "One day when haven close my name,", 
                    "I lay I close my eyes at night,", 
                    "I can see moon and light."]) 

print("---" * 10) 
first_song.sing_me_a_song()
print("---" * 10) 
second_song.sing_me_a_song() 


#Dictionary 
fruits = {'Cherry': 'Tastes delicious!'} 
print('---' * 10) 
print(fruits['Cherry'])  


#Import 
import mystuff 

print("---" * 10) 
mystuff.apple() 
print("---" * 10) 
print(mystuff.tangerine) 

#Class #Doing the same thing 
class mystuff(object):

    def __init__(self):
        self.tangerine = "Is it gonna happen." 

    def orange(self):
        print("It looks orange in color with a round shape.") 

result = mystuff()
print('---' * 10)
result.orange() 
print('---' * 10) 
print(result.tangerine) 
