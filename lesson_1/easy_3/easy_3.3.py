# Double Char (Part 1)

def repeater(message):
    doubled = [char * 2 for char in message]
    return "".join(doubled)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True