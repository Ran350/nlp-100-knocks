def cipher(plain):
    encrypted = [chr(219 - ord(w)) if w.islower() else w for w in plain]
    return ''.join(encrypted)

print(cipher("abcABC"))
