# Palindromic Substrings

# def palindromes(word):
#     all_palindromes = []
#     all_substrings = substrings(word)

#     for substr in all_substrings:
#         if len(substr) > 1 and is_palindrome(substr):
#             all_palindromes.append(substr)
#     return all_palindromes


# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False



# def substrings(word):
#     all_substrings = []
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
    return all_substrings

def palindromes(str):
    all_substrings = substrings(str)
    all_palindromes = []

    for word in all_substrings:
        if len(word) > 1 and word == word[::-1]:
            all_palindromes.append(word)
    return all_palindromes


print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True