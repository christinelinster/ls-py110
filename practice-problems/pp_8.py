# Practice Problem 8

'''
Create a function that takes a non-empty string as an argument. 
The string consists entirely of lowercase alphabetic characters. 

The function should return the length of the longest vowel substring. 
The vowels of interest are "a", "e", "i", "o", and "u".
'''
VOWELS = 'aeiou'
def longest_vowel_substring(str):
    count = 0
    max_count = 0

    for letter in str:
        if letter in VOWELS:
            count += 1
        else:
            count = 0 
        max_count = max(count, max_count)
        
    return max_count




print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)