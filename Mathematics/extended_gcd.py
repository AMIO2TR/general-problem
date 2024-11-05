def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    gcd_val, u1, v1 = extended_euclidean_algorithm(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    return gcd_val, u, v

# Input from user
p = int(input("Enter first number (p): "))
q = int(input("Enter second number (q): "))

# Calculating GCD, LCM, and coefficients u, v
gcd_val = gcd(p, q)
lcm_val = lcm(p, q)
gcd_val, u, v = extended_euclidean_algorithm(p, q)

# Displaying results
print(f"GCD of {p} and {q} is: {gcd_val}")
print(f"LCM of {p} and {q} is: {lcm_val}")
print(f"The values of u and v are: u = {u}, v = {v}")
print(f"Verification: {p}*{u} + {q}*{v} = {gcd_val}")