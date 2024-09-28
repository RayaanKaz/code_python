import random

diffClass = int(input("Enter the difficulty class: "))
roll = input("Press enter to roll the dice")
diceRoll = random.randrange(0,21)
print(f"You rolled {diceRoll}")
if diceRoll >= diffClass:
    print("You win sigma")
else:
    print("You lose beta")
