#Package name: Pillow
#Objective: Convert any files into pdf
from PIL import Image 
#Open the image
in_data = input("Enter file name to covert into pdf: ") #input from the user
img = Image.open(in_data)
#save the image as:
save_file = input("Name the pdf file: ")
img.save(save_file, "PDF")
print("The image has been successfully converted into pdf.")



#####################

