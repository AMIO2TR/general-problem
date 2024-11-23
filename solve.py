import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def extract_rsa_key_parameters(pem_file_path):
    # Read the PEM file
    with open(pem_file_path, 'rb') as pem_file:
        pem_data = pem_file.read()

    # Load the public key
    public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())

    # Extract modulus and public exponent
    numbers = public_key.public_numbers()
    modulus = numbers.n
    exponent = numbers.e

    return modulus, exponent


def search_ct_logs(domain):
    # Search Certificate Transparency logs for the domain
    url = f"https://crt.sh/?q={domain}&output=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to query CT logs")


def find_matching_subdomain(modulus, ct_entries):
    for entry in ct_entries:
        subdomain = entry.get("name_value")
        if subdomain:
            print(f"Checking certificate for subdomain: {subdomain}")
            # Retrieve certificate details from crt.sh
            crt_id = entry.get("id")
            crt_url = f"https://crt.sh/?d={crt_id}"
            crt_response = requests.get(crt_url)
            if crt_response.status_code == 200:
                try:
                    # Parse the certificate to check modulus
                    cert_data = crt_response.content
                    public_key = serialization.load_der_public_key(cert_data, backend=default_backend())
                    if isinstance(public_key, rsa.RSAPublicKey):
                        cert_modulus = public_key.public_numbers().n
                        if cert_modulus == modulus:
                            return subdomain
                except Exception as e:
                    continue
    return None


def main():
    # Specify the path to your PEM file
    pem_file_path = 'transparency.pem'

    # Extract RSA parameters
    modulus, exponent = extract_rsa_key_parameters(pem_file_path)
    print("Modulus:", modulus)
    print("Exponent:", exponent)

    # Search CT logs for cryptohack.org
    domain = "cryptohack.org"
    print(f"Searching CT logs for {domain}...")
    ct_entries = search_ct_logs(domain)

    # Find the matching subdomain
    print(f"Found {len(ct_entries)} certificates in CT logs.")
    matching_subdomain = find_matching_subdomain(modulus, ct_entries)

    if matching_subdomain:
        print(f"Matching Subdomain: {matching_subdomain}")
        print(f"Visit the subdomain to retrieve the flag: {matching_subdomain}")
    else:
        print("No matching subdomain found.")


if __name__ == '__main__':
    main()
#thetransparencyflagishere.cryptohack.org go to this site and find the flag