import random

# Set game parameters
secret_number = random.randint(1, 100)
max_tries = 10

# Start the game loop
for tries in range(1, max_tries + 1):
  # Get player guess
  guess = int(input(f"Guess number {tries} (between 1 and 100): "))

  # Check guess
  if guess == secret_number:
    print("Congratulations! You guessed the number!")
    break  # Exit loop on correct guess
  elif guess < secret_number:
    print("Too low, try again!")
  else:
    print("Too high, try again!")

# End of game message
if tries == max_tries:
  print(f"Sorry, you ran out of tries. The number was {secret_number}.")
