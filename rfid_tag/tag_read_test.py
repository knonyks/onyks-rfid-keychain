import serial
import os


save_file = 'test.txt'
data_list = {}


if os.path.exists(save_file):
	with open(save_file, 'r', encoding='utf-8') as file:
		for line in file:
			line = line.strip()
			if line:
				uid, data = line.split(';',1)
				data_list[uid] = data


ser = serial.Serial('/dev/serial0', 9600, timeout=1)

print("czekam na karte RFID...")
while True:
	data = ser.read(14)
	if data:
		if data[0] == 2 and data[-1] == 3:
			uid = data[1:-2].decode('ascii')
			if uid in data_list:
				print(f"uid: {uid} -> Dane: {data_list[uid]}")
			else:
				print(f"new uid: {uid}")
				new_data = input("Insert data: ")
				data_list[uid] = new_data

				with open(save_file, 'a', encoding='utf-8') as file:
					file.write(f"{uid};{new_data}\n")
