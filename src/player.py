# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_location, inventory=[]):
        self.name = name
        self.location = starting_location
        self.inventory = inventory

    def __str__(self):
        return f"\n********\nPlayer: {self.name}\nLocation: {self.location.name}\nInventory:{self.inventory}\n********\n"

    def travel(self, direction):
        if getattr(self.location, f"{direction}_to"):
            self.location = getattr(self.location, f"{direction}_to")
        else:
            print(f"You cannot move in that direction. Please enter another move.\n")
