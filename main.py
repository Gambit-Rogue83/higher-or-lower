#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

hidden_num = random.randint(1,100)


def compare(num1, num2, num3):
  """Compares the user's guess to the hidden number, while reducing the number of attempts remaining"""
  if num1 > num2:
    print("Too high.\nGuess again.")
    return num3 - 1
  elif num1 < num2:
    print("Too low.\nGuess again.")
    return num3 - 1
  else:
    print(f"You got it! The answer was {num2}")
    
def game():  
  print(logo)    
  print("Welcome to Higher or Lower!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  game_over = False
  
  if difficulty == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
  elif difficulty == 'hard':
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

  guess = 0
    
  while guess != hidden_num:
    guess = int(input("Make a guess: "))
    attempts = compare(guess, hidden_num, attempts)
    if guess != hidden_num and attempts > 0:
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif attempts == 0:
      print("You've run out of guesses, you lose.")
      break

game()