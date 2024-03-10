# Build a landscaper game - psuedo code

# Game state (Player dictionary)

player = {
    "money": 0,
    "equipment": 0
}

# Location - use this as a stretch to mow lawns in different places

# Weapons list (How does the player level up)

equipment = [
    {"name": "Teeth", "price": 0, "money": 1},
    {"name": "Rusty Scissors", "price": 5, "money": 5},
    {"name": "Old Timey Push mower", "price": 25, "money": 50},
    {"name": "Fancy Battery Powered Lawnmower", "price": 250, "money": 100},
    {"name": "Starving Students", "price": 500, "money": 250}
]

# Create the character CLASS for the player
class Character:

    # define constructor
    def __init__(self, name):
        
        # define your name
        self.name = name
        self.money = 0
        self.equipment = 0
    # function for mowing the lawn
    def mow(self, lawn):
        # if teeth get 1
        if self.equipment == 0:
            self.money += 1
        # if Rusty Scissors get 5
        elif self.equipment == 1:
            self.money += 5
        # push mower
        elif self.equipment == 2:
            self.money += 50
        # battery mower
        elif self.equipment == 3:
            self.money += 100
        elif self.equipment == 4:
            self.money += 250
        print(f"{self.name} has mowed 1 lawn with {equipment[self.equipment]["name"]} and received ${self.money}")
    # function for upgrading
    def upgrade(self):
        if self.equipment < len(equipment) -1:
            self.equipment += 1
            print(f"{self.name} upgraded to {equipment[self.equipment]["name"]}")
    # function for winning
    def win(self):
        if (self.equipment == 4 and self.money >= 1000):
            print(f"Congratulations, {self.name}'s mowing business rules the block. You win")
            return True
        return False
    # function for restarting
    def restart(self):
        self.money = 0
        self.equipment = 0
        print(f"{self.name} has restarted the game. You now have ${self.money} and your tool is {equipment[self.equipment]["name"]}")
        

        

# Create a character CLASS for the lawn
class Lawn:

    # define constructor
    def __init__(self):
        self.money = 1


# General functions
    

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
    choice = input(f"Hi {player.name}! Do you want to [m]ow the lawn, [u]grade your equipment, [q]uit, or [r]estart")

    # choice to mow
    if (choice == "m"):
        player.mow(lawn)


    # choice to upgrade
    if (choice == "u"):
        player.upgrade()

    # choice to quit
    if (choice == "q"):
        print("No mowing today")
        break

    # win condition
    if player.win():
        break

    # restart condition
    if (choice == "r"):
        player.restart()