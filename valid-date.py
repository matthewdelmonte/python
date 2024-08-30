# validate date entered

days_in_month = [(1, 31), (2, 30), (3, 31), (4, 28), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def verifyDate():
    print("Please enter a date.")
    month = input("Enter the month: ")
    day = input("Enter the day: ")
    year = input("Enter the year (xxxx): ")

    month_name = None

    for i, (lower, upper) in enumerate(days_in_month):
        if int(month) == lower and int(day) > upper:
           month_name = months[i]
           print(f"You entered {month}/{day}/{year}, but {month_name} does not have more than {upper} days.")
           return
        elif int(month) == lower and int(day) <= upper:
           print(f"The date you entered {month}/{day}/{year} is a valid date!")
           return


if __name__ == "__main__":
    verifyDate()
