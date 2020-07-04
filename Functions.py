"""
  _____                          _     _
 |  ___|  _   _   _ __     ___  | |_  (_)   ___    _ __    ___
 | |_    | | | | | '_ \   / __| | __| | |  / _ \  | '_ \  / __|
 |  _|   | |_| | | | | | | (__  | |_  | | | (_) | | | | | \__ \
 |_|      \__,_| |_| |_|  \___|  \__| |_|  \___/  |_| |_| |___/
                                                               
"""
def print_something(): #def keyword is used to make the function. It defines the functiom
	print("How are you")
testinput = input("Hey\n")
if testinput.lower() == "Hey".functiom #.lower() is a method used to make the string non-case sensitive
	print_something() #to call a function, use this format: func_name(params)
def calculate(a, b): #function arguments or params
	
	return a + b 
print("Sum of two numbers")
sumans = float(input()) #using float is necessary so we don't get 'ab' and get 
#'c' instead
print("Second number:")
ans = float(input())
sum = calculate(sumans, ans)
print(sumans, "+", ans, "=", calculate(sumans, ans))
