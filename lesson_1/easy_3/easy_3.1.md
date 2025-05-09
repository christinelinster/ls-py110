# After Midnight (Part 1)
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

# P: Problem
- Inputs:
    - positive or negative integer representing minutes related to midnight
- Outputs:
    - string denoting the time of day in 24 hr format (hh:mm)
- Explicit Instructions:
    - if number is negative, it represents minutes before midnight
    - if positive, represents after midnight 
    - only integers, can be positive or negative
- Implicit Instructions:
    - assume only integer values 
    - if midnight, it will be positive
    - convert negative numbers to 24hr format by subtracting from 24 hr and 60 min 

- Mental Model:

# E: Examples and Test Cases
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# D: Data Structures

# A: Algorithms
- set hours, convert int to hours by / 60.
- if number is positive and number > 24:
    - subtract 24 from the number
- if the number is negative and number > 24:
    - subtract the number from 24 
- hours = number // by 1 to get the remainder
- remainder = number - hours
- minutes = remainder * 60 
if number was negative:
 - 60 - remainder
if number was positive:
- leave it as is 
