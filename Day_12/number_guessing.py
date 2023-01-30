import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff == 'easy':
    guess = 10
if diff == 'hard':
    guess = 5
rd_number = random.randint(1,100)
win = False
while guess>0:
    #print(f"You have {guess} attempts remaining to guess the number")
    ent_number = int(input("Make a guess: "))
    if ent_number == rd_number:
        print(f"You got it!!The answer is{rd_number}")
        win =True
        break
    elif ent_number> rd_number:
        print("Too high")
    else:
        print("Too Low")
    print("Guess again.")
    guess -=1
    print(f"You have {guess} attempts remaining to guess the number")

if win==True:
    print("")
else:
    print(f"You loose! The Number was {rd_number}")