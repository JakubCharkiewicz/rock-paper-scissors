rock = ''' 
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
import random

playes_choice = input("What d'you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
if playes_choice == "1":
    print("Player chooses: " + paper)
elif playes_choice == "0":
    print("Player chooses: " + rock)
else:
    print("Player chooses: " + scissors)

y = [rock, paper, scissors]
x = random.choice(y)

print("Computer chooses: " + x)

if playes_choice == "1" and x == scissors:
        print("The result: Computer wins!")

elif playes_choice == "1" and x == paper:
        print("The result: Draw!")

elif playes_choice == "1" and x == rock:
        print("The result: Player wins!")

if playes_choice == "2" and x == scissors:
        print("The result: Draw!")

elif playes_choice == "2" and x == paper:
        print("The result: Player wins!")

elif playes_choice == "2" and x == rock:
        print("The result: Computer wins!")

if playes_choice == "0" and x == scissors:
        print("The result: Player wins!")

elif playes_choice == "0" and x == paper:
        print("The result: Computer wins!")

elif playes_choice == "0" and x == rock:
        print("The result: Draw")











