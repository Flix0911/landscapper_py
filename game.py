# Build a landscaper game - psuedo code

# Game state (Player dictionary)

player = {
    "money": 0,
    "equipment": 0
}

# Location - use this as a stretch to mow lawns in different places

# Weapons list (How does the player level up)

equipment = [
    {"name": "Teeth", "price": 0, "money": 1}
]

# Create the character CLASS for the player
class Character:

    # define constructor
    def __init__(self, name):
        
        # define your name
        self.name = name
        self.money = 0
    def mow(self, lawn):
        self.money += 1
        print(f"{self.name} has mowed 1 lawn and received ${self.money}")

# Create a character CLASS for the lawn
class Lawn:

    # define constructor
    def __init__(self):
        self.money = 1

# General functions
        
# mowing function


    # Win condition

# Game set up 
player_name = input("Welcome to the mow gang, what is your name")

# take Character class and create a player
player = Character(player_name)

lawn = Lawn()

# Loop for the game

    # Input loops
while(True):
    # text for input
    choice = input(f"Hi {player.name}! Do you want to [m]ow the law or [q]uit")

    # choice to mow
    if (choice == "m"):
        player.mow(lawn)


    # choice to upgrade

    # choice to quit
    if (choice == "q"):
        print("No mowing today")
        break