# After Midnight (Part 2)
"""
Write two functions that each take a time of day in 24 hour format, 
and return the number of minutes before and after midnight, respectively. 
Both functions should return a value in the range 0 through 1439.
"""
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(string_time):
    hours, minutes = string_time.split(":")
    min_after_midnight = ((int(hours) * MINUTES_PER_HOUR) + int(minutes)) % MINUTES_PER_DAY
    
    return min_after_midnight
    

def before_midnight(string_time):
    min_after = after_midnight(string_time)
    min_before_midnight = (MINUTES_PER_DAY - min_after) % MINUTES_PER_DAY

    return min_before_midnight

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True