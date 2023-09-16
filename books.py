class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_sold = False

    def sell(self):
        if not self.is_sold:
            self.is_sold = True
            print(f"The book '{self.title}' is now sold.")
        else:
            print(f"The book '{self.title}' is already sold.")

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: ${self.price:.2f}")
        print(f"Is Sold: {self.is_sold}")

def main():
    book1 = Book("Python for Beginners", "John Doe", 300, 29.99)
    book2 = Book("Advanced Python", "Jane Smith", 500, 49.99)
    book3 = Book("Data Science with Python", "Alice Brown", 400, 39.99)

    book1.display()
    book2.sell()
    book2.display()
    book3.display()

if __name__ == "__main__":
    main()
