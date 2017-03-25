# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Room M3

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Now, leave this room, and go somewhere else."
    
    hide eileen
    with dissolve
    
    "There's only one exit. You can't tell which direction that is, but it's forwards."

    menu:
    
        "Leave this room (through the only exit).":
            jump M2
        
        "Stay here.":
            jump M3

    # This ends the game.

    return

label M3:

    show eileen normal
    with dissolve
    
    e "hey. Why are you still here?"

    hide eileen
    with dissolve

    menu:
    
        "Leave this room (through the only exit).":
            jump M2
        
        "Stay here.":
            jump M3

label M2:

    "You're in a new room!"
    
    "There are two exits from here:"
    
    menu:
        "forwards":
            jump M1
        "right":
            jump N2

label M1:
    "Ack! It's a boring room!"
    return

label N2:
    "You went right... but it's still a boring room!"
    return