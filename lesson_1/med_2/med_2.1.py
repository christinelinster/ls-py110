# Lettercase Percentage Ratio

def percentage(count, total):
    return f'{count/total * 100:.2f}'


def letter_percentages(str):
    length = len(str)
    lower = 0
    upper = 0 
    neither = 0 

    for letter in str:
        if letter.isupper():
            upper += 1 
        elif letter.islower():
            lower += 1
        else:
            neither += 1

    return {'lowercase': percentage(lower, length), 'uppercase': percentage(upper, length), 'neither': percentage(neither, length)}



expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)