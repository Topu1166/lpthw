name = "Alice"
age = 30

# Concatenation
print("My name is " + name + " and I am " + str(age) + " years old.")

# Old-style formatting
print("My name is %s and I am %d years old." % (name, age))

# str.format() method
print("My name is {} and I am {} years old.".format(name, age))

# f-strings
print(f"My name is {name} and I am {age} years old.")

# Template strings
from string import Template
template = Template("My name is $name and I am $age years old.")
print(template.substitute(name=name, age=age))
