# Weird Case Transformer (Medium)

'''
Create a function that takes a string and 
returns it with every other character of every 
third word converted to uppercase. All other characters should remain the same.

'''

def to_weird_case(string):
    words = string.split()

    for i in range(2, len(words), 3):
        words[i] = transform(words[i])
    return " ".join(words)

def transform(word):
    new_word = '' 
    for i in range(len(word)):
        if i % 2 == 1:
            new_word += word[i].upper()
        else:
            new_word += word[i]
    return new_word



# # Examples
print(to_weird_case('Lorem Ipsum is simply dummy text of the printing world') == 
          'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world')
print(to_weird_case('It is a long established fact that a reader will be distracted') == 
          'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD')
print(to_weird_case('aaA bB c') == 'aaA bB c')