#all things in python are objects

# Example 1

age = 8

#age has access to all the functions and methods for int

print(age.real)
print(age.imag)


# Example 2

item = [1,2]
item.append(3)
print(item)
item.pop()
print(item)

print(id(item))