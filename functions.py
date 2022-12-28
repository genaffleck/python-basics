# functions are a set of code which only runs when it is called
# the data inside a function are called arguments

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