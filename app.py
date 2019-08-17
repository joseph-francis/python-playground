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
key_val = {"Mike": 1234, "Joseph": 324, "There": 12}
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
    my_file.close()
    # my_file.seek(0) - to go back the cursor.
    print(fruit, fruits)
    if fruit in fruits:
        return "The fruit is in the list"
    else:
        return "This fruit is not in the list"


print(find_in_file("Orange"))

sample_file = open("sample.txt", "w")
sample_file.write("Mike\nSomething_else\nTesting")
sample_file.close()

sample_file = open("sample.txt", "a")  # To append
sample_file.write("\nBloopers")
sample_file.close()

# r and w operations will not let you read the file. Only the default r will.

sample_file = open("sample.txt", "a+")  # Read and append
sample_file.seek(0)  # The cursor automatically places itself at the end. Need to guide it back to the beginning
sample_file.read()
sample_file.write("\nsomething new")
sample_file.close()

numbers = [1, 2, 3]
number_file = open("numbers.txt", "a+")
for num in numbers:
    number_file.write(str(num) + "\n")
number_file.close()

# The scope of variables in if-else statement is within the scope of the function.
