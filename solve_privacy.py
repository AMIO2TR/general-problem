#decrypt the .pem file (rsa_key.d use for decrypt the number )

import Crypto
from Crypto.PublicKey import RSA

with open("private.pem", "rb") as f:
    key = f.read()
    rsa_key = RSA.importKey(key)
    print(rsa_key.d)
