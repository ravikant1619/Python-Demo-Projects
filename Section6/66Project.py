def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if turn_is_right():
        turn_right()
        move()
    elif front_is_clear():
        move()    