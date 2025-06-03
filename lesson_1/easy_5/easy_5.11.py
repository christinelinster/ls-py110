# Remove Consecutive Duplicates

def unique_sequence(original):
    result = [original[0]]
    curr_num = original[0]
    for i in range(1, len(original)):
        if original[i] != curr_num:
            result.append(original[i])
            curr_num = original[i]
    return result

        


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True