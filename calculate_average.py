def average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

marks = [80, 75, 90, 85]

print("Average marks:", average(marks))
