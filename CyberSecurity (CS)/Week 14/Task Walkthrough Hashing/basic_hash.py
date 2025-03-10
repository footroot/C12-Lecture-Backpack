def simple_hash(data):
    return sum(ord(char) for char in data) % 256

print(simple_hash("Hello"))
print(simple_hash("World"))

print(simple_hash("listen"))
print(simple_hash("silent"))

import hashlib
data = input("Input some data: ")
print(hashlib.sha256(data.encode()).hexdigest())


def hash_file(file_path):
    BLOCKSIZE = 65536
    hash_func = hashlib.sha1()
    with open(file_path, 'rb') as file:
        buf = file.read(BLOCKSIZE)
        while len(buf) > 0:
            hash_func.update(buf)
            buf = file.read(BLOCKSIZE)
    return hash_func.hexdigest()

print(hash_file("test.txt"))