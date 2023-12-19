#                         # Exercizes
#                         # Task 1
#
# class Skaiciuokle:
#     def __init__(self, skaicius1, skaicius2):
#         self.skaicius1 = skaicius1
#         self.skaicius2 = skaicius2
#
#     def sudeti(self):
#         return self.skaicius1 + self.skaicius2
#
#     def atimti(self):
#         return self.skaicius1 - self.skaicius2
#
#     def dauginti(self):
#         return self.skaicius1 * self.skaicius2
#
#     def dalinti(self):
#         if self.skaicius2 != 0:
#             return self.skaicius1 / self.skaicius2
#         else:
#             return "Dalyba iš nulio negalima"
#
# sk = Skaiciuokle(10, 5)
#
# print("Suma:", sk.sudeti())
# print("Skirtumas:", sk.atimti())
# print("Sandauga:", sk.dauginti())
# print("Dalyba:", sk.dalinti())
#
#
#                         # Task 2
#
#
# class Darbuotojas:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#
#     def visu_vardas(self):
#         return f"{self.vardas} {self.pavarde}"
#
#     def el_pastas(self):
#         return f"{self.vardas.lower()}.{self.pavarde.lower()}@company.com"
#
# darbuotojas1 = Darbuotojas("Jonas", "Jonaitis")
# darbuotojas2 = Darbuotojas("Petras", "Petraitis")
#
# print("Pirmo darbuotojo vardas ir pavardė:", darbuotojas1.visu_vardas())
# print("Pirmo darbuotojo el. paštas:", darbuotojas1.el_pastas())
#
# print("Antro darbuotojo vardas ir pavardė:", darbuotojas2.visu_vardas())
# print("Antro darbuotojo el. paštas:", darbuotojas2.el_pastas())
#
#
#                         # Task 3
#
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def get_title(self):
#         return "Title: " + self.title
#
#     def get_author(self):
#         return "Author: " + self.author
#
# PP = Book("Pride and Prejudice", "Jane Austen")
# H = Book("Hamlet", "William Shakespeare")
# WP = Book("War and Peace", "Leo Tolsto")
#
# print(PP.title)
# print(H.author)
# print(WP.get_title())
# print(PP.get_author())
#
#
#                         # Task 4
#
# class coutry
#     def __init__(self, name, population, area):
#         self.name = name
#         self.population = population
#         self.area = area
#         self.is_big = self.check_if_big()
#         self.population_density = self.population / self.area
#
#     def check_if_big(self)
#         return  self.population > 15000000 or self.area > 3000000
#
#     def compare_population_density(self, other_coutry):
#         if self.population_density > other_coutry.population_density:
#             return f"{self.name} has bigger density as {other_coutry.name}"
#         elif
#             return f"{self.name} has less density as {other_coutry.name}"
#         else
#             return f"{self.name} has same density as {other_coutry.name}"
#
# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)
#
# print(australia.is_big)
# print(andorra.is_big)
# print(andorra.compare_population_density(australia))


                # Task 5

class Finansai:
    def __init__(self):
        self.pajamos = 0
        self.islaidos = 0
        self.balansas = 0
        self.ataskaita = []

    def ivesti_pajamas(self, suma):
        self.pajamos += suma
        self.balansas += suma
        self.ataskaita.append(("Pajamos", suma))

    def ivesti_islaidas(self, suma):
        self.islaidos += suma
        self.balansas -= suma
        self.ataskaita.append(("Išlaidos", suma))

    def perziureti_balansa(self):
        return f"Balansas: {self.balansas}"

    def perziureti_ataskaita(self):
        ataskaitos_tekstas = "\n".join([f"{irasas[0]}: {irasas[1]}" for irasas in self.ataskaita])
        return f"Biudžeto ataskaita:\n{ataskaitos_tekstas}"

# Pagrindinis programos logika
def run_programa():
    finansai = Finansai()
    while True:
        print("\nPasirinkite veiksmą:")
        print("1 - Įvesti pajamas")
        print("2 - Įvesti išlaidas")
        print("3 - Peržiūrėti balansą")
        print("4 - Peržiūrėti biudžeto ataskaitą")
        print("5 - Išeiti iš programos")

        veiksmas = input("Įveskite veiksmo numerį: ")

        if veiksmas == "1":
            suma = float(input("Įveskite pajamų sumą: "))
            finansai.ivesti_pajamas(suma)
            print("Pajamos įvestos.")
        elif veiksmas == "2":
            suma = float(input("Įveskite išlaidų sumą: "))
            finansai.ivesti_islaidas(suma)
            print("Išlaidos įvestos.")
        elif veiksmas == "3":
            print(finansai.perziureti_balansa())
        elif veiksmas == "4":
            print(finansai.perziureti_ataskaita())
        elif veiksmas == "5":
            print("Programa baigė darbą.")
            break
        else:
            print("Neteisingas veiksmo numeris. Bandykite dar kartą.")

if __name__ == "__main__":
    run_programa()
