import random
import time

print("Rock, Paper, Scissors Game")
print("Choose an option, and I'll try to beat you!")

# User choice input
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Introduce delay before displaying result
print("Thinking... 🤔")
time.sleep(1)  # 1-second delay

# Generate computer choice
computer_choice = random.choice(["rock", "paper", "scissors"])

# Game logic
if user_choice == computer_choice:
    result = "It's a tie!"
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    result = "You win!"
else:
    result = "You lose!"

# Display results
print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
print(result)