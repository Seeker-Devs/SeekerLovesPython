def print_something(): #def keyword is used to make the function.
	print("How are you")
testinput = input("Hey\n")
if testinput.lower() == "Hey".lower():
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