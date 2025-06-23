from faker import Faker

fake = Faker()

for _ in range(10):
    print(fake.name())

# print(fake.name())
# print(fake.address())
# print(fake.email())
# print(fake.phone_number())
# print(fake.date_of_birth())
# print(fake.random_number())
# print(fake.random_element(elements=("apple", "banana", "cherry")))