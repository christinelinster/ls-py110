# Find Balanced Substring (Advanced)

'''
Create a function that finds the longest substring 
of a string that has an equal number of each vowel 
(a, e, i, o, u). 

If there are multiple such substrings with the same length, 
return the one that appears first. If no such substring exists, return an empty string.'''


def balanced_vowels(text):
    all_substrings = get_substrings(text)

    if all_substrings:
        return sorted(all_substrings, key=len, reverse=True)[0]
    else:
        return "" 
    

def get_substrings(text):

    substrings = []
    for i in range(len(text)):
        for j in range(i+5, len(text) + 1):
            curr_substr = text[i:j]
            if has_equal_vowels(curr_substr):
                substrings.append(curr_substr)

    return substrings

def has_equal_vowels(text):
    VOWELS = 'aeiou'
    freq = text.count(VOWELS[0])
    if freq == 0:
        return False
    for c in VOWELS:
        if text.count(c) != freq:
            return False
    return True



        


# Examples
print(balanced_vowels("aeiou") == "aeiou")
print(balanced_vowels("aeiouu") == "aeiou")
print(balanced_vowels("aacdeeeeiiiioou") == "eeeeiiiioou")
print(balanced_vowels("xyz") == "")
print(balanced_vowels("aeiouaeiou") == "aeiouaeiou")
    