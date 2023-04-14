import pathlib
import secrets
import os
import base64
import getpass
import numpy

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt



print(secrets.token_bytes(16))
numpy.random.seed(15)
print(numpy.random.bytes(16))
