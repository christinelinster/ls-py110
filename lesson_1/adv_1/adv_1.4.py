# Merged Sorted Lists
def merge(lst1, lst2):
    merged_list = []
    i = 0 
    j = 0 

    while i < len(lst1) or j < len(lst2):
        if i == len(lst1):
            merged_list.extend(lst2[j:])
            break
        if j == len(lst2):
            merged_list.extend(lst1[i:])
            break

        if lst1[i] <= lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            merged_list.append(lst2[j])
            j += 1
    return merged_list


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)