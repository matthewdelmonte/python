# Use avg_sample_data.csv for testing

def average(total, count):
    return total / count


def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName, "r")
    total: float = 0.0
    count: int = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            try:
                total = total + float(xStr)
            except ValueError:
                print("There is a data type error. Check the source data.")
            count = count + 1
        line = infile.readline()
    print(f"\nThe average of the numbers is: {average(total, count):.2f}.")


if __name__ == "__main__":
    main()
