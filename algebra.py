# Algebraic equation f(x) = 2x + 3
# y is a dependent variable, it depends on the value of x
# x is an independent variable, it is not dependent on any other variable
# y = 2x + 3 is an expression, it is a mathematical statement that defines the relationship between x and y.
# f(x) is a function, it is a mathematical statement that defines the relationship between x and y.

def calculate_y(x_value):
    y_value = 2 * x_value + 3
    return y_value

x = 3   
result_y = calculate_y(x)
print(f"When x = {x}, y = {result_y}.")