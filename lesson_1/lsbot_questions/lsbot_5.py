# ​String Compression (Medium)

''' 
Create a function that performs basic string compression using counts 
of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3".
If the compressed string would not be smaller than the original string, your function should return the original string.
'''

def compress_string(string):
    if not string: 
        return ""
    
    new_string = ''
    count = 1
    curr_char = string[0]

    for i in range(1, len(string)):
        if string[i] == curr_char:
            count += 1
        else:
            new_string += curr_char + str(count)
            curr_char = string[i]
            count = 1
    new_string += curr_char + str(count)
    print(new_string)
    return new_string if len(new_string) < len(string) else string



 # Examples
print(compress_string("aabcccccaaa") == "a2b1c5a3")
print(compress_string("abcdef") == "abcdef")  # Compressed would be "a1b1c1d1e1f1" which is longer
print(compress_string("aaaaaa") == "a6")
print(compress_string("aaabbb") == "a3b3")
print(compress_string("") == "")
    