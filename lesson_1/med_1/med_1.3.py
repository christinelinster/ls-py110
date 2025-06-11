# Rotation (Part 3)

def max_rotation(number):
    num_str = str(number)
    for i in range(len(num_str)):
        first_section = num_str[:i]
        second_section = rotate(num_str[i:])
        num_str = first_section + second_section
    
    return int(num_str)
    
                   
def rotate(number):
    return number[1:] + number[0]




print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True


