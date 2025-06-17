# Staggered Case (Part 2)

def staggered_case(string):
    upper = True
    result = ""

    for letter in string:
        if letter.isalnum():
            if upper:
                result += letter.upper()
            else:
                result += letter.lower()
            upper = not upper
        else:
            result += letter
    return result



string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True