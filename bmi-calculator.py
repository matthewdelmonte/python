def getBMI(weight, height):
    while True:
        try:
            weight = float(weight)
            height = float(height)
            break
        except ValueError:
            print("Please enter a valid number")
            weight = input("Enter your weight in lb: ")
            height = input("Enter your height in in: ")
    return weight * 720 / (height ** 2)

def getBMICategory(bmi):
    bmi_range = [(0, 18.4), (18.5, 24.9), (25, 29.9), (30, 100)]
    categories = ["below", "within", "above", "obese"]

    for i, (lower, upper) in enumerate(bmi_range):
        if lower <= bmi <= upper:
            return categories[i]
    return "invalid"

def main():
    weight = input("Enter your weight in lb: ")
    height = input("Enter your height in in: ")
    bmi = getBMI(weight, height)
    category = getBMICategory(bmi)
    print(f"Your BMI is {bmi:.2f} and you are {category} the normal range.")

if __name__ == "__main__":
    main()