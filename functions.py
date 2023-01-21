# functions are a set of code which only runs when it is called
# the data inside a function are called arguments
#promote readability and code reuse

#parameters - are values accepted by the function inside the function definition
# arguments - are the values we pass to the function when we call it
# arguments can have a default value when it is not specified

#Example 1

def get_choices():
  player_choice = "rock"
  computer_choice = "paper"

  return player_choice   # return gives the value when the function is called

#Example 2

def greeting():
  return "Hi"

response = greeting()
print(response) 


# Example 3
def get_choices():
  player_choice = "rock"
  computer_choice = "paper"

  return player_choice

choices = get_choices()
print(choices)

# Example 4: 

def check_win(player, computer): #nag-pass-in ng dalawang variable
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie"

check_win("rock", "paper")

#Example 5:

def hello(name="my friend"): # will default to my friend if no name/argument is specified
  print("Hello! " + name)

hello("Genesis")
hello()

#Example 6:
def hi(name, age):
  print(f"Hello {name}, You are {age}.")

hi("Genesis", str(37))


#Example 7:
def change(value):
  value["name"]="Ruiz"

val = {"name": "Genesis"}

change(val)
print(val)

