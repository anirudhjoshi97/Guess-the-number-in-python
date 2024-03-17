import random

a = "rock"
b = "paper"
c = "scissor"

print("Enter a, b, or c")
user_choice = input("Enter your action: ")

if user_choice == a:
    print("You have chosen", a)
elif user_choice == b:
    print("You have chosen", b)
elif user_choice == c:
    print("You have chosen", c)
else:
    print("Invalid choice")

computer_choice = random.choice([a, b, c])
print("The computer has chosen", computer_choice)

if user_choice == computer_choice:
    print("It's a draw")
elif (user_choice == a and computer_choice == b) or \
     (user_choice == b and computer_choice == c) or \
     (user_choice == c and computer_choice == a):
    print("Computer has won the game")
else:
    print("You have won the game")
