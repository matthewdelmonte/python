count = dict()
names = ["matthew", "kimberly", "caleb", "alyssa", "matthew"]

for name in names:
    count[name] = count.get(name, 0) + 1
print(count)
