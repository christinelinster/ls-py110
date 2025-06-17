# Smallest Substring Repeaet

'''Write a function that takes a non-empty string `s` as input and finds the
minimum substring `t` and the maximum number `k`, such that the entire string
`s` is equal to `t` repeated `k` times.'''

def f(s):
    leading_sub = []
    for i in range(1, len(s)):
        leading_sub.append(s[:i])
    
    for substr in leading_sub:
        k = len(s) // len(substr)
        if substr * k == s:
            return [substr, k]

print(f("ababab"))
# Examples:
# f("ababab") # should return ["ab", 3]
