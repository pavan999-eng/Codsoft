import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
def declare_final_winner(user_score, computer_score, tie_score):
    print("\n" + "=" * 40)
    print("\nFINAL RESULTS")
    print(f"You: {user_score}  |  Computer: {computer_score}  |  Ties: {tie_score}")
    if user_score > computer_score:
        print("\nYou are the overall WINNER! Congratulations!")
    elif computer_score > user_score:
        print("\nComputer wins this time! Better luck next time!")
    else:
        print("\nIt's a tie overall! What a close game!")
    print("=" * 40)
def rock_paper_scissors():
    user_score = 0
    computer_score = 0
    tie_score = 0  
    valid_choices = {"r": "rock", "p": "paper", "s": "scissors"}
    print("\nWelcome to Rock-Paper-Scissors!")
    while True:
        print("\n" + "-" * 40)
        print("Shortcuts: Rock (r), Paper (p), Scissors (s), Exit (x)")
        user_choice = input("Your choice: ").strip().lower()
        if user_choice in ["x", "exit"]:
            declare_final_winner(user_score, computer_score, tie_score)
            print("Thanks for playing! See you next time!")
            break
        user_choice = valid_choices.get(user_choice, user_choice)
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock (r), paper (p), scissors (s), or exit (x).")
            continue
        computer_choice = get_computer_choice()
        print(f"\nComputer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        else:
            tie_score += 1  
        print(f"\nScore -> You: {user_score}, Computer: {computer_score}, Ties: {tie_score}")
        while True:
            print("\nShortcuts: Yes (y), No (n)")
            play_again = input("Do you want to play again? (yes (y) / no (n)): ").strip().lower()
            
            if play_again in ["yes", "y"]:
                break
            elif play_again in ["no", "n"]:
                declare_final_winner(user_score, computer_score, tie_score)
                print("Thanks for playing! See you next time!")
                return
            else:
                print("Invalid input! Please enter 'yes' (y) or 'no' (n).")
rock_paper_scissors()
