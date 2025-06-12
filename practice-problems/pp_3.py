# Practice Problem 3, needs practice 

'''
Create a function that takes a string argument and 
returns a copy of the string with every second character 
in every third word converted to uppercase. 
Other characters should remain the same.
'''

def to_weird_case(original):
    words = original.split()

    for i in range(2, len(words), 3):
        word = words[i]
        new_word = "".join(
            char.upper() if idx % 2 == 1 else char 
            for idx, char in enumerate(word)
            )
        words[i] = new_word

    return " ".join(words)




original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)