import time
import random
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

class AdventureGame:
    def __init__(self):
        self.name = ""
        self.character_class = ""
        self.companion = ""
        self.companion_name = ""
        self.sanity = 100
        self.score = 0
        self.inventory = []
        self.gold = 100
        self.companion_actions = []
        
        self.companions = {
            "Phoenix": {
                "emoji": "🔥",
                "description": "A majestic fire bird that boosts your score",
                "actions": ["soars above and reveals hidden treasure!", "burns enemies to ashes!", "grants you a vision of the future!"],
                "bonus": "score",
                "color": Fore.RED
            },
            "Shadow Wolf": {
                "emoji": "🐺",
                "description": "A mystical wolf that keeps you safe",
                "actions": ["growls and scares away danger!", "sniffs out the correct answer!", "protects you from harm!"],
                "bonus": "sanity",
                "color": Fore.CYAN
            },
            "Crystal Butterfly": {
                "emoji": "🦋",
                "description": "A delicate butterfly that brings luck",
                "actions": ["spreads glittering dust for luck!", "guides you through the darkness!", "brings you good fortune!"],
                "bonus": "gold",
                "color": Fore.MAGENTA
            },
            "Storm Dragon": {
                "emoji": "⚡",
                "description": "A powerful dragon that amplifies your power",
                "actions": ["unleashes lightning to stun enemies!", "creates a storm of power!", "roars with tremendous force!"],
                "bonus": "score",
                "color": Fore.YELLOW
            },
            "Moonlight Fox": {
                "emoji": "🦊",
                "description": "A clever fox that helps with riddles",
                "actions": ["whispers the answer in your ear!", "solves the puzzle with cunning!", "finds a clever loophole!"],
                "bonus": "riddle_help",
                "color": Fore.GREEN
            }
        }
        
        self.shop_items = {
            "Health Potion": {"price": 25, "effect": "Restores 20 sanity"},
            "Strength Elixir": {"price": 40, "effect": "Boosts score by 30"},
            "Courage Amulet": {"price": 50, "effect": "Prevents sanity loss for 1 path"},
            "Lucky Coin": {"price": 35, "effect": "Double points on next mini-game"},
            "Magic Scroll": {"price": 60, "effect": "Unlock secret path"}
        }
        
    def typewriter(self, text, color=Fore.WHITE):
        for char in text:
            print(color + char, end='', flush=True)
            time.sleep(0.02)
        print(Style.RESET_ALL)
    
    def clear_screen(self):
        print("\n" * 2)
    
    def show_fire_animation(self):
        """Phoenix fire animation"""
        frames = [
            """
                  *
                 / \\
                /   \\
               |  🔥  |
               |      |
            """,
            """
                 * *
                / | \\
               /  |  \\
              |  🔥🔥  |
              |        |
            """,
            """
               * * * *
              /   |   \\
             /    |    \\
            |   🔥🔥🔥   |
            |           |
            """,
            """
                * * *
               /   |   \\
              |   🔥🔥   |
              |    |     |
            """
        ]
        
        for frame in frames:
            self.clear_screen()
            print(Fore.RED + frame + Style.RESET_ALL)
            time.sleep(0.3)
    
    def show_magic_animation(self):
        """Magic spell animation"""
        frames = [
            """
                  ✨
                 
            """,
            """
                 ✨ ✨
                  ✨
            """,
            """
               ✨ ✨ ✨
                ✨ ✨
               ✨ ✨ ✨
            """,
            """
              ✨     ✨
               ✨ ✨ ✨
              ✨     ✨
            """,
            """
                ✨ ✨
                  ✨
                ✨ ✨
            """
        ]
        
        for frame in frames:
            self.clear_screen()
            print(Fore.MAGENTA + frame + Style.RESET_ALL)
            time.sleep(0.2)
    
    def show_lightning_animation(self):
        """Storm Dragon lightning animation"""
        frames = [
            """
               ⚡
                
            """,
            """
               ⚡ ⚡
                ⚡
            """,
            """
              ⚡ ⚡ ⚡
               ⚡ ⚡
              ⚡ ⚡ ⚡
            """,
            """
              ⚡   ⚡
               ⚡ ⚡
              ⚡   ⚡
            """,
            """
                ⚡
            """
        ]
        
        for frame in frames:
            self.clear_screen()
            print(Fore.YELLOW + frame + Style.RESET_ALL)
            time.sleep(0.2)
    
    def show_dancing_animation(self):
        """Dancing animation"""
        frames = [
            """
               \\o/
                |
               /|\\
            """,
            """
               o/
               /|
               | \\
            """,
            """
              \\o
               |\\
              /| 
            """,
            """
               /o\\
               |
              / \\
            """,
            """
              o/
             /|
            / |\\
            """
        ]
        
        for frame in frames:
            self.clear_screen()
            print(Fore.CYAN + frame + Style.RESET_ALL)
            time.sleep(0.25)
    
    def show_ghost_animation(self):
        """Ghost floating animation"""
        frames = [
            """
              👻
               
            """,
            """
                👻
               
            """,
            """
               👻
                
            """,
            """
              👻
               
            """,
            """
                 👻
            """
        ]
        
        for frame in frames:
            self.clear_screen()
            print(Fore.WHITE + frame + Style.RESET_ALL)
            time.sleep(0.3)
    
    def show_victory_animation(self):
        """Victory celebration animation"""
        frames = [
            """
                ✨
               \\o/
                |
               / \\
            """,
            """
              ✨ ✨
              \\o /
               |
              / \\
            """,
            """
            ✨ ✨ ✨
             \\o/
              |
             / \\
            """,
            """
              ✨ ✨
               \\o/
                |
               / \\
            """
        ]
        
        for frame in frames:
            self.clear_screen()
            print(Fore.GREEN + frame + Style.RESET_ALL)
            time.sleep(0.3)
    
    def show_defeat_animation(self):
        """Defeat animation"""
        frames = [
            """
              \\o/
               |
              / \\
            """,
            """
              \\o
               |
              / \\
            """,
            """
               o
               |
              / \\
            """,
            """
              
               o
              /|\\
            """,
            """
              
               o
              / \\
            """
        ]
        
        for frame in frames:
            self.clear_screen()
            print(Fore.RED + frame + Style.RESET_ALL)
            time.sleep(0.4)
    
    def randomize_companion(self):
        """Randomly select a companion"""
        self.companion = random.choice(list(self.companions.keys()))
        companion_color = self.companions[self.companion]["color"]
        
        self.companion_name = input(f"\n{companion_color}🐾 Your companion is a {self.companion}! What would you like to name them? > {Style.RESET_ALL}").strip() or self.companion
        
        companion_info = self.companions[self.companion]
        emoji = companion_info["emoji"]
        description = companion_info["description"]
        
        print(f"\n{companion_color}{emoji} {self.companion_name} the {self.companion}!")
        self.typewriter(f"Description: {description}\n", companion_color)
    
    def customize_character(self):
        """Character customization menu"""
        print("\n" + "="*60)
        self.typewriter("✨ CHARACTER CUSTOMIZATION ✨", Fore.CYAN)
        print("="*60)
        
        # Character Name
        self.name = input(f"\n{Fore.YELLOW}🌸 What is your name, adventurer? > {Style.RESET_ALL}").strip() or "Adventurer"
        
        # Character Class Selection
        print(f"\n{Fore.MAGENTA}🎭 Choose your character class:{Style.RESET_ALL}")
        print(f"{Fore.BLUE}1. 🗡️  Warrior - High Sanity, Low Score (Brave)")
        print(f"2. 🧙 Mage - High Score, Low Sanity (Magical)")
        print(f"3. 🏹 Rogue - Balanced Stats (Clever){Style.RESET_ALL}")
        
        class_choice = input(f"\n{Fore.GREEN}Choose (1-3) > {Style.RESET_ALL}").strip()
        
        if class_choice == "1":
            self.character_class = "Warrior"
            self.sanity = 130
            self.typewriter("\n⚔️ You are a brave Warrior! (+30 Sanity)", Fore.BLUE)
        elif class_choice == "2":
            self.character_class = "Mage"
            self.score = 50
            self.sanity = 70
            self.typewriter("\n🧙 You are a skilled Mage! (+50 Initial Score, -30 Sanity)", Fore.MAGENTA)
            self.show_magic_animation()
        elif class_choice == "3":
            self.character_class = "Rogue"
            self.gold = 150
            self.typewriter("\n🏹 You are a clever Rogue! (+50 Gold)", Fore.GREEN)
        else:
            self.character_class = "Rogue"
            self.gold = 150
            self.typewriter("\n🏹 You are a clever Rogue! (+50 Gold)", Fore.GREEN)
        
        time.sleep(1)
        
        # Companion Randomizer
        print("\n" + "="*60)
        self.typewriter("🐾 RANDOMIZING YOUR COMPANION... 🐾\n", Fore.CYAN)
        time.sleep(1)
        self.randomize_companion()
        
        time.sleep(1)
        self.typewriter(f"\nWelcome {self.name} the {self.character_class} and {self.companion_name}! Your adventure begins...\n", Fore.YELLOW)
        time.sleep(1)
        
        self.main_menu()
    
    def companion_action(self):
        """Display a random companion action"""
        companion_info = self.companions[self.companion]
        emoji = companion_info["emoji"]
        color = companion_info["color"]
        actions = companion_info["actions"]
        action = random.choice(actions)
        
        print(f"\n{color}{emoji} {self.companion_name} {action}{Style.RESET_ALL}")
        return companion_info["bonus"]
    
    def main_menu(self):
        while True:
            print("\n" + "="*60)
            companion_emoji = self.companions[self.companion]["emoji"]
            print(f"{Fore.YELLOW}💰 Gold: {self.gold} | {Fore.CYAN}Score: {self.score} | {Fore.RED}Sanity: {self.sanity}/130{Style.RESET_ALL} | {companion_emoji} {self.companion_name}")
            print("="*60)
            print(f"{Fore.LIGHTBLUE_EX}CHOOSE YOUR PATH:")
            print(f"{Fore.GREEN}1. 🌲 Explore the Enchanted Forest")
            print(f"{Fore.YELLOW}2. 🏪 Visit the Magical Marketplace")
            print(f"{Fore.MAGENTA}3. ⛰️  Climb the Mysterious Mountain")
            print(f"{Fore.CYAN}4. 👑 Attend the Royal Ball")
            print(f"{Fore.WHITE}5. 👻 Investigate the Haunted Ruins")
            print(f"{Fore.LIGHTMAGENTA_EX}6. 🛍️  Visit the Shop")
            print(f"{Fore.LIGHTCYAN_EX}7. 📊 Check Your Stats")
            print(f"{Fore.RED}8. 🚪 Exit Game{Style.RESET_ALL}")
            print("="*60)
            
            choice = input(f"\n{Fore.LIGHTGREEN_EX}{self.name}, choose (1-8) > {Style.RESET_ALL}").strip()
            
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
                self.shop()
            elif choice == "7":
                self.show_stats()
            elif choice == "8":
                self.end_game()
                break
            else:
                print(f"{Fore.RED}Invalid choice! Try again.{Style.RESET_ALL}")
    
    def shop(self):
        """Shop to buy items"""
        print(f"\n{Fore.LIGHTMAGENTA_EX}🛍️ " + "="*56)
        self.typewriter("Welcome to the Magical Shop!", Fore.LIGHTMAGENTA_EX)
        print(f"{Fore.YELLOW}Your Gold: {self.gold}\n{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}Available Items:{Style.RESET_ALL}")
        
        for i, (item_name, item_info) in enumerate(self.shop_items.items(), 1):
            print(f"{Fore.GREEN}{i}. {item_name}{Style.RESET_ALL} - {Fore.YELLOW}{item_info['price']} gold{Style.RESET_ALL} ({item_info['effect']})")
        
        print(f"{Fore.RED}{len(self.shop_items) + 1}. Leave Shop{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.LIGHTGREEN_EX}Choose item (1-{len(self.shop_items) + 1}) > {Style.RESET_ALL}").strip()
        
        try:
            choice = int(choice)
            if choice == len(self.shop_items) + 1:
                return
            
            if 1 <= choice <= len(self.shop_items):
                item_name = list(self.shop_items.keys())[choice - 1]
                item_price = self.shop_items[item_name]["price"]
                item_effect = self.shop_items[item_name]["effect"]
                
                if self.gold >= item_price:
                    self.gold -= item_price
                    self.inventory.append(item_name)
                    self.show_magic_animation()
                    self.typewriter(f"\n✓ You bought {item_name}!", Fore.GREEN)
                    self.typewriter(f"Effect: {item_effect}\n", Fore.CYAN)
                    
                    # Apply item effects
                    if "Health" in item_name:
                        self.sanity += 20
                    elif "Strength" in item_name:
                        self.score += 30
                else:
                    self.typewriter(f"\n✗ Not enough gold! (Need {item_price}, Have {self.gold})", Fore.RED)
        except:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
    
    def forest_path(self):
        print(f"\n{Fore.GREEN}🌲 " + "="*56)
        self.typewriter("You enter a mystical forest filled with glowing mushrooms...", Fore.GREEN)
        bonus = self.companion_action()
        print(f"{Fore.LIGHTBLUE_EX}A fairy appears and challenges you to a riddle!\n")
        
        riddle = "I have cities but no houses, forests but no trees, and water but no fish. What am I?"
        print(f"{Fore.YELLOW}Fairy's Riddle: {riddle}\n{Style.RESET_ALL}")
        
        answer = input(f"{Fore.LIGHTGREEN_EX}Your answer? > {Style.RESET_ALL}").strip().lower()
        
        points = 50
        if self.character_class == "Mage":
            points = 75
        
        if "map" in answer:
            self.show_victory_animation()
            self.typewriter("\n✓ CORRECT! The fairy gives you a magical map!", Fore.GREEN)
            if bonus == "score":
                points += 25
                self.typewriter(f"✨ Your companion helped! +25 bonus points!", Fore.CYAN)
            self.inventory.append("Magical Map")
            self.score += points
            self.gold += 15
        else:
            self.show_defeat_animation()
            self.typewriter(f"\n✗ Wrong! The answer was 'map'.", Fore.RED)
            self.sanity -= 10
        
        print(f"{Fore.YELLOW}Score: {self.score} | {Fore.RED}Sanity: {self.sanity} | {Fore.CYAN}Gold: {self.gold}{Style.RESET_ALL}")
        time.sleep(1)
    
    def marketplace_path(self):
        print(f"\n{Fore.LIGHTMAGENTA_EX}🏪 " + "="*56)
        self.typewriter("You arrive at a magical marketplace!", Fore.LIGHTMAGENTA_EX)
        bonus = self.companion_action()
        print(f"{Fore.YELLOW}A merchant challenges you to a bargaining game!\n{Style.RESET_ALL}")
        
        gold_reward = 20
        if self.character_class == "Rogue":
            gold_reward = 40
        
        for attempt in range(3):
            try:
                offer = int(input(f"{Fore.LIGHTGREEN_EX}Attempt {attempt + 1}/3 - Offer (1-100): > {Style.RESET_ALL}"))
                if offer >= 80:
                    self.show_magic_animation()
                    self.typewriter("\n✓ The merchant accepts!", Fore.GREEN)
                    if bonus == "gold":
                        gold_reward += 25
                        self.typewriter(f"✨ Your companion negotiated better! +25 gold bonus!", Fore.CYAN)
                    self.inventory.append("Magical Potion")
                    self.score += 60
                    self.gold += gold_reward
                    break
                else:
                    print(f"{Fore.YELLOW}Merchant: That's too low. Try again.{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
        
        print(f"{Fore.YELLOW}Score: {self.score} | {Fore.RED}Sanity: {self.sanity} | {Fore.CYAN}Gold: {self.gold}{Style.RESET_ALL}")
        time.sleep(1)
    
    def mountain_path(self):
        print(f"\n{Fore.LIGHTYELLOW_EX}⛰️ " + "="*56)
        self.typewriter("You climb a misty mountain. A stone guardian appears!", Fore.LIGHTYELLOW_EX)
        bonus = self.companion_action()
        
        if self.companion == "Storm Dragon":
            self.show_lightning_animation()
        
        print(f"{Fore.LIGHTBLUE_EX}Guardian: What gets wet while drying? > {Style.RESET_ALL}", end="")
        answer = input().strip().lower()
        
        points = 70
        if self.character_class == "Warrior":
            points = 100
        
        if "towel" in answer:
            self.show_victory_animation()
            self.typewriter("\n✓ Correct! The guardian moves aside!", Fore.GREEN)
            if bonus == "riddle_help":
                points += 50
                self.typewriter(f"✨ Your companion's wisdom helped! +50 bonus points!", Fore.CYAN)
            self.inventory.append("Rare Gem")
            self.score += points
            self.gold += 25
        else:
            self.show_defeat_animation()
            self.typewriter(f"\n✗ Wrong! The answer was 'towel'.", Fore.RED)
            self.sanity -= 20
        
        print(f"{Fore.YELLOW}Score: {self.score} | {Fore.RED}Sanity: {self.sanity} | {Fore.CYAN}Gold: {self.gold}{Style.RESET_ALL}")
        time.sleep(1)
    
    def ball_path(self):
        print(f"\n{Fore.LIGHTCYAN_EX}👑 " + "="*56)
        self.typewriter("You arrive at a grand royal ball!", Fore.LIGHTCYAN_EX)
        bonus = self.companion_action()
        self.show_dancing_animation()
        print(f"{Fore.LIGHTBLUE_EX}DANCE CHALLENGE - Follow the pattern:\n{Style.RESET_ALL}")
        
        pattern = ["UP", "DOWN", "LEFT", "RIGHT", "SPIN"]
        correct = 0
        
        for i, move in enumerate(pattern, 1):
            player_input = input(f"{Fore.LIGHTGREEN_EX}Move {i} (type '{move}'): > {Style.RESET_ALL}").strip().upper()
            if player_input == move:
                print(f"{Fore.GREEN}✓ Perfect!{Style.RESET_ALL}")
                correct += 1
            else:
                print(f"{Fore.RED}✗ Wrong!{Style.RESET_ALL}")
        
        if correct >= 4:
            self.show_victory_animation()
            self.typewriter("\n✓ Great dancing! Everyone applauds!", Fore.GREEN)
            if bonus == "score":
                self.typewriter(f"✨ Your companion danced with you! +30 bonus points!", Fore.CYAN)
                self.score += 30
            self.inventory.append("Royal Recognition")
            self.score += 80
            self.gold += 30
        else:
            self.show_defeat_animation()
        
        print(f"{Fore.YELLOW}Score: {self.score} | {Fore.RED}Sanity: {self.sanity} | {Fore.CYAN}Gold: {self.gold}{Style.RESET_ALL}")
        time.sleep(1)
    
    def ruins_path(self):
        print(f"\n{Fore.WHITE}👻 " + "="*56)
        self.typewriter("A ghostly figure appears!", Fore.WHITE)
        self.show_ghost_animation()
        bonus = self.companion_action()
        print(f"{Fore.LIGHTBLUE_EX}Ghost: I grow but am not alive. I need air but have no lungs. What am I? > {Style.RESET_ALL}", end="")
        answer = input().strip().lower()
        
        if "fire" in answer:
            self.show_victory_animation()
            self.typewriter("\n✓ Correct! The ghost rewards you!", Fore.GREEN)
            if bonus == "sanity":
                self.sanity += 20
                self.typewriter(f"✨ Your companion protected you! +20 sanity!", Fore.CYAN)
            self.inventory.append("Ghost's Treasure")
            self.score += 100
            self.gold += 50
        else:
            self.show_defeat_animation()
            self.typewriter(f"\n✗ Wrong! The answer was 'fire'.", Fore.RED)
            self.sanity -= 30
        
        print(f"{Fore.YELLOW}Score: {self.score} | {Fore.RED}Sanity: {self.sanity} | {Fore.CYAN}Gold: {self.gold}{Style.RESET_ALL}")
        time.sleep(1)
    
    def show_stats(self):
        companion_emoji = self.companions[self.companion]["emoji"]
        companion_color = self.companions[self.companion]["color"]
        print(f"\n{Fore.LIGHTCYAN_EX}" + "="*60)
        print(f"{Fore.LIGHTGREEN_EX}⭐ {self.name} the {self.character_class}'s STATS ⭐")
        print(f"{Fore.LIGHTMAGENTA_EX}Companion: {companion_color}{companion_emoji} {self.companion_name} the {self.companion}")
        print(f"{Fore.LIGHTYELLOW_EX}Score: {self.score}")
        print(f"{Fore.LIGHTRED_EX}Sanity: {self.sanity}/130")
        print(f"{Fore.LIGHTBLUE_EX}Gold: {self.gold}")
        print(f"{Fore.LIGHTGREEN_EX}Items: {', '.join(self.inventory) if self.inventory else 'None'}")
        print(f"{Fore.LIGHTCYAN_EX}" + "="*60 + f"{Style.RESET_ALL}")
    
    def end_game(self):
        companion_emoji = self.companions[self.companion]["emoji"]
        companion_color = self.companions[self.companion]["color"]
        self.show_victory_animation()
        print(f"\n{Fore.LIGHTGREEN_EX}" + "="*60)
        print(f"{Fore.LIGHTGREEN_EX}Thank you for playing, {self.name} the {self.character_class}!")
        print(f"{companion_color}Companion: {companion_emoji} {self.companion_name}")
        print(f"{Fore.LIGHTYELLOW_EX}Final Score: {self.score}")
        print(f"{Fore.LIGHTRED_EX}Final Sanity: {self.sanity}/130")
        print(f"{Fore.LIGHTBLUE_EX}Gold Remaining: {self.gold}")
        if self.inventory:
            print(f"{Fore.LIGHTGREEN_EX}Items Collected: {', '.join(self.inventory)}")
        print(f"{Fore.LIGHTGREEN_EX}" + "="*60 + f"{Style.RESET_ALL}")

if __name__ == "__main__":
    game = AdventureGame()
    game.customize_character()
