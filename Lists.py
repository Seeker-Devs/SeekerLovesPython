"""
  _       _         _
 | |     (_)  ___  | |_   ___
 | |     | | / __| | __| / __|
 | |___  | | \__ \ | |_  \__ \
 |_____| |_| |___/  \__| |___/
                              
"""
#Going deeper into lists (they were briefly explaining in Conditions.py)
#A string can be indexed like a list (others will cause an error)
string1 = "Random string bois"
print(string1[9])
print(string1[1], string1[2])
#Item in a list can be reassigned/changed
list1 = [5, 12, 14, 72]
print(list1)
#list starts from 0..  5 = [0]
list1[3] = 124000
print(list1)
list2 = [9, 7]
print(list1 + list2) #lists can be multiplied and added
print(list1 * 3) #list values will repeat thrice lmao
liststring1 = ["seeker", "you"]
print("seeker" in liststring1) #returns True if seeker is in liststring1
print("python" in liststring1)
print(not "seeker" in liststring1)
list3 = [1, 2, 3, 4]
#use append to add an item at the end of the list
list3.append(5)
print(list3)
#len returns the number of items in a list
test1 = len(list3)
print(test1)
#the insert method is similar to append.. but allows you to insert the item whereever you want
list3.insert(1, "lol.. im unique here")
print(list3)
#index method checks the position of the item in the list
lol = list3.index(3)
print(lol)
#generate random integers from number to number
newlist = range(9, 12) #other usage `newlist = range(10) (prints integer from 0 to 10)` or `range(1, 10, 2)` the 3rd argument is the interval
print(newlist[0], newlist[1]) 