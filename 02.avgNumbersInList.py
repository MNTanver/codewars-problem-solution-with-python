def find_average(numbers):
    sum = 0
    for i in range(0,len(numbers)):
        sum = sum + numbers[i]
    results = sum / len(numbers)
    return results
numbers = [1,2,3]
find_average(numbers)