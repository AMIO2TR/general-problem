from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Load the DER-encoded certificate
with open("2048b_rsa_example_cert.der", "rb") as f:
    cert_data = f.read()

# Parse the certificate
cert = x509.load_der_x509_certificate(cert_data)

# Extract the public key
public_key = cert.public_key()

# Ensure it's an RSA key
if isinstance(public_key, rsa.RSAPublicKey):
    modulus = public_key.public_numbers().n
    print(f"Modulus (n): {modulus}")
else:
    print("The public key is not an RSA key.")
