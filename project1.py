import random

def roll():
  return random.randint(1, 6)

while True:
  players = input("How many players (2-4)? ")
  if players.isdigit() and 2 <= int(players) <= 4:
    break
  else: 
    print("Pick a number from 2 to 4. Please try again.")

max_score = 50
player_scores = [0 for _ in range(int(players))]

while max_score > max(player_scores):
  for i in range(int(players)):
    print("Player " + str(i + 1) + "'s turn")
    score = 0

    while True:
      should_roll = input("Would you like to roll? (y/n) ")
      if(should_roll.lower() != "y"):
        break

      value = roll()
      print("You rolled a", value)
      if(value == 1):
        print("Turn ended!")
        score = 0
        break
      else: 
        score += value
        
      print("Your score is", score)

    player_scores[i] += score
    print("Your total score is", player_scores[i])

  

