import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    name: str
    address: str


def main() -> None:
    person = Person(name="Matthew", address="123 Main St")
    print(person)


if __name__ == "__main__":
    main()
