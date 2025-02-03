'''
Create a program that reads a string and alternates 
between adding an @ symbol after every other letter
for example, "hello" becomes "he@ll@o"
''' 

# h e l l o
# 0 1 2 3 4

# h e @ l l @ o

text = input("Enter a string: ")

new_text = ''

for i, char in enumerate(text):

    if i == 0:
        new_text = new_text + char

    elif i % 2 == 0:
        new_text = new_text + "@" + char

    else:
        new_text = new_text + char

print(f"Modified string {new_text}")