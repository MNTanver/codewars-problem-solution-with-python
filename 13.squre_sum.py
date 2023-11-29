# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9


def square_sum(numbers):
    sum = 0
    
    for i in range(0, len(numbers)):
        sum = sum + numbers[i] ** 2
    #return sum
    print(sum)

numbers = [1, 2, 3] 
square_sum(numbers) 
