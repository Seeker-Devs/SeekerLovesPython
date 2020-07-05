"""
   ____   _
  / ___| | |   __ _   ___   ___
 | |     | |  / _` | / __| / __|
 | |___  | | | (_| | \__ \ \__ \
  \____| |_|  \__,_| |___/ |___/
                                
"""
class Car: #define the class
    def honk(self): #you must pass self in function 'arguments'
        print("Honk honk")
    def carname(self, name="Test"): #name is a function argument too, just ignore self when using the functions
        return name #returns the carname instead of printing it
    def carspeed(self, speed):
        if isinstance(speed, int):
            return speed
    def breaks(self):
        return Car().carspeed(0)
Car().honk() #access honk from class Car()
input1 = input("Enter your car name:")
nameofcar = Car().carname(input1)
print("You car name is: {}".format(nameofcar))
try:
    input2 = int(input("Broom wroom! What speed would you like to drive the car at?"))
    speedofcar = Car().carspeed(input2)
    print(f"Your speed of car: {speedofcar}")
except ValueError:
    print("Speed must be an integer value.")
    print("Car speed has been set to 20.")
    Car().carspeed(20)
input3 = input("Would you like to stop the car?")
if input3.lower() == "Yes".lower():
    speednow = Car().breaks()
    print(f"Car speed now = {speednow}")
else:
    print("OH NOOOOOO! WE ALMOST CRASHED FRICK")
    Car().breaks()