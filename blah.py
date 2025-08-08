import pandas as pd

def mean():
    scores = [40, 45, 23, 39, 39]
    return sum(scores) / len(scores)

print(mean())

def mode():
    observation = [10, 20, 30, 30, 40, 50]
    return pd.Series(observation).mode().iloc[0]

print(mode())

def median():
    observation = [10, 20, 30, 30, 40, 50]
    return pd.Series(observation).median()

print(median())

scores = [40, 45, 23, 39, 39]

# First Quartile
q1 = pd.Series(scores).quantile(.25)
print(f"Q1: {q1}") # expect 39.0

# Third Quartile
q3 = pd.Series(scores).quantile(.75)
print(f"Q3: {q3}") # expect 40.0

# Inter Quartile Ratio
iqr = q3 - q1
print(f"IQR: {iqr}") # expect 1.0