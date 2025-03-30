def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")

    return a + b


def main():
    print(add(1, 2))
    print(add(1, "2"))


if __name__ == "__main__":
    main()
