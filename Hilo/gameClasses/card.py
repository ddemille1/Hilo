class Card:
    """This is where we create the card object
    
    Attributes:
        value: This is the face value of the card from 1-13
        
    Methods:
        drawCard: This generates the random value from 1-13
            return: value
        
        assignPoints: This assigns 100 points if the player was correct in guessing if the new card was higher or lower than the previous card.     
            Arguments: are value (from the card's attributes) and is_playing (from the director's attribures)

            return: points
            """
