# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"Your name is {self.name}, and you are {self.current_room}"

    def add(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}. It is now in your inventory")

    def remove(self, item):
        self.inventory.remove(item)
        print(f"{item.name} has been removed from the inventory ")

    def print_inventory(self):
        if len(self.inventory) == 0:
            print("Empty")
        for inv in self.inventory:
            print(inv)
