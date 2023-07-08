import requests
import os
from Crypto.Cipher import AES

encr = requests.get(f"https://aes.cryptohack.org/bean_counter/encrypt/").json()["encrypted"]
important = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
keystream = bytes.fromhex("".join([hex(a^b)[2:] for a,b in zip(bytes.fromhex(encr[0:32]),important)]))
flag = []
for x in range((len(encr)+31)//32):
    flag.append(bytes([a^b for a,b in zip(bytes.fromhex(encr[x*32: (x+1)*32]),keystream)]))
f = open('bean_counter.png', 'wb')
al = b"".join(flag)
f.write(b"".join(flag))
f.close()
