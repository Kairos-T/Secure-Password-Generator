import secrets
from cryptography.fernet import Fernet

alphanum = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ''.join(secrets.choice(alphanum) for i in range(16))
print("Your generated password is: ", password)

key = Fernet.generate_key()
cipher_suite = Fernet(key)
encrypted_password = cipher_suite.encrypt(password.encode())
print("Your encrypted password is: ", encrypted_password.decode)

decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
print("Your decrypted password is:", decrypted_password)