# Find the highest number in unsorted list

def main():
    try:
        numbers = input("Enter numbers separated by commas: ").split(",")
        numbers = [float(num) for num in numbers]
        print(numbers)
        check_numbers(numbers)  # This will raise an error
    except TypeError as e:
        print(e)

    max = 0

    for i in range(len(numbers)):
        if float(numbers[i]) > max:
            max = float(numbers[i])

    print(f"The largest number is {max}.") 

def check_numbers(num):
    for i, value in enumerate(num):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Argument {i+1} with value '{value}' is not a number (int or float).")
    return True  # Returns True if all arguments are numbers


if __name__ == '__main__':
    main()