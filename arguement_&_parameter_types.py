# Function argument & parameter types

# Example 1: Ordered
def simple_function(x): # necessary parameters or positional parameters which are defined in order
  pass

simple_function(1, 2) # these values or arguments must passed in order as the function shows above

# Example 2: Unordered
def complicated_function(x, y):
  print(x,y)
  pass

complicated_function(y = 2, x = 1) # conversely here, we can directly assign the arguments here out of order

# Example 3 Ordered & Unordered Correct
def more_complicated_function(x, y, z):
  print(x,y)
  pass

more_complicated_function(1, z = 2, y = 3) # here x argument is positionally assigned while z and y are defined 

# Example 4 Ordered & Unordered Incorrect
def wrong_more_complicated_function(x, y, z):
  print(x,y)
  pass

wrong_more_complicated_function(z = 2, 1, y = 3) # Positional argument cannot appear after keyword arguments

# Example 5 Optional Parameters 
def optional_parameter_function(x, y, z = None): # z parameter is not required when function is passed
  print(x,y)
  pass

optional_parameter_function(1,3) # positionally assigned x and y

# Example 6 *args functions 
def args_function(*args): # stores any number of args in a tuple which is an immutable type 
  print(args)
  pass

args_function(1, 2, "ay fellas")

# Example 6 **kwargs functions 
def kwargs_function(**kwargs): # stores any number of key word arguments in a dictionary which is an immutable type 
  print(kwargs)
  pass

kwargs_function(x = 1, s = "hello", b = True)

# Example 7 ultimate *args **kwargs functions 
def args_kwargs_function(*args, **kwargs): # taking *args and **kwargs as parameters
  print(args, kwargs)
  pass

args_kwargs_function(1, 2, 3, x = 1, s = "hello", b = True) # will know to assign key values to **kwargs and ints to *args


# Example 8 complex circumstances breaking apart arguments from lists and dictionaries
def strange_function(a, b, c = True, d = False): # strange assortment of parameters
  print()
  pass

strange_function(*[1,2], **{"c": "hello", "d": "cool"})
# * will allow us to break apart list and dictionary into positional arguments 

# Additional Notes
# A forward slash "/" can be used to force parameters to be positional only, 
# thereby making them required when calling and not by name. 
# So, def function(a, b, /, c, d, *args, e, f = False, **kwargs) means a and b cannot have default values, 
# are required to be passed when calling function, AND can't be supplied with their parameter names. 
# e must also be supplied with a value when called.

# Naming the first * is not required. 
# Doing so simply allows the function to take an arbitrary amount of positional parameters. 
# def function(a, b, /, c, d, *, e, f = False) would require at least 5 arguments (no more than 6) passed to it: a and b are required, 
# c and d are also required and optionally passed as keywords, e must be passed as keyword, f is completely optional, and nothing else is allowed