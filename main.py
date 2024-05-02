import random
def main() :

    print("Let's play some Rock Paper Scissors!")
    print("Ready?")
    print("Lets go!")

    user_wins = 0
    computer_wins = 0

    options = ["rock", "paper", "scissors"]

    while True:
        user_input = input("Type Rock/Papaer/Scissors or Q to end the game: ").lower()

        if user_input == "q":
            break
            
        if user_input not in options:
            continue

        random_num = random.randint(0,2)
        #Rock : 0, Paper: 1, Scissors: 2

        computer_pick = options[random_num] 
        print(f"Computer picked {computer_pick}")

        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            
        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            
        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1

        elif user_input == "rock" and computer_pick == "rock":
            print("It's a tie!")

        elif user_input == "paper" and computer_pick == "paper":
            print("It's a tie!")

        elif user_input == "scissors" and computer_pick == "scissors":
            print("It's a tie!")
            
        else:
            print("Computer wins")
            computer_wins += 1
    
    print("")
    print(f"You won {user_wins} times")
    print(f"The computer won {computer_wins} times")

    if user_wins > computer_wins:
        print("You are victorious!")
    elif user_wins == computer_wins:
        print("Your and the computer are evenly matched")
    else:
        print("Better luck next time")

    print("")
    print("Goodbye")


main()