import random


def shuffle_word(word):
    shuffled = ''.join(random.sample(word[1:-1], len(word)-2))
    return word[0] + shuffled + word[-1]


raw_text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = [w for w in raw_text.split()]

shuffled = [shuffle_word(w) if len(w) > 4 else w for w in words]


print(' '.join(shuffled))
