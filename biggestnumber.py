lst = [1, 2, 3, 4, 5]

# Initialize a variable to store the maximum value, starting with the first element of the list
largest_number = lst[0]

# Iterate through the list starting from the second element
for num in lst[1:]:
    # If the current number is greater than the current maximum, update the maximum
    if num > largest_number:
        largest_number = num

print("The largest number is:", largest_number)

