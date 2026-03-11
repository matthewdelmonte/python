import numpy as np

# Generate a random array and calculate its mean and standard deviation
rng = np.random.default_rng()

# Generate an array of 20 random numbers
a = rng.random(20)

mean = np.mean(a)
std = np.std(a)

print(f"a: {a}")

print(f"mean: {mean}")

print(f"standard deviation: {std}")
