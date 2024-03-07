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

# Create the character CLASS

    # define constructor

    # define the action of mowing the lawn
        # What do you earn from mowing the lawn and where does it tabulate your earnings

# General functions

    # Win condition

    # Game set up 

# Loop for the game

    # Input loops
while(True):
    # text for input
    choice = input("Do you want to [m]ow the law or [q]uit")

    # choice to mow
    if (choice == "m"):
        pass
    # choice to upgrade

    # choice to quit
    if (choice == "q"):
        print("No mowing today")
        break