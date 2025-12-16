# Rock Paper Scissors Game

import random

choices = ['rock', 'paper', 'scissors']

user_score = 0
computer_score = 0
round_number = 1

print("🎮 Welcome to Rock Paper Scissors Game 🎮")

while True:
    print(f"\n--- Round {round_number} ---")
    print("Choices: rock | paper | scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    print(f"Score ➜ You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

    round_number += 1

print("\n🎯 Final Score")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
print("Thanks for playing! 👋")
