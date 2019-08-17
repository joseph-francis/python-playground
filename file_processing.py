my_file = open("fruits.txt")
content = my_file.read()
my_file.close()

# Or you can use with statement. With with statement, closing is implicitly implied.

with open("fruits.txt") as fruits:
    fruits.read()

