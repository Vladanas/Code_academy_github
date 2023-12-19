class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

# Sukuriam knygos objektą
book1 = Book("Programavimo ABC", "John Smith", True)

# Prieinam atributus
print(f"Knygos pavadinimas: {book1.title}")
print(f"Autorius: {book1.author}")
print(f"Ar knyga prieinama: {book1.available}")
