# assignment operator

age = 20

# arithmetic operators

1+1 #2 Addition
2-1 #1 Subtraction
2*2 #4 Multiplication
4/2 #2 Division
4%3 #1 Remainder
4**2 #16 Exponentiation
5//2 # floor division - rounds down to the nearest whole number

# Arithmetic operators can be combined with the assignment operator

age = 20
age += 5

print(age)

# Comparison Operators

a = 1
b = 2

a == b  #False
a != b  #True
a > b   #False
a <= b  #True

print(isinstance, a==b)


# Boolean Operators

condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

#or - returns the first value of the operand that is not a false value, otherwise returns the last operand

print(0 or 1) #1
print(False or "hey") #'hey'
print('hi' or 'hey') #'hi'
print([] or 'hey') #'hey'
print(False or []) #'[]' since both 'False' or [] are both "False" values

#and - returns the second value given the first is true

print(0 and 1) #0
print(1 and 0) #0
print(False and "hey") #False
print("hi" and "he  y") #hey
print([] and False) #[]
print(False and []) #False


#identity operator: is

#membership operator: in

#ternary operator

def is_adult(age):
  if age > 18:
    return True
  else:
    return False

#using ternary
def is_adult2(age):
  return True if age > 18 else False
