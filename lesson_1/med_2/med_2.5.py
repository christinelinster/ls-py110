# Next Featured Number Higher than a Given Value - needs review


    
def get_featured_num(num):
    f_num = num + 1
    while f_num % 2 == 0 or f_num % 7 != 0:
        f_num += 1
    
    return f_num

def all_unique(num):
    num_list = list(str(num))
    return len(num_list) == len(set(num_list))

def next_featured(num):
    MAX_F_NUM = 9876543201
    f_num = get_featured_num(num)

    while f_num <= MAX_F_NUM: 
        if all_unique(f_num):
            return f_num
        f_num += 14
        
    return "There is no possible number that fulfills those requirements."
    

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

