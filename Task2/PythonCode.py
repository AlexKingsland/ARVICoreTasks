import serial 
import time

arduino = serial.Serial('COM3', 9600)

while True:

	command = input("Enter 1 to turn LED on, 0 to turn LED off, anything to exit: ")
	if command == "1" or command == "0":
		time.sleep(1) 
		arduino.write(str.encode(command))
	else:
		print ("Closing Serial...")
		time.sleep(1) 
		arduino.close()
		break
