#from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os
# Clearing the Screen
os.system('cls')
from Day_13.art import logo
print(logo)
bidding_record = {}
print("welocme to the secret auction program")
bidding_ongoing = True
highest_bider = ''
highest_bidding = 0
#while loop for getting all the bids of the user
while bidding_ongoing == True:
    # asking the user for their name and the bidding price
    name = input("What is your name?:")
    bid = int(input("What's your bid?:"))
    # storing the data inside the dictionary
    bidding_record[name] = bid
    # ask the user for adding more bids :- if yes then accept the bids else show the highest biders data
    bidding_ongoing_ = input("Are there any other bidders? Type 'yes' or 'no'.")
    if bidding_ongoing_ == 'yes':
      bidding_ongoing = True
      #clear()
      os.system('cls')
    else:
      bidding_ongoing = False
      #clear()
      os.system('cls')
      for i in bidding_record:
        if bidding_record[i] > highest_bidding:
          highest_bidding = bidding_record[i]
          highest_bider = i
      print(
          f"The highest bider is {highest_bider} and the bidding amount is {highest_bidding}")
