# Sum of Digits

# def sum_digits(number):
#     list_num = list(str(number))
#     total = 0
#     for num in list_num:
#         total += int(num)
#     return total

def sum_digits(number):
    return sum([int(n) for n in str(number)])


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True