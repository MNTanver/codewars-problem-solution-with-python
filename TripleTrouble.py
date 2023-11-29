# Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

# Note: You can expect all of the inputs to be the same length.

def triple_trouble(one, two, three):
    combined_string = ""
    for i in range(len(one)):
        combined_string =  one[i] + two[i] + three[i]
    return combined_string

input1 = "aa"
input2 = "bb"
input3 = "cc"
output = triple_trouble(input1, input2, input3)
print(output)  # Output: "abcabc"




