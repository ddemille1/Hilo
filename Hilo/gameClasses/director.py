from gameClasses.card import Card

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes: 
        points: how many points the player has aquired during game play. It will start at 300.
        
        is_playing: a boolean variable. True means still playing, False means not playing.
        
        choice: If the player has chosen the next card to be higher lower than the current card.
        
        """
    def __init__(self):
        """Constructs a new director.
        
        Arguments: 
            self (Director): an instance of Director"""
        
        self.points = 0
        self.is_playing: True
        self.choice = ''
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Arguments: 
            self (Director): an instance of Director"""
        while self.is_playing == True:
            self.display_current_card()
            self.get_choice()
            self.display_next_card()
            self.assign_points()
            self.display_output()

    
    
    def display_current_card(self):
        """first_display: displays the value of the current card in play.
        
        Arguments: 
            self (Director): an instance of Director"""
        card = Card()
        value = card.value
        print(f'The card is: {value}')

    def get_choice(self):    
        """Gets 'choice' from user.
        
        Arguments: 
            self (Director): an instance of Director"""

        self.choice = input('Higher or lower? [h/l] ')

    def display_next_card(self):
        """Gets new card from card object
        
        Arguments: 
            self (Director): an instance of Director"""
        next_card = Card()
        next_value = next_card.value
        print(f'Next card was: {next_value}')
 
    
    
    
    
    
    """Things should be good up to here"""
    
    def calculate_points(value, next_value, choice):
        """calculates the points earned this round.
        
        Arguments: 
            self (Director): an instance of Director
            
            value: the value of the first card
            
            next_value: the value of the next card
            
            choice: the players choice if the next card will be higher or lower than the first card."""
    points = 0
    value 
    if value > next_value and choice == 'h':
        points = 
"""Methods: 
  
        
        calculate_points: This assigns 100 points if the player was correct in guessing if the new card was higher or lower than the previous card.     
            Arguments: are value (from the card's attributes) and is_playing (from the director's attribures)

            return: points

        display_output: displays new card, displays updated points."""