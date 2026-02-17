class Book:
    """A class representing a book"""
    
    def __init__(self, title, author, year):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        """Return a user-friendly string representation of the book"""
        return f'"{self.title}" by {self.author} ({self.year})'
    
    def get_age(self):
        """Return the age of the book in years (relative to 2025)"""
        return 2025 - self.year


class EBook(Book):
    """A class representing an electronic book, inheriting from Book"""
    
    def __init__(self, title, author, year, file_size):
        """
        Initialize an EBook object.
        
        Args:
            title (str): The title of the ebook
            author (str): The author of the ebook
            year (int): The publication year of the ebook
            file_size (int): The file size in MB
        """
        super().__init__(title, author, year)
        self.file_size = file_size
    
    def __str__(self):
        """Return a user-friendly string representation of the ebook"""
        return f'"{self.title}" by {self.author} ({self.year}) - {self.file_size} MB'


if __name__ == '__main__':
    # Test the Book class
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(book1)
    print(f"Age: {book1.get_age()} years")
    
    # Test the EBook class
    ebook1 = EBook("Dune", "Frank Herbert", 1965, 5)
    print(ebook1)
    print(f"Age: {ebook1.get_age()} years")
