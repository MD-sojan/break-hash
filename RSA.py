import math
from Crypto.Util.number import long_to_bytes

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def factor_rsa(N):
    print("Attempting to factor N...")
    for i in range(2, 1000000):
        if N % i == 0:
            return i, N // i
    raise Exception("Failed to factor N. Try a more powerful factorization tool.")

def recover_flag(N, e, cyphertext):
    p, q = factor_rsa(N)
    print(f"Factors found: p = {p}, q = {q}")

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    decrypted = pow(cyphertext, d, N)
    flag = long_to_bytes(decrypted)

    print("Decrypted flag:", flag.decode(errors='ignore'))


if __name__ == "__main__":
    # Example inputs (replace with actual values from the program)
    N = int(input("Enter N: "))
    e = 65537
    cyphertext = int(input("Enter cyphertext: "))

    recover_flag(N, e, cyphertext)
