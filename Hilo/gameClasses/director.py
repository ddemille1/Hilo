class Director:
    """This is the class for the director. 
    Attributes: 
        points: how many points the player has aquired during game play. It will start at 300.
        
        is_playing: a boolean variable. True means still playing, False means not playing.
        
        choice: If the player has chosen the next card to be higher or lower than the current card.
        
        win: 100 points

        loser: -75 points

    Methods:
        start_game: Draw inatial card. Display_output.
        return points
        
        get_input: gets 'is_playing' and 'choice' from user.
            return: is_playing

        take_turn: draw a new card, compare to provious card to choice. 
            return: win or lose

        update_score: updates points from win or lose. 

        display_output: displays new card, displays updated points.
        return: points
        """