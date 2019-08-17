temps = [221, 234, 340, 230]

new_temps = [temp/10 for temp in temps]  # Similar to map function in Swift
print(new_temps)

# Define a function that takes a parameter a list that contains both numbers and strings and returns the list containing only the numbers.

values = [-5, -6, -7, -8, -9, "no data", 1, 2, 3, "yup"]


def foo(params):
    return [type(param) for param in params]


print(foo(values))


def map_and_filter(params):
    return [param for param in params if not isinstance(param, int)]


print(map_and_filter(values))

# If you have an if-else statement inside the list comprehension, you want to put the for-in loop at the very end.

# A list comprehension is an expression that creates a list by iterating over another container.
#
# A basic list comprehension:
#
# [i*2 for i in [1, 5, 10]]
# Output: [2, 10, 20]
#
# List comprehension with if condition:
#
# [i*2 for i in [1, -2, 10] if i>0]
# Output: [2, 20]
#
# List comprehension with an if and else condition:
#
# [i*2 if i>0 else 0 for i in [1, -2, 10]]
# Output: [2, 0, 20]
