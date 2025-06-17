# Count of Pairs

'''Write a function that takes a list of integers as input and counts the number of
pairs in the list. A pair is defined as two equal integers separated by some
other integer(s).'''

def pairs(lst):
    num_set = set(lst)
    count = 0
    for num in num_set:
        count += lst.count(num) // 2
    return count 

print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]))

# Examples:
# pairs([1, 2, 5, 6, 5, 2]) --> 2
# pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) --> 4