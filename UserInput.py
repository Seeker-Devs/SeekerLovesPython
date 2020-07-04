"""
  _   _                       ___                           _
 | | | |  ___    ___   _ __  |_ _|  _ __    _ __    _   _  | |_
 | | | | / __|  / _ \ | '__|  | |  | '_ \  | '_ \  | | | | | __|
 | |_| | \__ \ |  __/ | |     | |  | | | | | |_) | | |_| | | |_
  \___/  |___/  \___| |_|    |___| |_| |_| | .__/   \__,_|  \__|
                                           |_|
"""
#aight fams! Today, we're going to "study" about user input!
hello_world = input("Henlo senpai! Please input your name:")
print(hello_world)
if hello_world.lower() == "Seeker".lower(): #returns true, not case sensitive
    print("True")
else:
    print("False")
if hello_world.islower(): #CHECKS IF THE string is lower
    print("ye, it's lower")
else:
    print("no")
if hello_world is "Seeker": #== is used to check the equality between values and is is used to check if two values point to the same object.. or type... if we want to check the input
    #we should use '==' operator... let's make use of 'is'!
    print("ok")
else:
    print("no")
age = input("Enter your age:")
if age.isdigit(): #isalpha is for letter, checks if number is an integer
    print("yessir")
else:
    print("dum")
#is example
a1 = "a"
a2 = "a"
if a1 is a2:
    print("yes") #both are the same type.. strings
else:
    print("nooosoaosajdajs'")
b1 = f"a + 2"
b2 = f"a + 2"
if b1 is b2:
    print(" l o l")
else:
    print("ok")

