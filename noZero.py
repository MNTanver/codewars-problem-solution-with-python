# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

# Zero alone is fine, don't worry about it. Poor guy anyway


# def no_boring_zeros(n):
#     number_str = str(n)
#     if number_str != '0' and number_str.endswith('0'):
#         number_str = number_str.rstrip('0')
#     return int(number_str)
# print(no_boring_zeros(23500))

def non_zero(number):
        number = str(number)
        if number != 0 and number.endswith('0'):
            number = number.rstrip('0')
        return number

print(non_zero(23500))