#Loops

#Example 1

condition = True

while condition == True:
  print("The condition is true")
  condition = False #If the condition is not changed to False, then the loop is infinite


#Example 2
count = 0
while count < 10:
  print("The condition is True")
  count += 1

print("After the loop")

#Example 3 For Loop - commonly used to iterate items in a list

items = [1,2,3,4]
for item in items: #We are assigning each item in the list as the variable item
  print(item)

items = ["Genesis", "Ruiz", "Insigne"]

for index, name in enumerate(items):
  print(index, name)

#Example 4

for item in range(5):
  print(item)