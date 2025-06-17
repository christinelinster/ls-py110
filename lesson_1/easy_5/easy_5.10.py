# Remove Consecutive Duplicates

def unique_sequence(original):
    result = [original[0]]
    for num in original[1:]:
        if num != result[-1]:
            result.append(num)
    return result

        


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True