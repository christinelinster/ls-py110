# Anagram Difference (PEDAC Study Session)

def anagram_difference(str1, str2):
    result = 0
    dict1 = create_dictionary(str1)
    dict2 = create_dictionary(str2)

    for key, value in dict1.items():
        if key not in dict2:
            result += value
        else:
            diff = abs(value - dict2.get(key))
            del dict2[key]
            result += diff

    for key, value in dict2.items():
        if key not in dict1: 
            result += value

    return result

def create_dictionary(word):
    letters = {}
    for letter in word:
        letters[letter] = letters.get(letter, 0) + 1
    return letters

print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0 )
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2 )
print(anagram_difference('a', 'aab') == 2 )
print(anagram_difference('codewars', 'hackerrank') == 10 )
print(anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42)
print(anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50)