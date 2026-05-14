print("You want to know how much time would take to copy and write.") 
convert = int(input("How much GB: "))
regular = 4 
target = convert * 1024  
seconds = target / regular 
minutes = seconds / 60 
print(f"It  would take {minutes} minutes to finish.") 
