import requests

url = "thetransparencyflagishere.cryptohack.org"
response = requests.get(url)
print(response.text)