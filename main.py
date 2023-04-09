import pathlib
import secrets
import os
import base64
import getpass

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


# asymmetric key generation

def key_gen(password):
    new_salt = secrets.token_bytes(16)
    kdf = Scrypt(salt=new_salt, length=32, n=2**14, r=8, p=1)
    new_key = kdf.derive(password.encode())

    with open("info.txt", "wb") as file:
        file.write(new_key)

    return base64.urlsafe_b64encode(new_key)


def crypt_file(filename, key):
    fer = Fernet(key)
    with open(filename, "wb") as file:
        data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    # change filename (later)
    with open(filename, "wb") as file:
        file.write(encrypted_data)