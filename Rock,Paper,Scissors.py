import random
rock = '🪨'
paper = '📄'
scissor = '✂'
game_images = [rock, paper, scissor]

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice < 0 or user_choice > 2:
    print("Invalid number, you lose.")
else:
    print(f"You chose: {game_images[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_images[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw.")
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")