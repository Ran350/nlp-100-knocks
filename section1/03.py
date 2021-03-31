input = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

text = input.replace(",", "").replace(".", "")
words = [len(word) for word in text.split()]

print(words)
