series = [9, 15, 41, 12, 74, 15]
largest_num = -1

for num in series:
    if num > largest_num:
        largest_num = num
        print("{} is the greatest number.".format(largest_num))
    elif num < largest_num:
        print("{} is less than {}".format(num, largest_num))
print("finished loop")
