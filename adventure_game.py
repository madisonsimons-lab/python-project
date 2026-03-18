import random

class AdventureGame:
    def __init__(self):
        self.sanity = 100
        self.ending = None
        self.intro = "Welcome to the Enchanted Garden! 🌷 Beware, many have disappeared here..."

    def display_choices(self):
        print("\nChoose your path:")
        print("1 - Follow the Red-eyed Rabbit 🐇")
        print("2 - Approach the Cottage 🏡")
        print("3 - Explore the Ancient Forest 🌲")

    def rabbit_path(self):
        print("\nYou chase after the red-eyed rabbit... It leads you deeper into the garden.")
        self.sanity -= random.randint(5, 15)
        self.ending = self.bad_ending() if self.sanity < 50 else self.good_ending()

    def cottage_path(self):
        print("\nYou reach a dilapidated cottage. A doll-like woman greets you with a sinister smile...")
        self.sanity -= random.randint(10, 20)
        self.ending = self.bad_ending() if self.sanity < 50 else self.good_ending()

    def forest_path(self):
        print("\nAs you enter the forest, the trees whisper secrets. An ancient entity watches you...")
        self.sanity -= random.randint(0, 25)
        self.ending = self.bad_ending() if self.sanity < 50 else self.good_ending()

    def good_ending(self):
        return "🌟 You escaped the garden! You feel free, but the shadows linger..."

    def bad_ending(self):
        endings = [
            "You are never seen again, lost in the garden... 🌑",
            "The doll woman smiles wider as she takes you... 😱",
            "The ancient entity possesses you, and you become one with the forest... 🌲👻",
            "The rabbit leads you to darkness, and you realize it's a trap... 🕳️"
        ]
        return random.choice(endings)

    def play(self):
        print(self.intro)
        while self.ending is None:
            self.display_choices()
            choice = input("Enter your choice (1-3): ")
            if choice == '1':
                self.rabbit_path()
            elif choice == '2':
                self.cottage_path()
            elif choice == '3':
                self.forest_path()
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        print(self.ending)

if __name__ == '__main__':
    game = AdventureGame()
    game.play()