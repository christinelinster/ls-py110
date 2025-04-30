# Sort by Most Adjacent Consonants

'''
## Algorithms
1. Start
    - set an empty list for the result 
2. For each string in the list argument (sub-problem and algorithm)
    - determine the number of adjacent consonants
    - save the string and number of adjacent consonants in the dictionary 
3. Sort the dictionary based on highest number of adjacent consonants or maintain relative position if same number
4. Store sorted dictionary in result list
5. Return list 

'''
consonants = 'bcdfghjklmnpqrstvwxyz'

def get_max_consonant(string):
    string = ''.join(string.split(' '))
    max_consonant = 0
    adjacent_consonants = '' 

    for letter in string:
        if letter in consonants:
            adjacent_consonants += letter
        else:
            adjacent_consonants = ''
        
        if len(adjacent_consonants) > max_consonant:
            max_consonant = len(adjacent_consonants)
    
    return max_consonant


def sort_by_consonant_count(unsorted_list):
    sorted_list = sorted(unsorted_list, key = get_max_consonant, reverse = True)
    return sorted_list



my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']