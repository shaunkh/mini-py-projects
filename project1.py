import random

def roll():
  return random.randint(1, 6)

while True:
  players = input("How many players (2-4)? ")
  if players.isdigit() and 2 <= int(players) <= 4:
    break
  else: 
    print("Pick a number from 2 to 4. Please try again.")

max_score = 0
player_scores = [0 for _ in range(int(players))]

while max_score < max(player_scores)