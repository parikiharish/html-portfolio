import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choosing = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n").lower()
if choosing == "0":
    print(rock)
elif choosing == "1":
    print(paper)
elif choosing == "2":
    print(scissors)
else:
    print("You've choose wrong option")
rock_paper_scissors = [rock, paper, scissors]
print("Computer Choose:")
list_of_option = random.randint(0, 2)
print(rock_paper_scissors[list_of_option])
if list_of_option == 0:
    print("You Lose")
elif list_of_option == 1:
    print("You Win")
elif list_of_option == 2:
    print("You Lose")
