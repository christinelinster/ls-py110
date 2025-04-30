# Convert a String to a Number
Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

## P: Problem
- Inputs: string of digits
- Outputs: integer representing characters in the string
- Explicit Rules:
    - cannot use int() to explicitly coerce into an integer 
    - use each character in the string to calculate the result 
    - positive and negative signs do not matter
    - string will only include valid characters (numeric) 
    - string will not have float numbers 
- Implicit Rules:
- Mental Model: 
    - use character position to convert to integer
    - ones position: get remainder after dividing by 10
    - tens position: get remainder after dividing by 100 
    - and so on 

## E: Examples and Test Cases
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

## D: Data Structures
- list of numbers to add them together 

## A: Algorithms
- set numbers = [] 
- get the length of the string to determine how many numbers
- find the associated integer value and add to the list 
- add the numbers together in the list 


