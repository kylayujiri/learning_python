# PYTHON
# This document serves as a cheat sheet for what I've learned in Python.

# This is how comments are written.

# Primarily uses lower_case for variable names
# Does not use brackets or semi-colons

# Is dynamically typed (do not need to state variable types; the type of data an object can store is mutable)

# Primitives
my_integer = 5
my_float = 5.0
my_string = "5"
my_bool = True #true and false are capitalized

# More on Strings
my_str = "Hi"
my_str2 = "Kyla"
my_str3 = my_str + " " + my_str2 # "Hi Kyla"

make_nanana = "na" * 3 # Results in "nanana"

# Slicing Strings
orig_str = "Hello, world"
sliced_str = orig_str[2:] # "llo, world"
sliced_str2 = orig_str[0] + orig_str[11] # "Hd"

# Multi Line Strings
my_MLS = """ Hi!
This is my Multi Line String (MLS)."""

# Lists
my_list = [0, 1, 2, 3, 4, 5]
# for more on lists see pythonLists.py

# Tuples - immutable data structure (once created, the elements, order, and number of elements cannot be changed)
var1 = 5
my_tuple = ('str1', var1, 'str2', 3)
my_tuple[0] # gets 'str1'
my_tuple[1] # gets var1 which is 5
one, two, three, four = my_tuple # unpacking a tuple (assigns each variable with each element of the tuple)
my_one_element_tuple = (4,) # must have comma to be a tuple

# Operators
my_sum = 5 + 5
my_difference = 5 - 5
my_product = 5 * 5
my_quotient = 5 / 5
my_power = 5 ** 5 # This is 5^5
my_modulo = 5 % 5

# Printing
print("Hello, world")

# Printing Strings and Numbers Together (no concatenation of numbers and strings automatically)
str1 = "There are "
num = 5
str2 = " sheep."

print(str1 + str(num) + str2) # note the use of the function str()



# FUNCTIONS

# W/ No Return
def func_with_no_return(my_param):
    print(my_param)

func_with_no_return("Hi!")

# W/ Return
def add (num1, num2):
	return num1 + num2

sum = add(5, 6)

# Multiple Returns
def add_and_sub (num1, num2):
	add = num1 + num2
	sub = num1 - num2
	return add, sub

addNum, subNum = add_and_sub(10,5)

# Keyword Arguments
def func_using_keyword_args(param_one, param_two = "some value"):
	print(param_one + param_two)

func_using_keyword_args("Hi", "Hey") # will print "HiHey"
func_using_keyword_args("Hi") # will print "Hisome value"
func_using_keyword_args(param_one = "Hi", param_two = "Hey") # will print "HiHey"
func_using_keyword_args("Hi", param_two = "Hey") # will print "HiHey"


# CONTROL FLOW

# If/Else/Else If
my_num = 21

if my_num == 10:
	print("The num is 10!")
elif my_num == 20:
	print("The num is 20!")
else:
	print("The num is not 10 or 20!")

# LOGICAL OPERATORS
# and
bool1 = (2 + 2 >= 4) and (-1 * -1 < 0) # False
# or
bool2 = (2 + 3 == 5) or (-1 + 1 == 2) # True
# not
bool3 = not(5 + 5 == 9) # True

# LOOPS
# For Loop
myList = [1, 2, 3, 4, 5]
for tempVar in myList:
    print(tempVar)
# For Loop Using range()
for i in range(3):
    print("Hi!")
# While Loop
index = 0
while index < 5:
    print(index)
    index += 1

# Break and Continue
# just write break or continue where needed

# Try and Except
try:
	# the code that might cause an error
except ValueError: # the name of the error
	print("Error!")
