#### Set : ##################################
# The elements of a set is immutable, unordered, and not duplicable 
my_set = set({1, 38, 4, 8}) 

print(type(my_set), f"This is a buit-in-function: {my_set}") 


### 1.  remove()
my_set.remove(1) 
print("1 is removed from my_set: {}".format(my_set)) 

### 2.  add() ##################
my_set.add(23) 
print("\nadd() another number: {}\n".format(my_set))

## 3. discard(): #################
my_set.discard(8) 
print("8 has been discarded: {}\n".format(my_set))

## 4. update() ############
my_set.update({19, 39, 43}) 
print("'my_set' has been updated as 19, 39, and 43: {}\n".format(my_set)) 

## 5. pop() ###################
my_set.pop() # removes a random element from the set and returns the number 
print("A random number has been removed using .pop(): {}\n".format(my_set)) 


## 6. clear() ### clears the list 
# my_set.clear() 
# print("Clears the set: {}\n".format(my_set)) ## empty set

