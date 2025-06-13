# Unlucky Days - needs practice 
import datetime

def friday_the_13ths(year):
    day_13 = [datetime.date(year, month, 13) for month in range(1, 13)]

    count = 0 
    for date in day_13:
        if date.weekday() == 4:
            count += 1
    return count


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True