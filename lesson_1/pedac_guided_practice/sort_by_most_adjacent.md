## Sort by Most Adjacent Consonants

Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

## P: Problem 
- Input: list of strings
- Output: sorted list of strings

- Explicit Rules:
    - sorted by highest to lowest number of adjacent consonants in the string
    - if two strings have the same number of adjacent consonants, then it should maintain relative order
    - consonants are any character from a-z that do not include vowels (a, e, i, o, u)
    - if there is a space between two consonants, it still counts as adjacent 

- Implicit Rules
    - strings may contain more than one words 
    - if a consonant has no adjacent consonants, then the result is 0 adjacent consonants and is no different from a string with no consonants
    - sort in descending order 


- Mental Model: 
    - determine the highest number of adjacent consonants for each string
    - store result of adjacent consonants for each string with the string itself (dictionary?)
    - sort the strings from highest # of consonants to lowest (based on the count of adajacent consonants)

- Clarifying Questions: 
    - is y included as a consonant? Unsure. 
    - can strings be empty? Assume no. 
    - do they always contain multiple words, single word, or varies? Varies.
    - do apostrophes or commas between consonants also count as adjacent? Unsure.

## E: Examples and Test Cases
- the test cases do not answer if y is considered a consonant or whether apostrophes and commas are considered. 
- it does not answer if strings can be empty
- one consonant vs. 0 consonants are the same thing and the original order should just be maintained 
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

## Data Structures
- list of dictionaries or tuples to maintain the order while being able to access the word and number of adjacent consonants of each one 

## Algorithms
1. Start
    - set an empty list for the result 
2. For each string in the list argument (sub-problem and algorithm)
    - determine the number of adjacent consonants
    - save the string and number of adjacent consonants in the dictionary 
3. Sort the dictionary based on highest number of adjacent consonants or maintain relative position if same number
4. Store sorted dictionary in result list
5. Return list 


