done = True

if done:
  print("Yes")
else:
  print("No")

print(type(done) == bool)

# numbers are always true except 0

done = 0
if done:
  print("Yes")
else:
  print("No")

# strings are always true except when empty

done = "Genesis"
if done:
  print("Yes")
else:
  print("No")

# any

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(read_any_book)

# all

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve)