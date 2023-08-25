# sample.py
from calculator.multiply.multiply import multiply

# create a variable in the module
sample_variable = "This is a string variable in the sample.py module"


# A vunction in the module
def say_hello(name):
    return f"Hello, {name} welcome to this simple module."


# This is another function in the module
def add(a, b):
    int = multiply(a, b)
    return f"The sum of {int} + {b} is = {int+b}"


print(sample_variable)
print(say_hello("Matthew"))
print(add(2, 3))
