# Fibonacci Number Location By Length

## P: Problem 
- Input: Number representing length of fibonacci number 
- Output: Number representing index of the first fibonacci number that has a length determined by input 
- Explicit Rules: 
    - first fibonacci number has index of 1 
    - argument will always be be greater than or = 2 

## E: Examples & Test Cases 

print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)
print(find_fibonacci_index_by_length(10000) == 47847)

## D: Data Structures
- dictionary to store the first index that has X number of numbers (to memoize) 

## A: Algorithm:
- while the max of the values in dictionary are less than the input
- starting at 1, with index 1
- store the key-value pair with key as length of the number, and value as the index in a dictionary 
- stop when we get the key-value pair when the key matches the desired length 
- return the value associated with it 