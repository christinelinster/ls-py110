# Leading Substrings

def leading_substrings(word):
    result = []
    curr_substring = ''
    for letter in word:
        curr_substring += letter
        result.append(curr_substring)

    return result

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])