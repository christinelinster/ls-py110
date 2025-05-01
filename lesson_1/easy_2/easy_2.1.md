# Cute Angles
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

## P: Problem 
- Inputs: float number that represents the degrees
- Output: string that represents the degrees, minutes, and seconds 
- Explicit Rules:
    - single quote (') to represent minutes
    - double quote (") to represent seconds 
    - 60 minutes in a degree
    - 60 seconds in a minute 
- Implicit Rules:
    - inputs will only be valid floating point numbers 
    - represent integer numbers in degrees
    - represent remainder on right-side of float of degrees in minutes
    - represent remainder of right-side of float of minutes in seconds 
    - each value has to have at least two numbers, if the integer value is only 1 number, there should be a leading 0 in front of it 
- Mental Model:
    - get the integer values and multiply remainder by 60 to get minutes, do the same for seconds 

## E: Examples and Test Cases
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

## D: Data Structures
- string to represent the final output 
- list to push results and join them together

## A: Algorithm
- degree = int(input)
- remainder = (input - degree) * 60
- minutes = int(remainder)
- remainder = (remainder - minutes) * 60 
- seconds = int(remainder)



