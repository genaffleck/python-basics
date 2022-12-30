import random

player_name = input("What is your name?: ").title()

def get_choices():
  player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
  sirRuiz_options = ["rock", "paper", "scissors"]
  sirRuiz_choice = random.choice(sirRuiz_options)
  choices = {"player": player_choice, "sirRuiz": sirRuiz_choice}
  return choices

def check_win(player, sirRuiz):
  print(f"You chose {player}, sirRuiz chose {sirRuiz}")
  if player == sirRuiz:
    return "It's a tie"
  elif player == "rock":
    if sirRuiz == "scissors":
      return f"You win {player_name}!"
    else:
      return f"You lose {player_name}!"
  elif player == "paper":
    if sirRuiz == "rock":
      return f"You win {player_name}!"
    else:
      return f"You lose {player_name}!"
  elif player == "scissors":
    if sirRuiz == "paper":
      return f"You win {player_name}!"
    else:
      return f"You lose {player_name}!"

choices = get_choices()
result = check_win(choices["player"], choices["sirRuiz"])
print(result)