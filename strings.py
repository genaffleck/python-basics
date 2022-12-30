"Gen"
'Gen'

# assigning a string to a variable
name = "Gen" 

#concatenating strings
my_name = name + " is my name."
print(my_name)

name += "is my name"
print(name)

age = str(39) #converts to a string

# multiline string

print('''Gen is
37
years old
''')

# String built-in methods
# string methods do not change original string

name = "Gen"
print(name.upper())
print(name.lower())
print(name.islower()) # returns boolean
print("genesis ruiz".title())

#global functions

name = "Gen"
print(len(name))
print("G" in name) # returns boolean

# Escaping: characters

name = "G\"en"
print(name)

name_2= "Ge\nesis" #\n means new line
print(name_2)

name_3 = "Gen\\esis"
print(name_3)
