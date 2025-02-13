from art import logo
import random

random_num = random.choice(range(1,101))
print(random_num)

isGameOver = False

def health(level):
      life = 0
      if level == "easy":
            life += 10
            return life
      elif level == "hard":
            life += 5
            return life
      else:
            return life

def num_control(input_guess):
      global random_num
      if input_guess == random_num:
            print(f"You got it! The answer was {random_num}")
            return True
      elif input_guess > random_num:
            print("Too HIGH !")
            return False
      elif input_guess < random_num:
            print("Too LOW !")
            return False
      else:
            print("Wrong input !")
            return False

print("Welcome to the Number Guessing Game! \n"
"I'm thinking of a number between 1 and 100.")

user1 = input("Choose a difficulty. Type 'easy' or 'hard' :").lower()
episode_life = health(user1)


while not isGameOver:
      print(logo)
      for repeat in range(episode_life+1,0,-1):
            if repeat != 0:
                  print(f"You have {repeat-1} attempts remaining to guess the number.")
                  guess = int(input("Make a guess:"))
                  if num_control(guess):
                        break
            else:
                  print("Game over you lose !")
      isGameOver = True