from gameClasses.card import Card

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes: 
        value: the number on the first card in the round

        next_value: the number on the next card in the round.

        points: how many points the player has aquired during game play. It will start at 300.
        
        is_playing: a boolean variable. True means still playing, False means not playing.
        
        choice: If the player has chosen the next card to be higher or lower than the current card.

        
        get_input: gets 'is_playing' and 'choice' from user.
            return: is_playing

        take_turn: draw a new card, compare to provious card to choice. 
            return: win or lose

        update_score: updates points from win or lose. 

        display_output: displays new card, displays updated points.
        return: points
        """

   
    def __init__(self):
        """Constructs a new director.
        
        Arguments: 
            self (Director): an instance of Director"""
        
        self.initial_stake = 300
        card = Card()
        self.value = card.draw()
        self.next_value = 0
        self.points = self.initial_stake
        self.is_playing = True
        self.choice = ''
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Arguments: 
            self (Director): an instance of Director"""
        print(f"Your starting score is: {self.points}")
        while (self.is_playing == True and self.points > 0):
            self.display_current_card()
            self.get_choice()
            self.display_next_card()
            self.calculate_points()
            self.display_output()
        
        print('Game over. Thanks for playing.')
        if self.points < self.initial_stake:
            loss = self.initial_stake - self.points
            print (f"You lost {loss}. Better luck next time.")

        else:
            gain = self.points - self.initial_stake
            print(f"Congratulations, you won {gain}.")
    
    
    def display_current_card(self):
        """first_display: displays the value of the current card in play.
        
        Arguments: 
            self (Director): an instance of Director"""
        
        print(f'The card is: {self.value}')

    def get_choice(self):    
        """Gets 'choice' from user.
        
        Arguments: 
            self (Director): an instance of Director"""
        self.choice = input('Higher or lower? [h/l] ').lower()
        while self.choice != "h" and self.choice != "l":
            self.choice = input('Invalid choice. Higher or lower? [h/l] ').lower()

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

            self (Director): an instance of Director

        if self.choice == "h":
                if self.next_value > self.value:
                    self.points += 100
                else:
                    self.points -= 75
        elif self.choice == "l":
                if self.next_value < self.value:
                    self.points += 100
                else:
                    self.points -=75


    def display_output(self):
        """display_output: displays updated points, asks if playing again, resets value to current,value (so next round will start out using previous rounds new card)
        
        Arguments: 
            self (Director): an instance of Director"""
        

        print(f'Your score is: {self.points}')
        play_again = input('Play again? [y/n] ').lower()
        while play_again != "y" and play_again != "n":
            play_again = input('Invalid choice. Play again? [y/n] ').lower()
        print('')
        if play_again == 'y':
            self.is_playing = True
            self.value = self.next_value
            return
        
        if play_again == 'n':
            self.is_playing = False
            return
        
        
       
