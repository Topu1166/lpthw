#Make the accending order of a list.
my_list = [1, 8, 3, 2, 10, 5] 
sort_list = sorted(my_list) 
print(f"The sorted list is {sort_list}.")

#
#Sum of Number from 1 to N:
#Write a program that asks the user to enter number
# 'n' and prints the sum of all numbers from 1 to n.
number = int(input("Enter a number to print the sum of it: ")) 

sum = 0 
for num in range(1, number + 1):
    sum += num 

print(f"The sum of the number is {sum}.")  


#Even or odd:
#Write a program that asks the user to enter a 
#number and prints whether it is even or odd. 
even_or_odd = int(input("Enter a number whether it's even or odd: ")) 

def even_odd(num):
    if num == 0: 
        print(f"{num} is neither even or odd.")
    elif num % 2 == 0:
        print(f"{num} is an even number.") 
        
    elif num % 2 != 0:
        print(f"{num} is an odd number.") 

even_odd(even_or_odd) 

#Find the largest Number:
#Given a list of numbers: [4, 9, 1, 22, 17], write 
#code to find the largest number.
number = [4, 9, 1, 22, 17] 
largest_number = max(number) 
print(f"The largest number is {largest_number}.") 

#Manually:
def largest_num(num):
    largest = num[0]
    for x_num in num:
        if x_num > largest:
            largest = x_num 

    return largest 

rslt = largest_num(number) 
print("The largest number is {}.".format(rslt)) 

#check for Prime Number:
#Write a program that takes an integer as input and
#checks whether it's a prime number. 
prime_number = int(input("Enter a number whether it's a prime or not: ")) 

if prime_number == 1 or prime_number == 0:    
    print(f"{prime_number} is not a prime number.")

    is_prime = True 
    for num in range(2, int(prime_number ** 0.5) + 1):
        if prime_number % num == 0:
            is_prime = False 
            break 
        
    if is_prime: 
        print(f"{prime_number} is a prime number.") 
    else:
        print(f"{prime_number} is not a prime number.") 


#Reverse a string:
#Write a function that takes a string and returns it
# reversed (eg., "hello" becomes "olleh"). 
revrs = input("Enter a word or a sentence to reverse it: ") 

def reversed_string(word):
    return word [:: -1] 

rslt = reversed_string(revrs) 
print(f"The reversed string is {rslt}.") 


#Manually:
word_sen = input("Enter a word or a sentence to reverse it: ") 

reversed_str = " "
for char in word_sen:
    reversed_str = char + reversed_str 

print(f"The reversed string is \"{reversed_str}.\"") 


#6. Count Vowels 
#Write a program to count the number of vowels in 
#a given string. 
a_string = input("Enter a sentence to count vowels: ") 

def count_vowels(sentence):
    vowels = "AEIOUaeiou" 
    count = 0 
    for x in sentence:
        if x in vowels:
            count += 1 
    return count 

rslt = count_vowels(a_string) 
print("There are {} vowels in the given sentence.".format(rslt)) 


#Fibonacci Sequence: 
def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

number = 10 
for i in range(number + 1):
    print(fibonacci(i), end=' ') 