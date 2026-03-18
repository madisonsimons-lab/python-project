import time
import random

class AdventureGame:
    def __init__(self):
        self.sanity = 100  # Player's sanity level
        self.name = ""
        self.story_path = []

    def start_game(self):
        self.typewriter_effect("Welcome to the Adventure Game!\n")
        self.set_character_name()  # Set the character name
        self.choose_path()  # Player starts at the first choice

    def typewriter_effect(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)  # Delay between characters
        print()  # New line at the end

    def set_character_name(self):
        self.name = input("What is your character's name? ")
        self.typewriter_effect(f"Ah, {self.name}! A fine name!\n")

    def choose_path(self):
        self.typewriter_effect("You find yourself at a crossroads. Do you go Left or Right? ")
        choice = input("(L/R): ").strip().lower()
        if choice == 'l':
            self.path_left()
        elif choice == 'r':
            self.path_right()
        else:
            self.typewriter_effect("Not a valid choice! Try again.\n")
            self.choose_path()  # Recur until valid choice

    def path_left(self):
        self.typewriter_effect("You head into the ancient forest...\n")
        self.sanity -= random.randint(10, 30)  # Random sanity decrease
        self.typewriter_effect(f"Your sanity level is now {self.sanity}.\n")
        if self.sanity <= 0:
            self.game_over("You've lost your sanity in the forest.")
        else:
            self.typewriter_effect("You encounter a dark creature! Choose to Flee or Face it!\n")
            choice = input("(F/F): ").strip().lower()
            if choice == 'f':
                self.typewriter_effect("You flee back to safety!\n")
                self.start_game()  # Restart to give another chance
            else:
                self.game_over("You faced the darkness... and lost.")

    def path_right(self):
        self.typewriter_effect("You discover a cottage...\n")
        self.typewriter_effect("Inside, a tea party awaits!\n")
        self.typewriter_effect(f"Would you like to join {self.name}? (yes/no) ")
        choice = input("(y/n): ").strip().lower()
        if choice == 'y':
            self.typewriter_effect("You enjoy a beautiful tea party!\n")
            self.start_game()  # Option to restart
        else:
            self.typewriter_effect("You leave the cottage but find something eerie in the forest...\n")
            self.path_left()  # Go back to left path

    def game_over(self, reason):
        self.typewriter_effect(reason)
        self.typewriter_effect("Game Over!\n")
        self.typewriter_effect(f"Thank you for playing, {self.name}!\n")
        self.typewriter_effect("Would you like to play again? (yes/no)")
        choice = input("(y/n): ").strip().lower()
        if choice == 'y':
            self.sanity = 100  # Reset sanity
            self.start_game()  # Restart
        else:
            self.typewriter_effect("Farewell!")

if __name__ == '__main__':
    game = AdventureGame()  # Create an instance of the game
    game.start_game()  # Start the game