"""Module for demonstrating a simple Book class."""


class Book:
    """A simple Book class to demonstrate OOP concepts."""

    def __init__(self, title, author, pages, price):
        """Initialize the attributes of the book."""
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_sold = False

    def sell(self):
        """Mark the book as sold."""
        if not self.is_sold:
            self.is_sold = True
            print(f"The book '{self.title}' is now sold.")
        else:
            print(f"The book '{self.title}' is already sold.")

    def display(self):
        """Display the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: ${self.price:.2f}")
        print(f"Is Sold: {self.is_sold}")


def main():
    """Create and interact with Book instances."""
    book1 = Book("Python for Beginners", "John Doe", 300, 29.99)
    book2 = Book("Advanced Python", "Jane Smith", 500, 49.99)
    book3 = Book("Data Science with Python", "Alice Brown", 400, 39.99)

    book1.display()
    book2.sell()
    book2.display()
    book3.display()


if __name__ == "__main__":
    main()
