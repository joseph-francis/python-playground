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
address.pop(1)  # removes by index
print(address)

# Dictionaries
key_val = {"Mike": 1234, "Joseph":324, "There": 12}
print(key_val["There"])
print(key_val["Joseph"])

keys = ["a", "b", "c"]
values = [1, 2, 3]

combined = dict(zip(keys, values))
print(combined)

val_from_user = int(input("Enter the number: "))
# print("The squared result is: " + str(val_from_user ** 2))

if val_from_user in key_val.values():
    print("The value matched!")
else:
    print("The value did not match")

# elif = else if


def get_age(year):
    return 2019 - year


def find_in_file(fruit):
    my_file = open("sample.txt")
    fruits = my_file.read().splitlines()
    print(fruit, fruits)
    if fruit in fruits:
        return "The fruit is in the list"
    else:
        return "This fruit is not in the list"


print(find_in_file("Orange"))


