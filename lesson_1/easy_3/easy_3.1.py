# After Midnight (Part 1)
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def time_of_day(time_in_minutes):
    while time_in_minutes < 0:
        time_in_minutes += MINUTES_PER_DAY
    
    time_in_minutes = time_in_minutes % MINUTES_PER_DAY
    hours = time_in_minutes // MINUTES_PER_HOUR
    minutes = time_in_minutes % MINUTES_PER_HOUR
    time_in_minutes = time_in_minutes / 60 
    
    return f"{hours:02d}:{minutes:02d}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

