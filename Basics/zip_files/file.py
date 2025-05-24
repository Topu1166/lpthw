import os 

file_name = input("Enter the folder's name: ") 

if not os.path.exists(file_name):
    os.makedirs("my_folder") 
    print("There is no folder named {}.".format(file_name))
    print("The folder has been created as 'my_folder'.") 
else: 
    print("The folder already exists.")