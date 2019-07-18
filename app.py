my_string = "My String"

print(my_string)
print(type(my_string))
print(len(my_string))

print(type(5))
print(int("1024"))

address = ["New York", 18, "Joseph"]

# The upper bound is excluded
print(address[0:2])
print(address[:])
print(address[:2])

address.append("Something")
print(address)
address.remove("Something")
print(address)
address.pop(1)
print(address)
