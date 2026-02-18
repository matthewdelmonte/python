def grandisSeriesAverage(steps):
    currentSum = 0
    runningAverageTotal = 0

    for i in range(0, steps, 1):
        term = 1 if i % 2 == 0 else -1
        currentSum += term
        runningAverageTotal += currentSum

    return runningAverageTotal / steps

print(grandisSeriesAverage(1000))