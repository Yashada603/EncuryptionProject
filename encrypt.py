from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

data = b"Secret Data"

encrypted = cipher.encrypt(data)
print("Encrypted:", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted)