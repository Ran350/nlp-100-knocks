def word_bi_gram(text):
    text = text.replace(",", "").replace(".", "")
    words = [word for word in text.split()]

    return [words[i]+words[i+1] for i in range(len(words)-1)]


def char_bi_gram(text):
    return [text[i]+text[i+1] for i in range(len(text)-1)]


input = "I am an NLPer"
print(word_bi_gram(input))
print(char_bi_gram(input))
