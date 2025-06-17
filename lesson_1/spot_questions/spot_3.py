# Count Substring Instances

'''Write a function that takes two strings as input, `full_text` and `search_text`,
and returns the number of times `search_text` appears in `full_text`.
'''

def solution(text, search):
    count = 0
    i = 0 
    while i + len(search) < len(text) + 1:
        if text[i: i + len(search)] == search:
            count += 1
            i += len(search)
        else:
            i += 1
    return count 

print(solution('abcdeb','b'))
print(solution('aaabbbcccc', 'bbb'))

# Examples:
# solution('abcdeb','b') # should return 2 since 'b' shows up twice
# solution('aaabbbcccc', 'bbb') # should return 1
