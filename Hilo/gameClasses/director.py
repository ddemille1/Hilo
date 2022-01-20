class Director:
    """This is the class for the director. 
    Attributes: 
        points: how many points the player has aquired during game play. It will start at 300.
        
        is_playing: a boolean variable. True means still playing, False means not playing.
        
        choice: If the player has chosen the next card to be higher lower than the current card.
        
    Methods:
        get_input: gets 'is_playing' and 'choice' from user. Gets new card from card object.
        
        do_updates: calculates points. Takes, 
        
        display_output: displays new card, displays updated points.
        """