import numpy as np

# Generate a random array and calculate its mean and standard deviation
rng = np.random.default_rng()

# Generate an array of 20 random numbers
a = rng.random(20)

print("a: ", a)

print("mean: ", np.mean(a))

print("standard deviation: ", np.std(a))
