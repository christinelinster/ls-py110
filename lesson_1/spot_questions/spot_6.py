# Odd Number Sub-Strings

'''Write a function that takes a string of integers as input and returns the
number of substrings that result in an odd number when converted to an integer.'''

def solve(num_str):
    substrings = all_substrings(num_str)
    count = 0 
    for num in substrings:
        if int(num) % 2 == 1:
            count += 1
    return count

def all_substrings(num_str):
    substrings = [] 
    for i in range(len(num_str) + 1):
        for j in range(i + 1, len(num_str) + 1):
            substrings.append(num_str[i: j])
    return substrings

print(solve('1341'))
print(solve('1357'))
# Examples:
# solve("1341") # should return 7
# solve("1357") # should return 10
