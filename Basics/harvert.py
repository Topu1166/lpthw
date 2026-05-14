# 
# from string import digits
#  
# for i in digits:
#     for j in digits:
#         for k in digits:
#             for l in digits:
#                 print(i, j, k, l) 

from string import ascii_letters

def four_lett_pass(word):
    approaches = 0

    for i in ascii_letters:
        for j in ascii_letters:
            for k in ascii_letters:
                for l in ascii_letters:
                    guess = i + j + k + l
                    approaches += 1 

                    if guess == word:
                        print(f"Password matched: {guess}")
                        print(f"Approaches: {approaches}") 
                        return 
    
    print("Password not found.") 
    
word = "kite"
four_lett_pass(word) 
