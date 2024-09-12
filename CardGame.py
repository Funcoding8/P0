class CardGame:

    """
    Imports the random module, which provides functions for generating random numbers and making random selections.
    """
    import random

    def initialize_game():
        """Initialize the game with a list of four cards, two pairs."""
        cards = ['A', 'A', 'B', 'B']
        random.shuffle(cards)
        card_state = {i: False for i in range(4)}
        return cards, card_state

    def display_cards(cards, card_state):
        """Display the current state of the cards."""
        display = []
        for index, card in enumerate(cards):
            if card_state[index]:
                display.append(card) 
            else:
                display.append('*')   
        print("Cards: ", ' '.join(display))

    def check_for_match(cards, card_state, first_choice, second_choice):
        """Check if the chosen cards match."""
        if cards[first_choice] == cards[second_choice]:
            print("It's a match!")
            card_state[first_choice] = True
            card_state[second_choice] = True
        else:
            print("Not a match. Try again!")

    def game_loop():
        """Main game loop."""
        cards, card_state = initialize_game()
        attempts = 0

        while not all(card_state.values()):
            display_cards(cards, card_state)
            try:
            
                first_choice = int(input("Pick the first card to flip (0-3): "))
                second_choice = int(input("Pick the second card to flip (0-3): "))
                
            
                if first_choice < 0 or first_choice > 3 or second_choice < 0 or second_choice > 3:
                    print("Invalid input. Please choose a number between 0 and 3.")
                    continue
                if first_choice == second_choice:
                    print("You must pick two different cards!")
                    continue
                if card_state[first_choice] or card_state[second_choice]:
                    print("One or both cards are already face up. Choose again.")
                    continue

                
                check_for_match(cards, card_state, first_choice, second_choice)
                attempts += 1
            
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        print(f"Congratulations! You've matched all cards in {attempts} attempts.")
        print("Your Prize is a Joker card!")

    game_loop()
