# Matching Parenthesis?

def is_balanced(message):
    stack = []

    for char in message:
        if char == "(":
            stack.append(char)
        if char == ")":
            if not stack:
                return False
            stack.pop()
    
    return not stack

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True