# All Substrings

# def substrings(word):
#     all_substrings = list()
#     for i in range(len(word)):
#         substrings = leading_substrings(word[i:len(word) + 1])
#         all_substrings.extend(substrings)
    
#     return all_substrings

    

# def leading_substrings(word):
#     result = []
#     curr_substring = ''
#     for letter in word:
#         curr_substring += letter
#         result.append(curr_substring)

#     return result


def substrings(str):
    all_substrings = []

    for i in range(len(str)+1):
        for j in range(i + 1, len(str) + 1):
            all_substrings.append(str[i:j])

    print(all_substrings)
    return all_substrings

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True