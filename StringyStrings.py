# write me a function stringy that takes a size and returns a string of alternating 1s and 0s.

# the string should start with a 1.

# a string with size 6 should return :'101010'.

# with size 4 should return : '1010'.

# with size 12 should return : '101010101010'.

# The size will always be positive and will only use whole numbers.



def stringy(size): 
    result = ""
    for i in range(size):
        if i % 2 == 0:
            result += '1'
        else:
            result += '0'
    return result

size = 9
print(stringy(size))

# def alternate_ones_and_zeros(length):
#     return ''.join(['1' if i % 2 == 0 else '0' for i in range(length)])

# # Example usage:
# length = 10
# alternating_string = alternate_ones_and_zeros(length)
# print(alternating_string)
