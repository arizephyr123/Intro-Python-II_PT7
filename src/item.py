
class Item:
    def __init__(self, name, owner, is_available=True):
        self.name = name
        self.owner = owner
        self.is_available = is_available

    def __str__(self):
        if self.is_available == True:
            return f"{self.name} is in the {self.owner}"
        else:
            return f"{self.name} is in {self.owner}'s inventory.'"
