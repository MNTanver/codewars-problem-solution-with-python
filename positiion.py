# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Ouput :: "Position of alphabet: 1"


def position(alphabet):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet.lower()
    position = alp.index(alphabet) + 1
    return f"Position of alphabet: {position}"
# Example usage:
letter = input("Enter a letter: ")
position = position(letter)
print(position)

