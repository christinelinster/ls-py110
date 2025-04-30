# Letter Swap
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

## P: Problem
- Inputs: string of words
- Ouputs: string of words with reversed first/last letter for each word 
- Explicit Rules:
    - each word is separated by a space
    - only letters and spaces, no punctuation or numbers
    - each word has at least one letter
    - string will contain at least one word 
    - no leading or trailing white space
- Implicit Rules:
    - no empty string 
- Mental Model: 
    - for each word if length of word > 1 , reverse first and last letter

## E: Examples and Test Cases
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

## D: Data Structure
- list containing each word in string
- new string 

## A: Algorithm
- set list_of_words as list of words from string
- set swapped_words as empty list 
- iterate through each word in the list:
    - if length of word > 1:
        - swap first and last letter
    - add swapped word to swapped_word list
- combine swapped_words into a string
