def worksentence(sentence, separator=" "):
    words = sentence.split(separator)
    number_of_words = len(words)
    # print(words)
    for j in range (number_of_words):
        for i in range(len(words)):
            print(words[i], end=separator)
        print()
        words.pop(-1)

worksentence("La tercera forma de eliminar un eliminar elementos de una lista con Python es la sentencia del")


print("--------------------------------")

def worksentence2(sentence, separator=" "):
    """Delete the last word of a sentence using a for loop

    Args:
        sentence (str): A sentence like "Hello world"
        separator (str, optional): The separator of words. Defaults to " ".
    """
    number_of_words = len(sentence.split(separator))
    print(sentence)
    for j in range (number_of_words-1):
        sentence = sentence.rsplit(' ', 1)[0]
        print(sentence)

worksentence2("La tercera forma de eliminar un eliminar elementos de una lista con Python es la sentencia del")
