# Step Up Karel
# Have Karel pick up the beeper and place it on top of the step. At the end Karel should be in this state:

def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()


# Turns Karel 90 degrees to the right. 
def turn_right():
   turn_left()
   turn_left()
   turn_left()

