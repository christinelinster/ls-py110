# Typoglycemia Generator

'''Write a function that generates text following a pattern where:
1) the first and last characters of each word remain in their original place
2) characters between the first and last characters are sorted alphabetically
3) punctuation should remain at the same place as it started'''

def scramble_words(words):
    all_words = words.split()
    for i, word in enumerate(all_words):
        start = 0
        end = -1 if word[-1].isalnum() else -2
        print(end)

        middle = get_middle(word[start + 1:end])

        all_words[i] = word[start] + middle + word[end:]
    return " ".join(all_words)
    
def get_middle(word):
    sorted_word = sorted([c for c in word if c.isalnum()])
    final_middle = ''
    for char in word:
        if char.isalnum():
            final_middle += sorted_word.pop(0)
        else:
            final_middle += char
    return final_middle



print(scramble_words('professionals'))
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")
# Examples:
# scramble_words('professionals') # should return 'paefilnoorsss'
# scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") # should return "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."