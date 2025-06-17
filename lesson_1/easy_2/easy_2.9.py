# How Many? 

'''
Write a function that counts the number of occurrences of each element in a given list. 
Once counted, print each element alongside the number of occurrences. 
Consider the words case sensitive e.g. ("suv" != "SUV").

'''

def count_occurrences(lst):
    freq_map = {}

    for item in lst:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    for item, count in freq_map.items():
        print(f'{item} ==> {count}')


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'suv', 'car', 'truck']

count_occurrences(vehicles)