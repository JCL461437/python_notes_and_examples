# Mutable vs Immutable 
# Mutable Types: list, set, dictionary (these can be changed)
# Immutable Types: strings, ints, floats, bools, bytes, tuples (cannot be changed)

# Example 1
x = (1, 2) # tuple 
x[0] = 1 # cannot assign a new value to this variable

# Example 2
x = (1, 2) # tuple 
y = x # you can assign a immutable type to another variable (copy of the immutable object.
x = (1,2,3) # this will not affect the value of Y. Whenever using an immutable type, so long as you don;t change the values of what Y is storing it will be okay.
print(x, y) 

# Example 3 
x = [1, 2] # list which is mutable
y = x 
x [0] = (100) # X and Y will have the same value. When using mutable values, where variable is assigned to another variable storing mutable type, what happens is you are storing a reference or alias to another object. So if the reference object is changed then both will change.
print(x, y) 


def get_largest_numbers(numbers, n): # the numbers parameter is a reference to the nums array/list below
    numbers.sort()

    return numbers[-n:]

nums = [2, 3, 4, 1, 34, 123, 321, 1]

print(nums) # this list will be unsorted 
largest = get_largest_numbers(nums, 2)
print(nums) # this list will be sort 