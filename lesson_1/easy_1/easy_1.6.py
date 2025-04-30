# Letter Counter (Part 2)
'''
Modify the word_sizes function from the previous exercise to exclude 
non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

'''


def word_sizes(string):

    word_count = {}
    for word in string.split():
        cleaned_word = ''.join(char for char in word if char.isalpha())
        word_length = len(cleaned_word)

        word_count[word_length] = word_count.get(word_length, 0) + 1

    return word_count

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})