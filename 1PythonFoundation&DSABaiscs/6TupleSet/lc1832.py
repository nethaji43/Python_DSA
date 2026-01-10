def identifyPangram(sentence):
    converted_sentence = set(sentence)
    if len(converted_sentence) == 26:
        return bool(1)
    else:
        return bool(0)
print(identifyPangram("thequickbrownfoxjumpsoverthelazydog"))
