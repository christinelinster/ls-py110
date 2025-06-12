# Practice Problem 19 

def odd_fellow(num_list):
    num_set = set(num_list)

    for num in num_set:
        if num_list.count(num) % 2 == 1:
            return num
        

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)