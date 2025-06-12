# Practice Problem 11 -- needs practice 

'''
Create a function that takes a nonempty string as an argument and 
returns a tuple consisting of a string and an integer. If we call the string argument s, 
the string component of the returned tuple t, and the integer component of the tuple k, 
then s, t, and k must be related to each other such that s == t * k. 
The values of t and k should be the shortest possible substring and the largest possible 
repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.
'''

# ## A: Algorithm 
# - for i in range (1, len(str) + 1)
# - set t as substr to string up to i
# - k = s / t 
# - if t * k == str, then return (t, k)

def repeated_substring(str):
    for i in range(1, len(str) + 1):
        t = str[:i]
        k = len(str) // len(t)

        if t * k == str:
            return (t, k)
    



print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
print(repeated_substring('xyxxyx') == ('xyx', 2))