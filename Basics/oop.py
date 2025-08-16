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
        self.word = "Look! This is so tasty."

    def ant():
        print("The ants live in the sand.")

class Animal(Cat): #Cat is-a Animal 

    def __init__(self):
        self.catch = "Catch me the bird."
    def fish():
        print("Do you fish everyday?") 

thing = Animal() #instanciate/ object 
thing.catch 
thing.fish 