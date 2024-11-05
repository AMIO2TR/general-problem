from Crypto.Util.number import long_to_bytes

KEY1 = int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313', 16)
b = int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', 16)
c = int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', 16)
d = int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf', 16)

key2 = b ^ KEY1
key3 = c ^ key2
flag = d ^ KEY1 ^ key2 ^ key3

print(long_to_bytes(flag))