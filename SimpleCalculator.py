"""
  ____    _                       _           ____           _                  _           _
 / ___|  (_)  _ __ ___    _ __   | |   ___   / ___|   __ _  | |   ___   _   _  | |   __ _  | |_    ___    _ __
 \___ \  | | | '_ ` _ \  | '_ \  | |  / _ \ | |      / _` | | |  / __| | | | | | |  / _` | | __|  / _ \  | '__|
  ___) | | | | | | | | | | |_) | | | |  __/ | |___  | (_| | | | | (__  | |_| | | | | (_| | | |_  | (_) | | |
 |____/  |_| |_| |_| |_| | .__/  |_|  \___|  \____|  \__,_| |_|  \___|  \__,_| |_|  \__,_|  \__|  \___/  |_|
                         |_|
"""
print("Welcome to SimpleCalculator for this Python Tutorial by Seeker!")
# -------- F U N C T I O N S -------- #
def add(a, b):
	return a + b
def multiply(a, b):
	return a * b
def substract(a, b):
	return a - b
def divide(a, b):
	return a / b
def remainder(a, b):
	return a % b
# -------- I N P U T -------- #
while True: #tabs were uswd
	inputchoice = input("Enter: \nA to calculate \nB to multiply \nC to substract \nD to divide\n")
	if inputchoice in ("A", "B", "C", "D"):
		if inputchoice.lower() == "A".lower():
			print("Loading...")
			first = float(input("Enter your first number: "))
			second = float(input("Enter your second number: "))
			print(f"{first} + {second}\n=  {add(first, second)}")
		elif inputchoice.lower() == "B".lower():
			print("Loading")
			first = float(input("Enter your first number: "))
			second = float(input("Enter your second number: "))
			print(f"{first} * {second}\n= {multiply(first, second)}")
		elif inputchoice.lower() == "C".lower():
			print("Loading")
			first = float(input("Enter your first number: "))
			second = float(input("Enter your second number: "))
			print(f"{first} - {second}\n= {substract(first, second)}")
		elif inputchoice.lower() == "D".lower():
			print("Loading")
			first = float(input("Enter your first number: "))
			second = float(input("Enter your second number: "))
			print(f"{first} ÷ {second}\n= {divide(first, second)}\nRemainder:  {remainder(first, second)}")
		break	
	else:
		print("Invalid input.")
