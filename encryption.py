import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

encrypt_dict = {chars[i]: key[i] for i in range(len(chars))}
decrypt_dict = {key[i]: chars[i] for i in range(len(chars))}

# encrypt

def encrypt(message):
  return ''.join(encrypt_dict[char] for char in message if char in encrypt_dict)
  
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt(plain_text)

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# decrypt

def decrypt(message):
  return ''.join(decrypt_dict[char] for char in message if char in decrypt_dict)

cipher_text = input("Enter a message to decrypt: ")
decrypted_text = decrypt(cipher_text)

print(f"Encrypted message: {cipher_text}")
print(f"Decrypted message: {decrypted_text}")

