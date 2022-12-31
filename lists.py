# Lists are used to store multiple items in a single variable to reference them with a common name

# syntax: list_variable = [<item1>, <item2>, <item3>,...]

# Example 1


food = ["pizza", "carrots", "eggs"]

print(food)

# we can mix multiple data types in a list
dogs = ["Syd", "Roger",  1, True]

print("Roger" in dogs)
print(dogs[3])


# lists can also be empty
cats = []

# update items in a list
dogs = ["Syd", "Roger",  1, True]
dogs[1] = "Beau"
print(dogs)

#slice list
print(dogs[1:3])

#len
print(len(dogs))

#add items to a list
dogs.append("Quincy")
print(dogs)
dogs.extend(["A", "B"])
print(dogs)
dogs += ["C", "D"]
print(dogs)

#add items to a specific location in the list
dogs.insert(2, "E")
dogs[1:1] = ["Test1", "Test2"]

# remove items on list
dogs.remove("A")
print(dogs)

print(dogs.pop()) #returns last item on list


# sort list: must be the same data type: either all strings or all items are numbers

names = ["den", "Gen", "Pen", "Den"]
namescopy = names[:]
names.sort()
print(names)

# sort method orders uppercase letter first
names.sort(key=str.lower)
print(names)

# sorting changes the list
print(namescopy)