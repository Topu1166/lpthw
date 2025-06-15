#Exercise: 1 
#Check if the folder exists, if not create one 
#with user input. 
import os 
#Check if the file exists or not 
dir_name = input("Enter the folder's name: ") 
#printing the absolute path 
print("Printing the absolute path: ", os.path.abspath(dir_name)) 

if not os.path.exists(dir_name):
    rename_dir = input("Name the Folder: ") 
    os.makedirs(rename_dir) 
    print("There is no folder named {}.".format(dir_name))
    print("The folder has been created as {}.".format(rename_dir)) 
else: 
    print("The folder already exists.") 


#Exercise: 2 
#Unzip a folder  