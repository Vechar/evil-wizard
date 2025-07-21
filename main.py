import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = round(self.attack_power * random.uniform(0.8, 1.2))  # Randomize attack damage +- 20%
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    def heal(self):
        heal_amount = round(self.max_health * 0.15 * random.uniform(0.8, 1.2))  # Heal 15% of max health, randomized
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name, evaded=False):
        super().__init__(name, health=120, attack_power=30)
        self.evaded = evaded  # Track if the Archer has evaded an attack
        
    def quick_shot(self, opponent):
        damage = round(self.attack_power * random.uniform(0.8, 1.2) * 0.3)  # Randomize attack damage +- 20%, also, each shot is 30% less powerful
        opponent.health -= damage
        print(f"{self.name} performs a quick shot on {opponent.name} for {damage} damage!")
        
        damage = round(self.attack_power * random.uniform(0.8, 1.2) * 0.3)  # Randomize attack damage +- 20%, also, each shot is 30% less powerful
        opponent.health -= damage
        print(f"{self.name} performs a quick shot on {opponent.name} for {damage} damage!")
        
    def evade(self):
        chance_to_evade = random.random()
        self.evaded = False
        if chance_to_evade < 0.7:  # 70% chance to evade
            self.evaded = True
        else:
            self.evaded = False
            
        print(f"{self.name} attempts to evade the attack!")


# Create Paladin class 
class Paladin(Character):
    def __init__(self, name, blocked=False):
        super().__init__(name, health=200, attack_power=20)
        self.blocked = blocked  # Track if the Paladin has blocked an attack
        
    def holy_strike(self, opponent):
        damage = round(self.attack_power * random.uniform(0.8, 1.2) * 1.5)  # Randomize attack damage +- 20%, also, each shot is 50% more powerful
        opponent.health -= damage
        print(f"{self.name} performs a Holy Strike on {opponent.name} for {damage} damage!")
        
    def block(self):
        chance_to_block = random.random()
        self.blocked = False
        if chance_to_block < 0.7:  # 70% chance to block
            self.blocked = True
        else:
            self.blocked = False
            
        print(f"{self.name} attempts to block the attack!")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    
    turn_counter = 0
    print(f"\n{wizard.name} appears! Prepare for battle!")
    
    while wizard.health > 0 and player.health > 0:
        turn_counter += 1
        print(f"\n--- Turn {turn_counter} ---")
        
        print("\n--- Your Turn ---")
        print(f"Health: {player.health}")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                ability_choice = input("Choose ability: \n1. Quick Shot \n2. Evade \n> ")
                if ability_choice == '1':
                    player.quick_shot(wizard)
                elif ability_choice == '2':
                    player.evade()
                    
            elif isinstance(player, Paladin):
                ability_choice = input("Choose ability: \n1. Holy Strike \n2. Divine Shield \n> ")
                if ability_choice == '1':
                    player.holy_strike(wizard)
                elif ability_choice == '2':
                    player.block()

        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            print("\n--- Enemy Turn ---")
            if random.random() < 0.75:
                wizard.regenerate()
                
            if isinstance(player, Archer) and player.evaded == True:
                print(f"{wizard.name}'s attack was evaded!")
                player.evaded = False

                
            if isinstance(player, Paladin) and player.blocked == True:
                print(f"{wizard.name}'s attack was blocked!")
                player.blocked = False
            
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated! \nGame Over!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()

