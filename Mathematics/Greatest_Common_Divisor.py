def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
a=66528
b=52920
print("GCD of", a, "and", b, "is:", gcd(a, b))
