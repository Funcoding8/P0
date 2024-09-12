class character:


    def __init__character(self, name, health, attack,inventory):
        self.name = name
        self.health = health
        self.attack = attack
        self.dialogue = []
        self.inventory = inventory

    def talk_to_Player(self, player):
        for sentence in self.sentences:
            if player == sentence:
                print(self.dialogue[sentence])

    def receive_inventory(self, item):
        self.inventory.append(item)

    def attack_player(self, player):
        player.health -= self.attack
        print(f"{self.name} attacked {player.name} for {self.attack} damage!")
    
    