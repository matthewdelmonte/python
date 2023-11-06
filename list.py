# x = list()

# prints variable type
# print(type(x))

# prints list methods
# print(dir(x))

numbers = list()
for n in range(0, 7):
    numbers.append(n)

print("This is an array: {} that holds 7 elements.".format(numbers))

cars = ["Mazda", "Chevy", "Ford", "Honda"]

cars.insert(2, "Mini")

for x in cars:
    print(x)
