# Crypto Attack Toolkit 🔐

**4 cryptographic attack tools** — RSA, hash attacks, lattice cryptanalysis, symmetric cipher attacks.

## Tools

| Tool | Target | Techniques |
|------|--------|------------|
| `rsa_attacks.py` | RSA | Wiener, Fermat, Common modulus, Hastad, Small e |
| `hash_attacks.py` | Hash functions | Identification, Length extension, Collision |
| `lattice_crypto.py` | Lattice-based | LLL, HNP, DSA nonce, ECDSA, Knapsack |
| `symmetric_attacks.py` | Block/Stream ciphers | ECB oracle, Padding oracle, CTR bitflip, IV reuse |

## Installation

```bash
git clone https://github.com/ridhinva/Crypto-Attack-Toolkit.git
cd Crypto-Attack-Toolkit
pip install pycryptodome fpylll  # optional, for some modules
```

## Usage

```bash
# RSA Fermat factorization (p,q close)
python3 rsa_attacks.py --fermat 1234567890123456789012345678901234567890

# RSA Wiener attack (small d)
python3 rsa_attacks.py --wiener <n> <e>

# Hash identification
python3 hash_attacks.py --identify 5d41402abc4b2a76b9719d911017c592
```

## Author

**Ridhin V A** ([@c_y_p_h3r](https://x.com/c_y_p_h3r))


## Disclaimer

For authorized security testing and educational purposes only.
