from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Bot', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(r"""\
__¶_____________________________________________¶
__¶¶___________________________________________¶¶
__¶¶¶¶________________________________________¶¶¶
__¶¶_¶¶_____________________________________¶¶_¶¶
__¶¶__¶¶___________________________________¶¶__¶¶
__¶¶_¶_¶¶_________________________________¶¶_¶_¶¶
__¶¶__¶__¶_______________________________¶¶_¶__¶¶
__¶¶___¶__¶¶____________________________¶__¶___¶¶
___¶¶___¶¶_¶¶_________________________¶¶__¶___¶¶
____¶¶___¶¶_¶¶_______________________¶¶_¶¶___¶¶¶
_____¶¶___¶¶__¶_____________________¶¶_¶¶____¶¶
______¶¶___¶¶__¶¶__________________¶__¶¶___¶¶¶
_______¶¶____¶¶_¶¶_______________¶¶_¶¶¶____¶¶
________¶¶____¶¶_¶¶_____________¶¶_¶¶____¶¶¶
_________¶¶____¶¶__¶¶__________¶__¶¶____¶¶¶
__________¶¶_____¶¶_¶¶_______¶¶__¶¶____¶¶
___________¶¶_____¶¶_¶¶_____¶¶_¶¶_____¶¶
_____________¶¶____¶¶__¶¶__¶__¶¶____¶¶¶
______________¶¶¶____¶¶_¶¶¶_¶¶¶___¶¶¶
________________¶¶¶___¶¶__¶¶¶___¶¶¶¶
__________________¶¶¶___¶¶_¶¶__¶¶¶
____________________¶¶¶__¶¶_¶¶¶¶
____________________¶_¶¶¶__¶¶_¶¶___¶¶¶¶¶¶
_________¶¶¶¶¶¶¶¶_¶¶_¶¶_¶¶__¶¶_¶¶¶¶¶¶¶¶_¶¶
________¶¶_¶¶¶¶¶¶¶¶_¶¶_¶¶¶¶¶__¶¶¶¶¶¶__¶¶_¶¶
________¶¶¶¶___¶¶¶¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶__¶¶¶¶
_____________¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶_¶¶¶
___________¶¶¶_¶_¶¶¶¶¶______¶¶¶_¶¶¶_¶¶¶¶
__________¶¶¶_¶_¶¶__¶¶¶_____¶¶¶__¶¶¶__¶¶¶
_________¶¶_¶¶_¶¶__¶¶_¶_____¶_¶¶__¶¶_¶_¶¶¶
_______¶¶¶_¶_¶¶¶__¶¶_¶¶_____¶¶_¶___¶¶_¶¶_¶¶¶
______¶¶_¶¶_¶¶¶____¶¶¶_______¶¶¶_____¶¶_¶_¶¶¶¶
_¶¶¶¶¶¶_¶_¶¶¶_________________________¶¶_¶¶_¶¶¶¶¶¶
¶¶____¶¶_¶¶¶____________________________¶¶_¶¶____¶
¶¶_____¶¶¶¶______________________________¶¶_____¶¶
_¶¶¶____¶¶_______________________________¶____¶¶¶
__¶¶¶¶__¶¶_______________________________¶¶¶¶¶¶¶
____¶¶¶¶¶_________________________________¶¶¶

""")

while True:
    action = input('Enter an action: ')
    if action == 'start':
        if newPlayer.current_room:
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction! Try a different action...')
    if action == 'n':
        if newPlayer.current_room.n_to:
            newPlayer.current_room = newPlayer.current_room.n_to
            print(f'{newPlayer.current_room}')
        else:
            print('you cannot go north')
    if action == 's':
        if newPlayer.current_room.s_to:
            newPlayer.current_room = newPlayer.current_room.s_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction! Try a different action...')
    if action == 'e':
        if newPlayer.current_room.e_to:
            newPlayer.current_room = newPlayer.current_room.e_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction! Try a different action...')
    if action == 'w':
        if newPlayer.current_room.w_to:
            newPlayer.current_room = newPlayer.current_room.w_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction! Try a different action...')
    if action == 'q':
        exit()
