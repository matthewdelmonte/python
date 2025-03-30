# return message that speed was within the limit or post fine


def getFine(sl, cs):
    while True:
        try:
            speed_limit = int(sl)
            clocked_speed = int(cs)

            if clocked_speed > speed_limit:
                base_fine = 50
                mile_over_limit_fine = (clocked_speed - speed_limit) * 5
                over_ninety_fine = 0

                if clocked_speed > 90:
                    over_ninety_fine = 200

                fine = float(base_fine + mile_over_limit_fine + over_ninety_fine)

                return fine
            else:
                return 0
        except ValueError:
            print(
                "Invalid input. Please enter a number for speed limit and clocked speed."
            )
            sl = input("Enter the speed limit: ")
            cs = input("Enter the clocked speed: ")


def getSpeed():
    speed_limit = input("Enter the speed limit: ")
    clocked_speed = input("Enter the clocked speed: ")

    fine = getFine(speed_limit, clocked_speed)

    if fine > 0:
        return print(f"The fine is ${fine:.2f}")
    else:
        return print("No speeding violation.")


if __name__ == "__main__":
    getSpeed()  # input 65, 75 expect fine to = 100
