# List Comprehensions 

# Basic List Comprehension 
x = [i for i in range(10)] # For loop inside list 

print(x)

# Nested List Comprehension 
x = [[j for j in range(5)] for i in range(10)] 

print(x)

#
x = [i for i in range(10) if i % 2 ==0] # Condition checking if i is even and then it will print

print(x)