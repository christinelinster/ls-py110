# All Substrings

def substrings(word):
    all_substrings = list()
    for i in range(len(word)):
        substrings = leading_substrings(word[i:len(word) + 1])
        all_substrings.extend(substrings)
    
    return all_substrings

    

def leading_substrings(word):
    result = []
    curr_substring = ''
    for letter in word:
        curr_substring += letter
        result.append(curr_substring)

    return result

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True