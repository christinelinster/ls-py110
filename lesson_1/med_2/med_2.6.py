# Sum Square -  Square Sum 

def sum_square_difference(num):
    sum_square = sum(i for i in range(1, num + 1)) ** 2
    square_sum = sum(i ** 2 for i in range(1, num +1))
    return sum_square - square_sum



print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
