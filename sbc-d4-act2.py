
from random import randint

print("Lottery!")

# Generate user's chosen numbers
user_numbers = [int(input(f"Choose your  numbers {i + 1} (0-9): ")) for i in range(3)]
print("Your chosen numbers:", *user_numbers)

# Generate the winning numbers
winning_numbers = [randint(0, 9) for _ in range(3)]
print("The winning numbers are revealed:", *winning_numbers)

# Check if the user's fate is intertwined with victory
if user_numbers == winning_numbers:
    print("Congratulations, you win!")
elif set(user_numbers) == set(winning_numbers):
    print("Some of your chosen numbers match the combination!")
else:
    print(" Better luck next time!")
