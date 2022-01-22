import random

class Card:
    """A playing card with values.

    The responsibility of Card is pick a random number card.
   
    Attributes:
        value (int): The number shown on the card.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def pick(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)