from art import logo, vs
from game_data import data
import random
#from replit import clear
import os


def selecting():
  raa = random.choice(data)
  return raa


def high_low(point=0,f_selection = selecting()):
  os.system('cls')
  print(logo)
  if point > 0:
    print(f"You're right! Current score: {point}")
  first_option = f_selection
  second_option = selecting()
  if first_option == second_option:
    second_option = selecting()
  print(
      f"Compare A: {first_option['name']}, a {first_option['description']}, from {first_option['country']}")
  print(vs)
  print(
      f"Against B: {second_option['name']}, a {second_option['description']}, from {second_option['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B': ")
  if user_choice == 'A' and first_option['follower_count'] > second_option['follower_count']:
    print('You win')
    point += 1
    high_low(point,f_selection=second_option)
  elif user_choice == 'B' and first_option['follower_count'] < second_option['follower_count']:
    print('You win')
    point += 1
    high_low(point, f_selection=second_option)
  else:
    print(f"You Loose and you got {point} point ")


high_low()
