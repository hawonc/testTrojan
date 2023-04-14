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

    with open("info.txt", "wb") as file:
        file.write(new_key)

    return base64.urlsafe_b64encode(new_key)


def encrypt_file(filename, key):
    fer = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    
    encrypted_data = fer.encrypt(data)
    # change filename (later)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Incorrect password. Erasing file contents.")
        os.remove(filename)
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_dir(path, key):
    for child in pathlib.Path(path).glob("*"):
        if child.is_file():
            print(f"[*] Encrypting {child}")
            encrypt_file(child, key)
        elif child.is_dir():
            encrypt_dir(child, key)

def decrypt_dir(path, key):
    for child in pathlib.Path(path).glob("*"):
        if child.is_file():
            print(f"[*] Decrypting {child}")
            decrypt_file(child, key)
        elif child.is_dir():
            decrypt_dir(child, key)


def main():
    mode = input("Enter mode requested (E/D): ")
    if (mode == "E"):
        password = input("Enter password used for encryption: ")
        t_key = key_gen(password)
        cwd = os.getcwd()
        print("Encrypting directory: {0}".format(cwd))
        c = input("Continue? (Y/N) : ")
        if (c != "Y"):
            os.exit()
        encrypt_dir(cwd, t_key)
    else:
        password = input("Enter password used for decryption: ")
        t_key = key_gen(password)
        cwd = os.getcwd()
        print("Decrypting directory: {0}".format(cwd))
        c = input("Continue? (Y/N) : ")
        if (c != "Y"):
            os.exit()
        decrypt_dir(cwd, t_key)



if __name__ == '__main__':
    main()
