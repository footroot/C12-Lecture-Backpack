word = "welcome"
#       0123456

print(word.upper())
print(word.replace("e", "*"))

# Indexing
print(word[2])
print(word[4])

# Slicing
print(word[0:3])


for letter in word:
    print(letter)


for i in range(len(word)):
    if i%2 == 0:
        print(word[i])


