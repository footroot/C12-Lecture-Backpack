from hashlib import sha256

text = b"Hello"
text2 = b"Goodbye"

hash_text = sha256(text)
hash_text2 = sha256(text2)

print(hash_text.hexdigest())
print(hash_text2.hexdigest())