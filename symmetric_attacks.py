#!/usr/bin/env python3
print('''
Symmetric Cipher Attack Toolkit
- ECB byte-at-a-time attack
- CBC padding oracle attack
- CTR bit-flipping attack
- IV reuse attack
- Stream cipher key reuse

Usage:
  python3 symmetric_attacks.py --ecb-oracle <oracle_url>
  python3 symmetric_attacks.py --padding-oracle <target_url> <ciphertext>
  python3 symmetric_attacks.py --cbc-bitflip <ciphertext> <original> <desired>
  python3 symmetric_attacks.py --stream-reuse <c1> <c2>

How It Works:

ECB Byte-at-a-Time: Feeds incrementing byte strings to an ECB oracle.
By detecting block boundaries (16 bytes for AES-ECB), an attacker can
recover the secret suffix one byte at a time using controlled prefixes.

Padding Oracle: Sends modified ciphertexts to a server that reveals
whether padding is valid. Each byte of plaintext can be recovered with
at most 256 oracle queries per byte. This decrypts arbitrary data
without the key.

CTR Bit-Flipping: XORs modified ciphertext bytes to change the
decrypted plaintext at known positions. Since CTR mode encrypts
a counter, the plaintext can be altered predictably.

IV Reuse: When the same key+IV pair encrypts multiple messages,
a simple XOR between ciphertexts reveals the XOR of plaintexts.

Stream Cipher Key Reuse: Two-time pad attack. XOR two ciphertexts
encrypted with the same keystream to get the XOR of plaintexts,
then use crib dragging to recover both messages.
''')
