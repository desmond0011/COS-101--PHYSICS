
# 1. SUM OF A LIST OF NUMBERS

def sum1(numbers):
    return sum(numbers)

def sum2(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

def sum3(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result


# 2. AVERAGE / MEAN OF NUMBERS IN A LIST

def average1(numbers):
    return sum(numbers) / len(numbers)

def average2(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def average3(numbers):
    count = len(numbers)
    total = sum(numbers)
    mean = total / count
    return mean


# 3. MEDIAN OF A LIST

def median1(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2
    return numbers[middle]

def median2(numbers):
    import statistics
    return statistics.median(numbers)

def median3(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2


# 4. MODE OF A LIST

def mode1(numbers):
    return max(set(numbers), key=numbers.count)

def mode2(numbers):
    from statistics import mode
    return mode(numbers)

def mode3(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    return max(frequency, key=frequency.get)


# TEST THE FUNCTIONS

numbers = [2, 4, 4, 6, 8]

print("Sum:", sum1(numbers))
print("Average:", average1(numbers))
print("Median:", median1(numbers))
print("Mode:", mode1(numbers))
