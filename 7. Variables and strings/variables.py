variable = 10
this_is_a_variable = variable # normal assignment

a, b, c, d = 1, 2, 3, 4 # comma separated assignment

print(variable , " " , this_is_a_variable , " " , a) # in python comma (,) is used to concatinate 2 strings

# Rules of naming a variable
# 1. It should start with a letter or a underscore (_)
# 2. Letters numbers or underscores are allowed in python (same as C++)
# 3. Names are case sensitive
# 4. variables should be names in snake_case format
# 4a. CAPITAL_SNAKE_CASE means a constant
# 4b. UpperCamelCase means we want to define a class
# variables that start and end with double underscores are called dunders and should be left alone

# data types in python
# 1. int
# 2. float
# 3. bool (True / False) [T / F should be capital]
# 4. str enclosed in ""
# 5. list enclosed in []
# 6. dict enclosed in {"key" : "value", ...}

# None is a value similar to null
x = None 
x = 10
x = "some string"
# we are reassigning the same x to different data types this is known as dynamic typing
x = 'some other string' # single and double quotes are both valid for strings

# single quotes are valid inside double quotes and vice versa (same like JavaScript)
username = "shrirang"
print("Hello, " + username + " welcome to the game...") # if everything is of same data type then (+) operator can be used

# interpolation 
variable = 15
variable_string = f"the value of variable is {variable}"
print(variable_string)

# how to access a string letter by letter? -> by using the square brackets []
print("shrirang"[0]) # forward access
print("shrirang"[-1]) # reverse access

# converting data types by calling constructors of the respective classes
x = 10
x = "8"
print(float(x)) 

