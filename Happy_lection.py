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


                            # Exercizes 3
                            # Task 1

class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def read_book(self):
        if self.available:
            print(f"Jūs skaitote knygą '{self.title}'")
        else:
            print("Atsiprašome, ši knyga šiuo metu neprieinama")

    def change_availability(self, new_status):
        self.available = new_status
        if new_status:
            print(f"Knyga '{self.title}' dabar prieinama")
        else:
            print(f"Knyga '{self.title}' dabar neprieinama")

# Sukuriam knygos objektą
book1 = Book("Programavimo ABC", "John Smith", True)

# Išbandome metodus
book1.read_book()  # Rezultatas: "Jūs skaitote knygą 'Programavimo ABC'"
book1.change_availability(False)  # Rezultatas: "Knyga 'Programavimo ABC' dabar neprieinama"
book1.read_book()  # Rezultatas: "Atsiprašome, ši knyga šiuo metu neprieinama"

