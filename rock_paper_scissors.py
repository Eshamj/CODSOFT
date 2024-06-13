import random
while True:
    user=input("Enter a choice (rock, paper, scissors): ")
    selections=["rock", "paper", "scissors"]
    computer_selection = random.choice(selections)
    print("You chose",user,",computer chose",computer_selection)

    if user==computer_selection:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user=="rock":
        if computer_selection=="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user=="paper":
        if computer_selection=="rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user=="scissors":
        if computer_selection=="paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

    play_again=input("Do you want to play again? (yes/no): ")
    if play_again.lower()== "no":
        break
