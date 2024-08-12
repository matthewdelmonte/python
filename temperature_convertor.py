# convert celcius to fahrenheit
def main():
    while True:
        scale = prompt("Enter 'f' for Fahrenheit or 'c' for Celcius: ", True)

        if scale in ["c", "f"]:
            temp = input("What is the temperature? ")
            if scale == "c":
                fahrenheit = (float(temp) * 9/5) + 32
                if fahrenheit >=90 or fahrenheit <=30:
                    f_temp_message(temp, fahrenheit)
                    warning(fahrenheit)
                else:
                    f_temp_message(temp, fahrenheit)
            elif scale == "f":
                celcius = (float(temp) - 32) * 5/9
                c_temp_message(temp, celcius)
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

def warning(temp):
    if temp >= 90:
        print("It is hot outside, please stay hydrated!")
    elif temp <=30:
        print("It's cold outside, please dress warmly!")

def f_temp_message(temp, fahrenheit):
        print(f"{temp} degrees Celcius, is {str(round(fahrenheit, 1))} degrees Fahrenheit.")

def c_temp_message(temp, celcius):
        print(f"{temp} degrees Fahrenheit, is {str(round(celcius, 1))} degrees Celcius.")

if __name__ == '__name__':
    main()