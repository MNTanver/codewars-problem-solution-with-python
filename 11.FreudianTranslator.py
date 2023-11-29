# In this kata, the function will take a string as its argument, and return a string with every word replaced by the explanation to everything, according to Freud. Note that an empty string, or no arguments, should return an empty string.

#**************************************************

def to_freud(sen):
    new_sen = sen.split(' ')
    i = 0
    new_str = ' '
    if len(sen) == 0:
        return sen
    else:
        while i < len(new_sen):
            new_str += 'sex' + ' '
            i += 1
        return new_str.strip()
print(to_freud(""))