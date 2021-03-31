with open("./popular-names.txt", 'r') as f:
    text = f.read().replace("\t", " ")

with open("./popular-names-out.txt", 'w') as f:
    f.write(text)
