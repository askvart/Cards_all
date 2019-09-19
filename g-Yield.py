def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

adress = 'Four score and seven years ago...'
result = index_words(adress)
print(result)

def index_words_iterator(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1

print('----------')
adress = 'Four score and seven years ago...'
result = list(index_words(adress))
print(result)
print('===========')
result = list(index_words_iterator(adress))
print(result)