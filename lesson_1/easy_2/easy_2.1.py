# Cute Angles

'''
Write a function that takes a floating point number representing an angle between 
0 and 360 degrees and returns a string representing that angle in degrees, minutes, 
and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') 
to represent minutes, and a double quote (") to represent seconds. There are 60 minutes 
in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
'''


DEGREE = "\u00B0"
MINUTES_PER_DEGREE = 60 
SECONDS_PER_MINUTE = 60 

def pad_zero(number):
    string_number = str(number)
    if len(string_number) < 2:
        return f'0{string_number}'
    else:
        return string_number


def dms(number):
    degree = int(number)
    minutes = int((number - degree) * MINUTES_PER_DEGREE)
    seconds = int((((number - degree) * MINUTES_PER_DEGREE) - minutes) * SECONDS_PER_MINUTE)

    result = f'''{degree}{DEGREE}{pad_zero(minutes)}'{pad_zero(seconds)}"'''
    return result
    


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")