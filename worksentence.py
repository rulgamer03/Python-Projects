def worksentence(sentence, separator=" "):
    words = sentence.split(separator)
    number_of_words = len(words)
    # print(words)
    for j in range (number_of_words):
        for i in range(len(words)):
            print(words[i], end=separator)
        print()
        words.pop(-1)



worksentence("Hola como estas muy bien")
