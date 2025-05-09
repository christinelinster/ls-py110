# Name Swapping

def swap_name(name):
    reversed_name = name.split()[::-1]
    return ", ".join(reversed_name)


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True