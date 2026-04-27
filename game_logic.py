def get_winner(user, computer):
    if user == computer:
        return "draw"
    
    if (user == "stone" and computer == "scissors") or \
       (user == "paper" and computer == "stone") or \
       (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"