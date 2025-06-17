# Rotating Characters (Medium)

'''
Create a function that takes a string and a number n as arguments. 
The function should rotate each character in the string by n positions in the alphabet. 
If rotating would go past 'z', wrap around to 'a'. Leave non-alphabetic characters unchanged. Preserve case.
'''

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate_characters(text, n):
    rotated_text = ''
    for char in text:
        if char.isalpha():
            position = ALPHABET.find(char.lower())
            new_position = (position + n) % len(ALPHABET)
            new_char = ALPHABET[new_position]

            if char.isupper():
                new_char = new_char.upper()
                
            rotated_text += new_char
        else:
            rotated_text += char
    return rotated_text


 # Examples
print(rotate_characters("hello", 1) == "ifmmp")
print(rotate_characters("Python!", 3) == "Sbwkrq!")
print(rotate_characters("LaunchSchool", 13) == "YnhapuFpubby")
print(rotate_characters("Zz", 1) == "Aa")