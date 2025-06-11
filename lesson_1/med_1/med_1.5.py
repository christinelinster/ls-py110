# Word to Digit 
import string
print(string.punctuation)

NUM_DICT = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def word_to_digit(message):
    words = message.split()

    final_message = [str(NUM_DICT.get(word, word)) for word in words]
    return ' '.join(final_message)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True