from Crypto.PublicKey import RSA

with open("bruce_rsa.pub", 'rb') as f:
    key = f.read()
    rsa_key = RSA.importKey(key)
    print(rsa_key.n)