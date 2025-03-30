academic_standing = ["Freshman", "Sophomore", "Junior", "Senior"]


def get_validated_input(prompt, min_value, max_value):
    while True:
        try:
            credits_earned = int(input(prompt))
            if min_value <= credits_earned <= max_value:
                return credits_earned
            else:
                print(
                    f"Input must be between {min_value} and {max_value}. Please try again."
                )
        except ValueError:
            print("Invalid input. Please enter an integer.")


def determine_standing(credits_earned):
    ranges = [(0, 6), (7, 15), (16, 25), (26, 36)]

    for i, (lower, upper) in enumerate(ranges):
        if lower <= credits_earned <= upper:
            return academic_standing[i]
    return None


def getStanding():
    min_value = 0
    max_value = 36
    credits_earned = get_validated_input(
        "Enter the number of credits earned: ", min_value, max_value
    )
    standing = determine_standing(credits_earned)
    if standing:
        print(f"You've earned the standing of: {standing}")
    else:
        print("Invalid range for academic standing.")


if __name__ == "__main__":
    getStanding()
