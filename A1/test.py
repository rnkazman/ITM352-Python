from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A secret message.")
print(token)
print(f.decrypt(token))
