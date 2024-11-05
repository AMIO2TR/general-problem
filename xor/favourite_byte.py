from binascii import unhexlify
import string

def single_byte_xor(input, key):
	if len(chr(key)) != 1:
		raise "key length exception: in single_byte_xor key must be 1 byte long!"

	output = b''
	for b in input:
		output += bytes([b ^ key])

	try: 
		return output.decode("utf-8")
	except: 
		return "can not decode some bytes"


data = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
decode = unhexlify(data)

print("[-] Hex_decode: {}\n".format(decode))

result = {}

for i in range(256):
	result[i] = single_byte_xor(decode, i)

print("[*] FLAG: {}".format([s for s in result.values() if "crypto" in s]))

