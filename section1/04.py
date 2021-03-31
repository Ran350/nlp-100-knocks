raw_text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

text = raw_text.replace(",", "").replace(".", "")
words = [word for word in text.split()]

nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]

element = {}
for i, word in enumerate(words):
    if i in nums:
        element[word[:1]] = i
    else:
        element[word[:2]] = i

print(element)
