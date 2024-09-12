class item:
    def __init__(self, name, description, point):
        self.name = name
        self.description = description
        self.point = point
    
    def use_item(self, player):
        if self.name == 0:
            player.health += self.point
            print(f"You used the {self.name} and gained {self.point} health.")
        elif self.name == "sword":
            player.attack += self.point
            print(f"You used the {self.name} and gained {self.point} attack power.")
        elif self.name == "shield":
            player.defense += self.point
            print(f"You used the {self.name} and gained {self.point} defense.")
        elif self.name == "joker":
            print(f"You used the Joker card. It can mimic any other item's effect!")
            # Add specific Joker card functionality here
        else:
            print(f"You don't have a {self.name} to use.")

# Add Joker card
joker_card = item("joker", "A wild card that can mimic any other item's effect", 0)
