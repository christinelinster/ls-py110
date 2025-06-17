# Delete Vowels
VOWELS = 'aeiou'
def remove_vowels(original):
    no_vowels = []
    for word in original:
        no_vowels.append("".join(char for char in word if char.lower() not in VOWELS))

    return no_vowels


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True