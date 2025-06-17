# Longest Chain of Vowels

'''Write a function that takes a lowercase string as input and returns the
length of the longest substring that consists entirely of vowels (a, e, i, o, u).
'''

vowels = 'aeiou'

def solve(str):
    longest = 0
    l = 0
    curr_longest = 0 
    while l < len(str):
        if str[l] in vowels:
            curr_longest += 1
            longest = max(longest, curr_longest)
        else: 
            curr_longest = 0
        l += 1
    return longest

print(solve("roadwarriors"))
print(solve("suoidea"))

# Examples:
# solve("roadwarriors") # should return 2
# solve("suoidea") # should return 3
