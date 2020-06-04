from room import Room
from player import Player
from item import Item
print(r"""
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
-----------------------------------------------------------------------------------
    Commands: 
       start => starts the game                                                 
       look => see items in a room
       take, get => followed by item's name will add it to your inventory        
       drop => followed by item's name will remove it from inventory    
       inv => see items in your inventory
          n => go north
          s => go south
          e => go east
          w => go west
-----------------------------------------------------------------------------------
""")


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

sword = Item("sword", "battle sword")
axe = Item("axe", "battle axe")
torch = Item("torch", "lights up the room")
dagger = Item("dagger", "good for cutting ropes, not ideal for battle")
gold = Item("gold", "for buying items and trading")

room['outside'].items = []
room['foyer'].items = [torch]
room['overlook'].items = [dagger]
room['narrow'].items = [axe, sword]
room['treasure'].items = [gold]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

newPlayer = Player('Bot', room['outside'])
while True:
    action = input('Enter an action: ').split(" ")

    if len(action) == 1:
        action = action[0]

    elif len(action) > 1:
        new_item = action[1]
        action = action[0]

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

    if action == 'look':
        if newPlayer.current_room.items:
            for obj in newPlayer.current_room.items:
                print("There is a "+obj.name+" in this room")
        else:
            print('no items in this room')

    if action == 'inv':
        newPlayer.print_inventory()

    if action in ["take", "get"]:
        for inv in newPlayer.current_room.items:
            if inv.name == new_item:
                newPlayer.add(inv)
                newPlayer.current_room.on_take(inv)
            else:
                print('item is not in the room')

    if action in ["drop", "d"]:
        for inv in newPlayer.inventory:
            if inv.name == new_item:
                newPlayer.remove(inv)
                newPlayer.current_room.on_drop(inv)
            else:
                print('item is not in inventory')
    if action == 'q':
        exit()
