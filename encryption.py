import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

print(f"chars: {chars}")
print(f"key: {key}")


