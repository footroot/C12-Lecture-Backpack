def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# message = "HELLO WORLD"
# shift = 3
# print("Encrypted:", caesar_cipher_encrypt(message, shift))

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
         "U", "V", "W", "X", "Y", "Z"]

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            new_index = (alpha.index(char) + shift) % len(alpha)
            new_char = alpha[new_index]
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

message = "HELLO WORLD"
shift = 5
encrypted_message = caesar_cipher_encrypt(message, shift)
print("Encrypted:", encrypted_message)

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

print("Decrypted:", caesar_cipher_decrypt(encrypted_message, shift))
