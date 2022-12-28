# functions are a set of code which only runs when it is called

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
