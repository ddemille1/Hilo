import random

class Card:
    """This is where we create the card object
    
    Attributes:
        value: This is the face value of the card from 1-13
        
    Methods:
        drawCard: This generates the random value from 1-13
            return: value"""
    def __init__(self):    
        """Constructs a new instance of Die with a value and points attribute.
        Args:
            self (Die): An instance of Die.
        """
        self.value = 0

# 3) Create the roll(self) method. Use the following method comment.
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
    def draw(self):
        self.value = random.randint(1, 13)
        return self.value
        

#card = Card()
#value = card.value
#random = card.draw()

#print(value)
#print(random)
