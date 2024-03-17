import random

words = ['anirudh', 'JOSHI', 'DILSHAD GARDEN', 'NAME']

computer_guess = random.choice(words)

number_of_attempts = random.randint(1, 5)
print("The number of attempts you have is: ", number_of_attempts)

for _ in range(number_of_attempts):
    user_guess = input("Enter the word: ")

    if user_guess == computer_guess:
        print("Congratulations, you have won the game!")
        break
    else:
        print("Try again.")

else:
    print("Sorry, you have exhausted all attempts.")

print("The word was:", computer_guess)

     