# tuples: allows you to create immutable groups of objects: which means once created can no longer be modified
#uses parenthesis

names = ("Roger", "Syd", "Beau")

print(names[0])
print(names.index("Roger"))
print(len(names))
print("Roger" in names)

# We can also extract part of tuples using slices

#sort
print(sorted(names)) #does not modify the tuple

newTuple = names + ("Tina", "Nina")
print(newTuple)
