import csv
import sys

import random
from tabulate import tabulate

dane = []

#odczytanie z csv
with open("plik.csv", mode="r", encoding="utf-8") as plik:
    reader = csv.reader(plik, delimiter=',')  # zmień delimiter jeśli potrzeba
    dane = list(reader)


with open("plik.csv", mode="a", newline="", encoding="utf-8") as plik:
    writer = csv.writer(plik, delimiter=',')

    while True:

        command = input("-> ")

            #print(tabulate(dane[1:], headers=dane[0], tablefmt="grid"))

        if command == "add":

            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            email = input("Podaj email: ")

            uid1 = ''.join(random.choices('0123456789ABCDEF', k=14))
            uid2 = ''.join(random.choices('0123456789ABCDEF', k=14))

            new_dane = [uid1, uid2, imie, nazwisko, email]

            dane.append(new_dane)
            writer.writerow(new_dane)
            print("Zapisano")

        elif command == "print":
            print(tabulate(dane[1:], headers=dane[0], tablefmt="grid"))

        elif command == "exit":
            break

        else:
            print("invalid command")



