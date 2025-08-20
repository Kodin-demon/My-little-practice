import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"characters: {chars}")
# print(f"key       : {key}")

# Encryption part

plain_text = input("Enter a Message to encrypt: ")
encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]

print(f"Original Message : {plain_text}")
print(f"Encrypted Message: {encrypted_text}")

# Decryption part

encrypted_text = input("Enter a Message to decrypt: ")
plain_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message: {encrypted_text}")
print(f"Decrypted Message: {plain_text}")
