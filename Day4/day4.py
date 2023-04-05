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

#Write your code below this line 👇
import random
print("******************************************")
print("\n-------Welcome to Rock Paper Scissors------\nPress 0(Rock), 1(Paper), 2(Scissors)\n")
print("******************************************")

user_input = int(input("Enter your choice:"))
print("\n Your choice:")
if (user_input <= 2):
  #display user input
  if user_input == 0 :
    print(rock)
  elif user_input == 1:
    print(paper)
  elif user_input == 2 :
    print(scissors)
else:
  print("\nEnter valid choice")
  exit(0)

#display computer generated input
print("\n Computer's choice:")
comp_input = random.randint(0,3)
if comp_input == 0 :
  print(rock)
elif comp_input == 1:
  print(paper)
elif comp_input == 2 :
  print(scissors)

print("******************************************")
#case 1 :Tie
if user_input == comp_input :
  print("Opps!Their's a Tie")
  
#Case 2 : Rock crushes Scissors 
if  ( user_input == 0 and comp_input == 2 ):
  print("Yayy! You won ...Rock crushed Scissors")
elif  ( comp_input == 0 and user_input == 2 ):
  print("Ohh No! You lost ...Rock crushed Scissors")

#Case 3: Paper covers Rock 
if  ( user_input == 1 and comp_input == 0 ):
  print("Yayy! You won ...Paper covers Rock")
elif  ( comp_input == 1 and user_input == 0 ):
  print("Ohh No! You lost ...Paper covers Rock")

#Case 4: scissors cut paper
if  ( user_input == 2 and comp_input == 1 ):
  print("Yayy! You won ...Scissors cuts Paper")
elif  ( comp_input == 2 and user_input == 1 ):
  print("Ohh No! You lost ...Scissors cuts Paper")

print("******************************************")
