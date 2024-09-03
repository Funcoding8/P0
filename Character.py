class character:


    def __init__(self, name, health, attack, dialogue,inventory):
        self.name = name
        self.health = health
        self.attack = attack
        self.dialogue = dialogue
        self.inventory = inventory

    def talk_to_Payer(self, player):
        for sentence in self.sentences:
            if player == sentence:
                print(self.dialogue[sentence])

    def receive_inventory(self, item):
        self.inventory.append(item)