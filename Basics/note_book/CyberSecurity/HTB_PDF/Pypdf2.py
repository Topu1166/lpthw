#import PyPDF2 
#input_file = input("File Name: ")
#with open(input_file, "rb") as file:
#    reader = PyPDF2.PdfReader(file)
#    text = " " 
#    for page in reader.pages:
#        text += page.extract_text() + "\n" 
#
#with open("output.txt", "w") as out:
#    out.write(text) 

import PyPDF2
from docx import Document

# Ask user for input PDF and output DOCX
input_file = input("Enter PDF filename: ")       # e.g., mypdf.pdf
output_file = input("Enter DOCX filename: ")     # e.g., output.docx

# Read PDF
with open(input_file, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:                           # check if text was extracted
            text += page_text + "\n"

# Create Word document
doc = Document()
for line in text.split("\n"):
    doc.add_paragraph(line)

# Save DOCX
doc.save(output_file)

print(f"PDF has been converted to {output_file} successfully!")
