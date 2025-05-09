# Sequence Count

def sequence(count, num):
    list = []
    for i in range(count):
        list.append(num * (i + 1))
    return list


print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True