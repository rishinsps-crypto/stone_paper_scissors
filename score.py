class Score:
    def __init__(self):
        self.user = 0
        self.computer = 0
        self.draw = 0

    def update(self, result):
        if result == "user":
            self.user += 1
        elif result == "computer":
            self.computer += 1
        else:
            self.draw += 1

    def display(self):
        print("\n📊 Score Board")
        print("You:", self.user)
        print("Computer:", self.computer)
        print("Draw:", self.draw)