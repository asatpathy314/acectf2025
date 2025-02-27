"""" SOURCE CODE
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

k = os.urandom(16) # Is it too short?

def encrypt(plaintext):
    cipher = AES.new(k, AES.MODE_CTR, counter=Counter.new(128)) # I was told, CTR can't be broken!
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()

msg = b'This is just a test message and can totally be ignored.' # Just checking functionality

encrypted_msg = encrypt(msg)

with open('flag.txt', 'r') as f:
    flag = f.readline().strip().encode()

encrypted_flag = encrypt(flag)

with open('msg.txt', 'w+') as o:
    o.write(f"{encrypted_msg}\n")
    o.write(f"{encrypted_flag}")
"""
with open('msg.txt', 'r') as f:
    encrypted_msg_hex = f.readline().strip()
    encrypted_flag_hex = f.readline().strip()

c1 = bytes.fromhex(encrypted_msg_hex)
c2 = bytes.fromhex(encrypted_flag_hex)

msg = b'This is just a test message and can totally be ignored.'

# Use the minimum length to handle varying message sizes
min_len = min(len(c2), len(msg))
c1_part = c1[:min_len]
msg_part = msg[:min_len]

# XOR the ciphertexts and then with the known plaintext
flag_xor = bytes([a ^ b for a, b in zip(c1_part, c2)])
flag = bytes([m ^ fx for m, fx in zip(msg_part, flag_xor)])

print(flag.decode())
