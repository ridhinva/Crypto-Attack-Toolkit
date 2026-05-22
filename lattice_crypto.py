#!/usr/bin/env python3
print('''
Lattice-based Cryptanalysis Toolkit
- LLL reduction
- Hidden Number Problem (HNP)
- DSA nonce recovery
- ECDSA bias attacks
- Knapsack cryptosystem attacks

Usage:
  python3 lattice_crypto.py --hnp <samples_file>
  python3 lattice_crypto.py --dsa-nonce-recovery <r> <s> <h>
  python3 lattice_crypto.py --knapsack <public_key>

Requires: fpylll (pip install fpylll)
''')
