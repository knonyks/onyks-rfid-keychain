import csv
import sys
import serial
import os

from tabulate import tabulate

import random



filename = "plik.csv"
header = ["UID_125KHz", "UID_13.56MHz", "Name", "Surname", "Email", "Phone"]
data = []


# 125KHz read
def read_uid_125(port='/dev/serial0', baudrate=9600, timeout=1):
    ser = serial.Serial(port, baudrate, timeout=timeout)
    print("bring 125KHz rfid tag")

    while True:
        data = ser.read(14)
        if len(data) == 14 and data[0] == 2 and data[-1] == 3:
            try:
                uid = data[1:-1].decode('ascii')  # UID without STX and ETX
                return uid
            except UnicodeDecodeError:
                print("Error decoding uid")

#make new csv file with header
if not os.path.exists(filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as plik:
        writer = csv.writer(plik, delimiter=',')
        writer.writerow(header)


#read from csv
with open(filename, mode="r", encoding="utf-8") as plik:
    reader = csv.reader(plik, delimiter=',')  # zmień delimiter jeśli potrzeba
    data = list(reader)

#main
with open(filename, mode="a", newline="", encoding="utf-8") as plik:
    writer = csv.writer(plik, delimiter=',')

    while True:

        command = input("-> ")

        if command == "add":

            name = input("enter your name: ")
            surname = input("enter you surname: ")
            email = input("enter your email: ")
            pnumber = input("enter your phone number: ")

            uid1 = read_uid_125()
            print(f"125KHz UID: {uid1}")
            uid2 = ''.join(random.choices('0123456789ABCDEF', k=14))
            print(f"13,56MHz UID: {uid2}")

            new_row = [uid1, uid2, name, surname, email, pnumber]

            data.append(new_row)
            writer.writerow(new_row)
            print("saved!")

	elif command == "read":
	    
	
        elif command == "print":
            print(tabulate(data[1:], headers=data[0], tablefmt="grid"))

        elif command == "help":
            print("add - add new keychain \n print - print a table of all added keychains \n exit - ends program")


        elif command == "exit":
            break

        else:
            print("invalid command \n use help to see all available commands")



