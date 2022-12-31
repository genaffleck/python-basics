# Dictionaries are used to store data values in key value pairs

#syntax: dictionary_name = {"key1":value1, "key2":value2, ... }
#Note: values can be strings or variables

# Example 1

dict = {"name": "Beau","color": "Blue"}

dog = {"name" : "Roger", "age": 8, "color": "blue"}

print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(list(dog.values()))
print(dog.items())
print(list(dog.items()))
print(len(dog))

# add items
dog["favortite food"] = "Meat"
print(dog)

dog["name"] = "Syd"
print(dog["name"])

print(dog.get("name"))
print(dog.get("color", "brown"))
print("age" in dog)

print(dog.pop("name"))
print(dog)
print(dog.popitem()) #removes the last key-value pair inserted