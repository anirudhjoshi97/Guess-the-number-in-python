import random
import fibo

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)

guessed_number = random.randint(lower_bound, upper_bound)

x = random.randint(1, 10)

print("The number of guesses you have is:", x)

for _ in range(x):
    number = int(input("Please enter your number: "))
    if number == guessed_number:
        print("Congratulations, you got it right!")
        break
    else:
        print("Try again.")
else:
    print("Sorry, your choices are over! The correct number was:", guessed_number)

fibo.fib(10)
