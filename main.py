from game_logic import get_winner
from score import Score
from utils import get_computer_choice, get_user_choice


def play_game():
    score = Score()

    print("🎮 Welcome to Stone Paper Scissors Game")
    print("Press 'q' to quit anytime\n")

    while True:
        user = input("\nPlay? (y/q): ").lower()

        if user == "q":
            print("\n👋 Exiting Game...")
            score.display()
            break

        elif user == "y":
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print("You chose:", user_choice)
            print("Computer chose:", computer_choice)

            result = get_winner(user_choice, computer_choice)

            if result == "user":
                print("🔥 You Win!")
            elif result == "computer":
                print("💻 Computer Wins!")
            else:
                print("😐 It's a Draw!")

            score.update(result)

        else:
            print("❌ Invalid input!")


if __name__ == "__main__":
    play_game()