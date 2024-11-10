from Crypto.Util.number import inverse, long_to_bytes

x = 6 % 11
y =  8146798528947 % 17

find_min = min(x,y)

print(find_min)