from gameClasses.card import Card

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes: 
        value: the number on the first card in the round

        next_value: the number on the next card in the round.

        points: how many points the player has aquired during game play. It will start at 300.
        
        is_playing: a boolean variable. True means still playing, False means not playing.
        
        choice: If the player has chosen the next card to be higher lower than the current card.
        
        """
    def __init__(self):
        """Constructs a new director.
        
        Arguments: 
            self (Director): an instance of Director"""
        
        card = Card()
        self.value = card.draw()
        self.next_value = 0
        self.points = 300
        self.is_playing = True
        self.choice = ''
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Arguments: 
            self (Director): an instance of Director"""
        
        while (self.is_playing == True and self.points > 0):
            self.display_current_card()
            self.get_choice()
            self.display_next_card()
            self.calculate_points()
            self.display_output()

    
    
    def display_current_card(self):
        """first_display: displays the value of the current card in play.
        
        Arguments: 
            self (Director): an instance of Director"""
        
        print(f'The card is: {self.value}')

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
        self.next_value = next_card.draw()
        print(f'Next card was: {self.next_value}')
    
    def calculate_points(self):
        """calculates the points earned this round. Adds 100 points if player guessed correctly if the next card was higher or lower than the previous card. Deducts 75 points from players score if the player guessed wrong.
        
        Arguments: 
            self (Director): an instance of Director"""
 
        if self.value > self.next_value and self.choice == 'h':
            self.points = self.points - 75
            return

        if self.value < self.next_value and self.choice == 'h':
            self.points = self.points + 100
            return

        if self.value > self.next_value and self.choice == 'l':
            self.points = self.points + 100
            return

        if self.value < self.next_value and self.choice == 'l':
            self.points = self.points - 75
            return


    def display_output(self):
        """display_output: displays updated points, asks if playing again, resets value to current,value (so next round will start out using previous rounds new card)
        
        Arguments: 
            self (Director): an instance of Director"""
        

        print(f'Your score is: {self.points}')
        play_again = input('Play again? [y/n] ')
        print('')
        if play_again == 'y':
            self.is_playing = True
            self.value = self.next_value
            return
        
        if play_again == 'n':
            self.is_playing = False
            return
        
        
        
