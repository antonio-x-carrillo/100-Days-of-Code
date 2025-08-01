# Works with Website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Find a wall at the start
while right_is_clear() and front_is_clear():
    move()
# Turn if wall is not on the right side
if right_is_clear():
    turn_left()

while not at_goal():
    # When possible, make a right turn
    if right_is_clear():
        turn_right()
        move()
    # Otherwise keep straight
    elif front_is_clear():
        move()
    # As a last resort, turn left
    else:
        turn_left()