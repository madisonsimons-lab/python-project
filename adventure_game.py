import time
import random

class AdventureGame:
    def __init__(self):
        self.name = ""
        self.sanity = 100
        self.score = 0
        self.inventory = []
        
    def typewriter(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()
    
    def start_game(self):
        print("\n" + "="*60)
        self.typewriter("✨ WELCOME TO THE ENCHANTED ADVENTURE! ✨")
        print("="*60)
        
        self.name = input("\n🌸 What is your name, adventurer? > ").strip() or "Adventurer"
        self.typewriter(f"\nHello {self.name}! Your journey begins...\n")
        time.sleep(1)
        
        self.main_menu()
    
    def main_menu(self):
        while True:
            print("\n" + "="*60)
            print("CHOOSE YOUR PATH:")
            print("1. 🌲 Explore the Enchanted Forest")
            print("2. 🏪 Visit the Magical Marketplace")
            print("3. ⛰️  Climb the Mysterious Mountain")
            print("4. 👑 Attend the Royal Ball")
            print("5. 👻 Investigate the Haunted Ruins")
            print("6. 📊 Check Your Stats")
            print("7. 🚪 Exit Game")
            print("="*60)
            
            choice = input(f"\n{self.name}, choose (1-7) > ").strip()
            
            if choice == "1":
                self.forest_path()
            elif choice == "2":
                self.marketplace_path()
            elif choice == "3":
                self.mountain_path()
            elif choice == "4":
                self.ball_path()
            elif choice == "5":
                self.ruins_path()
            elif choice == "6":
                self.show_stats()
            elif choice == "7":
                self.end_game()
                break
            else:
                print("Invalid choice! Try again.")
    
    def forest_path(self):
        print("\n🌲 " + "="*56)
        self.typewriter("You enter a mystical forest filled with glowing mushrooms...")
        print("A fairy appears and challenges you to a riddle!\n")
        
        riddle = "I have cities but no houses, forests but no trees, and water but no fish. What am I?"
        print(f"Fairy's Riddle: {riddle}\n")
        
        answer = input("Your answer? > ").strip().lower()
        
        if "map" in answer:
            self.typewriter("\n✓ CORRECT! The fairy gives you a magical map!")
            self.inventory.append("Magical Map")
            self.score += 50
        else:
            self.typewriter(f"\n✗ Wrong! The answer was 'map'.")
            self.sanity -= 10
        
        print(f"\nScore: {self.score} | Sanity: {self.sanity}")
        time.sleep(1)
    
    def marketplace_path(self):
        print("\n🏪 " + "="*56)
        self.typewriter("You arrive at a magical marketplace!")
        print("A merchant challenges you to a bargaining game!\n")
        
        for attempt in range(3):
            try:
                offer = int(input(f"Attempt {attempt + 1}/3 - Offer (1-100): > "))
                if offer >= 80:
                    self.typewriter("\n✓ The merchant accepts!")
                    self.inventory.append("Magical Potion")
                    self.score += 60
                    break
                else:
                    print(f"Merchant: That's too low. Try again.")
            except:
                print("Invalid input!")
        
        print(f"\nScore: {self.score} | Sanity: {self.sanity}")
        time.sleep(1)
    
    def mountain_path(self):
        print("\n⛰️ " + "="*56)
        self.typewriter("You climb a misty mountain. A stone guardian appears!\n")
        
        answer = input("Guardian: What gets wet while drying? > ").strip().lower()
        
        if "towel" in answer:
            self.typewriter("\n✓ Correct! The guardian moves aside!")
            self.inventory.append("Rare Gem")
            self.score += 70
        else:
            self.typewriter(f"\n✗ Wrong! The answer was 'towel'.")
            self.sanity -= 20
        
        print(f"\nScore: {self.score} | Sanity: {self.sanity}")
        time.sleep(1)
    
    def ball_path(self):
        print("\n👑 " + "="*56)
        self.typewriter("You arrive at a grand royal ball!\n")
        print("DANCE CHALLENGE - Follow the pattern:\n")
        
        pattern = ["UP", "DOWN", "LEFT", "RIGHT", "SPIN"]
        correct = 0
        
        for i, move in enumerate(pattern, 1):
            player_input = input(f"Move {i} (type '{move}'): > ").strip().upper()
            if player_input == move:
                print("✓ Perfect!")
                correct += 1
            else:
                print(f"✗ Wrong!")
        
        if correct >= 4:
            self.typewriter("\n✓ Great dancing! Everyone applauds!")
            self.inventory.append("Royal Recognition")
            self.score += 80
        
        print(f"\nScore: {self.score} | Sanity: {self.sanity}")
        time.sleep(1)
    
    def ruins_path(self):
        print("\n👻 " + "="*56)
        self.typewriter("A ghostly figure appears!\n")
        
        answer = input("Ghost: I grow but am not alive. I need air but have no lungs. What am I? > ").strip().lower()
        
        if "fire" in answer:
            self.typewriter("\n✓ Correct! The ghost rewards you!")
            self.inventory.append("Ghost's Treasure")
            self.score += 100
        else:
            self.typewriter(f"\n✗ Wrong! The answer was 'fire'.")
            self.sanity -= 30
        
        print(f"\nScore: {self.score} | Sanity: {self.sanity}")
        time.sleep(1)
    
    def show_stats(self):
        print("\n" + "="*60)
        print(f"⭐ {self.name}'s STATS ⭐")
        print(f"Score: {self.score}")
        print(f"Sanity: {self.sanity}/100")
        print(f"Items: {', '.join(self.inventory) if self.inventory else 'None'}")
        print("="*60)
    
    def end_game(self):
        print("\n" + "="*60)
        print(f"Thank you for playing, {self.name}!")
        print(f"Final Score: {self.score}")
        print(f"Final Sanity: {self.sanity}/100")
        if self.inventory:
            print(f"Items Collected: {', '.join(self.inventory)}")
        print("="*60)

if __name__ == "__main__":
    game = AdventureGame()
    game.start_game()
