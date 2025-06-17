# Alphabet Symmetry

'''Write a function that takes a list of words as input and returns a list of
integers. Each integer represents the count of letters in the word that occupy
their positions in the alphabet.'''

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def solve(lst):
    correct_position = []
    for word in lst:
        correct = 0
        for i, char in enumerate(word):
            if char.lower() == ALPHABET[i]:
                correct += 1
        correct_position.append(correct)
    return correct_position

print(solve(["abode","ABc","xyzD"]))
print(solve(["abide","ABc","xyz"]))

# Examples:
# solve(["abode","ABc","xyzD"]) # should return [4, 3, 1]
# solve(["abide","ABc","xyz"]) # should return [4, 3, 0]
