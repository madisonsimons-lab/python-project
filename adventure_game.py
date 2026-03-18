import random

class AdventureGame:
    def __init__(self):
        self.inventory = []
        self.score = 0
        self.sanity = 100
        self.paths = {
            'forest': self.forest_path,
            'marketplace': self.marketplace_path,
            'mountain': self.mountain_path,
            'ball': self.ball_path,
            'ruins': self.ruins_path
        }
        self.current_path = None

    def choose_path(self, path):
        if path in self.paths:
            self.current_path = path
            self.paths[path]()
        else:
            print("Invalid path.")

    def forest_path(self):
        print("You are in the forest.")
        self.riddle_game()  # Example mini-game

    def marketplace_path(self):
        print("You are in the bustling marketplace.")
        self.bargaining_game()  # Example mini-game

    def mountain_path(self):
        print("You have reached the mountain top.")
        self.puzzle_game()  # Example mini-game

    def ball_path(self):
        print("Welcome to the grand ball!")
        self.dancing_game()  # Example mini-game

    def ruins_path(self):
        print("You explore the ancient ruins.")
        self.tea_party_game()  # Example mini-game

    def riddle_game(self):
        print("Solving a riddle...")
        # implement riddle logic
        self.score += 10

    def bargaining_game(self):
        print("Bargaining with a merchant...")
        # implement bargaining logic
        self.score += 10

    def puzzle_game(self):
        print("Solving a puzzle...")
        # implement puzzle logic
        self.score += 10

    def dancing_game(self):
        print("Dancing at the ball...")
        # implement dancing logic
        self.score += 10

    def tea_party_game(self):
        print("Having a tea party...")
        # implement tea party logic
        self.score += 10

    def display_status(self):
        print(f"Inventory: {self.inventory}")
        print(f"Score: {self.score}")
        print(f"Sanity: {self.sanity}")

if __name__ == '__main__':
    game = AdventureGame()
    game.choose_path('forest')  # Start the game in the forest
    game.display_status()