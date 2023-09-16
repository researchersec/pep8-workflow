"""This module contains the Literature class and its related operations."""

class Literature:
    """A class to represent a piece of literature."""
    def __init__(self, title, writer, length, cost):
        """Initialize the literature's attributes."""
        self.title = title
        self.writer = writer
        self.length = length
        self.cost = cost
        self.is_purchased = False

    def purchase(self):
        """Mark the literature as purchased and print an appropriate message."""
        if not self.is_purchased:
            self.is_purchased = True
            print(f"The literature '{self.title}' is now purchased.")
        else:
            print(f"The literature '{self.title}' is already purchased.")

    def showcase(self):
        """Display the literature's details."""
        print(f"Title: {self.title}")
        print(f"Writer: {self.writer}")
        print(f"Length: {self.length}")
        print(f"Cost: ${self.cost:.2f}")
        print(f"Is Purchased: {self.is_purchased}")

def execute():
    """Main function to create and interact with Literature instances."""
    literature1 = Literature("Python Lore", "John Deer", 320, 28.99)
    literature2 = Literature("Mastering Python Tales", "Jane Snow", 520, 47.99)
    literature3 = Literature("Python in Mythology", "Alice Green", 420, 38.99)

    literature1.showcase()
    literature2.purchase()
    literature2.showcase()
    literature3.showcase()

if __name__ == "__main__":
    execute()
