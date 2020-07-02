print("Alright, this file will teach you about conditions. If you have an IQ level above 1, you probably know what this should be about. If you don't, well... you should! *GOOGLE IT UP*.")
Average_age_in_town = 18
if Average_age_in_town > 18: #a colon is important
    print("Average age in town ia 18+.")
elif Average_age_in_town < 18:
    print("Average age in town is below 18.")
elif Average_age_in_town == 18:
    print("Average age in town is 18.")
else:
    print("Average age in town is unknown.")
#syntax example:
#if statement is true/false:
    #do something
#elif anotherstatement is true/false:
    #do something
#else: (if all statements are invalid and there is no other option left, or you can say the default statement if 'all else fails')
    #do something  
#output is average age in town is 18
Seeker_is_making_a_py_tutorial = True #case sensitive, true will cause an error
if Seeker_is_making_a_py_tutorial is True:
    print("Seeker is making a Python tutorial! Check it out! Oh wait, you are..")
Just_a_string = "Just a string fam!"
if Just_a_string == "Just a string fam!":
    print("Moving on to the while statement.. beep boop, boop beep!")
s = 5
while s <= 6.9:
    print(s)
    s = s + 1
print("Okay.. stop it LOL!")
#just because I'm bored UwU
Grocery_list = ["Potatoes", "Onions", "Python"] #this is a list, kind of like an array
print("Dad, I want to buy some " + Grocery_list[2] + "!") #doesn't start with 1
print(f"Mama, you forgot to buy the {Grocery_list[1]}!") #you can just type f before the quotes and type the variables inside a curly bracket