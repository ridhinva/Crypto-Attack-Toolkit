#!/usr/bin/env python3
"""
RSA Attack Tool
- Wiener attack (small d)
- Fermat factorization (close p,q)
- Common modulus attack
- Hastad broadcast attack
- Small public exponent attack
- Coppersmith attack
"""
import sys, os, math
from math import gcd, isqrt

BANNER = '''
RSA Attack Toolkit
- Wiener (d < N^0.25)
- Fermat (p,q close)
- Common Modulus
- Hastad Broadcast
- Small e (cube root)
- Common factor (GCD)
'''

def fermat_factor(n):
    a = isqrt(n)
    if a * a < n:
        a += 1
    b2 = a * a - n
    while b2 >= 0:
        b = isqrt(b2)
        if b * b == b2:
            return a - b, a + b
        a += 1
        b2 = a * a - n
    return None, None

def wiener_attack(e, n):
    """Wiener's attack for small private exponent d"""
    def continued_fraction(num, den):
        cf = []
        while den:
            q = num // den
            cf.append(q)
            num, den = den, num - q * den
        return cf
    
    def convergents(cf):
        n0, n1 = 0, 1
        d0, d1 = 1, 0
        convs = []
        for a in cf:
            n2 = a * n1 + n0
            d2 = a * d1 + d0
            convs.append((n2, d2))
            n0, n1 = n1, n2
            d0, d1 = d1, d2
        return convs
    
    cf = continued_fraction(e, n)
    for k, d in convergents(cf):
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        # Check if phi is valid
        s = n - phi + 1
        discriminant = s * s - 4 * n
        if discriminant >= 0:
            sqrt_disc = isqrt(discriminant)
            if sqrt_disc * sqrt_disc == discriminant:
                return d
    return None

def main():
    print(BANNER)
    if len(sys.argv) < 2:
        print("Usage: python3 rsa_attacks.py <n> <e> [<ciphertext>]")
        print("       python3 rsa_attacks.py --fermat <n>")
        print("       python3 rsa_attacks.py --wiener <n> <e>")
        print("       python3 rsa_attacks.py --gcd <n1> <n2>")
        sys.exit(1)
    
    if sys.argv[1] == "--fermat":
        n = int(sys.argv[2])
        p, q = fermat_factor(n)
        if p and q:
            print(f"[+] Factors: p={p}\n           q={q}")
        else:
            print("[-] Fermat factorization failed")
    elif sys.argv[1] == "--wiener":
        n = int(sys.argv[2])
        e = int(sys.argv[3])
        d = wiener_attack(e, n)
        if d:
            print(f"[+] Private exponent d={d}")
        else:
            print("[-] Wiener attack failed (d may be large)")
    else:
        print("Specify an attack: --fermat, --wiener, --gcd")

if __name__ == "__main__":
    main()
