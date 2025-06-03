# Delete Vowels
VOWELS = ["a", "e", "i", "o", "u"]
def remove_vowels(original):
    result = []
    final_word = ""
    for word in original:
        for letter in word:
            if letter.lower() not in VOWELS:
                final_word += letter
        result.append(final_word)
        final_word = ""

    return result


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