# convert celcius to fahrenheit
def main():
    while True:
        scale = prompt("Enter 'f' for Fahrenheit or 'c' for Celcius: ", True)

        if scale in ["c", "f"]:
            temp = input("What is the temperature? ")
            if scale == "c":
                fahrenheit = (float(temp) * 9/5) + 32
                print(f"{temp} degrees Celcius, is {str(round(fahrenheit, 1))} degrees Fahrenheit.")
            elif scale == "f":
                celcius = (float(temp) - 32) * 5/9
                print(f"{temp} degrees Fahrenheit, is {str(round(celcius, 1))} degrees Celcius.")
            break
        else:
            print("You must enter either f or c.")


def prompt(display="Please input a string", require=True):
    if require:
        s = False
        while not s:
            s = input(display + " ").lower()
    else:
        s = input(display + " ").lower()
    return s

main()