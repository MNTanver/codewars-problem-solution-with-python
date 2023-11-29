# Zero Terminated Sum

# Mary has another puzzle book, and it's up to you to help her out! This book is filled with zero-terminated substrings, and you have to find the substring with the largest sum of its digits. For example, one puzzle looks like this:

# "72102450111111090"

# Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums of their digits are 10, 11, 6, and 9 respectively. Therefore, the substring with the largest sum of its digits is 245, and its sum is 11.

# Write a function largest_sum which takes a string and returns the maximum of the sums of the substrings. In the example above, your function should return 11.
# Notes:

#     A substring can have length 0. For example, 123004560 has three substrings, and the middle one has length 0.
#     All inputs will be valid strings of digits, and the last digit will always be 0.


def largest_sum(s):
    max_sum = 0
    current_sum = 0
    for digit in s:
        if digit == '0':
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        else:
            current_sum += int(digit)
    return max_sum


# The function iterates through the string s, keeping track of the current sum of digits in current_sum and the maximum sum of digits seen so far in max_sum. Whenever it encounters a zero, it updates max_sum if the current sum is greater, and resets current_sum to zero for the next substring.

# Note that the function assumes that the input string is well-formed (i.e., ends in a zero), so you may want to add some input validation to handle other cases.