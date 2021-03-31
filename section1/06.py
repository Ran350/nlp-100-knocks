def char_bi_gram(text):
    return [text[i]+text[i+1] for i in range(len(text)-1)]


input1 = "paraparaparadise"
input2 = "paragraph"

x = set(char_bi_gram(input1))
y = set(char_bi_gram(input2))

print("和集合:", x.union(y))
print("差集合:", x.difference(y))
print("積集合:", x.intersection(y))

print("'se' in x:", "se" in x)
print("'se' in y:", "se" in y)
