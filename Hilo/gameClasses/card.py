import random

class Card:
    """The responsibilty of this class is to give the director a random card.
    
    Attributes:
        card_value: This is the face value of the card from 1-13
        
    Methods:
        value: return the value of the last card drawn. (card_value)
        
        draw: This generates the random value from 1-13, stores in card value. 
            return: card_value
            """

    """value: This is the face value of the card from 1-13"""

    def __init__(self):    
        """Constructs a new instance of Die with a value attribute.
        
        Args:
            self (Die): An instance of Die."""

        self.value = 0

        
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Die): An instance of Die."""

        self.value = random.randint(1, 13)
        return self.value
        
