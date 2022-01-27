from pickle import TRUE
from gameClasses.director import Director

director = Director()

current_score = director.start_game() 
while current_score >= 0:
    if not director.get_input():
        break
    reward = director.take_turn() 
    director.update_score(reward)
    current_score = director.display_output()


"""End the game displaying score and a message if you won or lost"""

director.start_game()
