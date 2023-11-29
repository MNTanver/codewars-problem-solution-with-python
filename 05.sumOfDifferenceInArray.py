#Your task is to sum the differences between consecutive pairs in the array in descending order. 
# [2, 1, 10]  -->  9
# In descending order: [10, 2, 1]
# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell)

def sum_of_differences(arr):
    arr.sort(reverse=True)
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    
arr = [2, 1, 10]
sum_of_differences(arr)


