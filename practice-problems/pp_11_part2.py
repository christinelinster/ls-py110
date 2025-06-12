# - Create a functin to Find all the possible substrings of s
# - Create a function to check whether the substring * some value k == s 
# - define repeated_substring that takes a single input string (s)
#     - Initialize an empty dictionary to hold all substrings matching the criteria t * k == s
#     - Call my substring funtion to find all substrings of `s`, `all_substrings`
#     - Iterate over `all_substrings`
#         - Call my criteria function
#             - if substring matches critera:
#                 - Add the tuple containg substring and remaning count to the dictionary
#     - Check which substring: repeating count has smallest substring and largest repeating count
#         - return said pair


def possible_substring_with_first_letter(str):
    my_substr = []
    for i in range(1, len(str) + 1):
        my_substr.append(str[:i])
    return my_substr

def match_criteria(substr, str):
    k = len(str) // len(substr)
    if substr * k == str:
        return True
    
def repeated_substring(str):
    str_dict = {}
    all_substr = possible_substring_with_first_letter(str)

    for substr in all_substr:
        if match_criteria(substr, str):
            k = len(str) // len(substr)
            str_dict[substr] = k
    return (sorted(str_dict.items())[0])




print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
print(repeated_substring('xyxxyx') == ('xyx', 2))