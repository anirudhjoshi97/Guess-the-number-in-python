import random


#enter the lower and upper bound value
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)


# computer will guess a number between the lower and upper bound range given by the user
guessed_number = random.randint(lower_bound, upper_bound)


# computer will tell the number of guesses
x = random.randint(1, 10)

print("The number of guesses you have is:", x)

#the number of attempts you have
for _ in range(x):
    #input your guessed number
    number = int(input("Please enter your number: "))\
    #will check the number if the number is correct or not
    if number == guessed_number:
        print("Congratulations, you got it right!")
        break
    else:
        print("Try again.")

 #when your attempts are over       
else:
    print("Sorry, your choices are over! The correct number was:", guessed_number)









