names = []

with open("files\\names.txt", "r", encoding="utf-8") as file:
    names = file.readlines()

names.sort()
print(names)

with open("files\\names.txt", 'w', encoding='utf-8') as file:
    file.writelines(names)

# ASk student if they can create the code that will read and write by only opening the file once.
with open('files\\names.txt', "r+", encoding='utf-8') as file:
    names = file.readlines()
    # file.seek(0)
    names.sort()
    file.writelines(names)