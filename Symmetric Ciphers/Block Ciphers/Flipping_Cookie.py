import requests
from datetime import datetime, timedelta

cookie = requests.get("https://aes.cryptohack.org/flipping_cookie/get_cookie/").json()["cookie"]
iv = bytes.fromhex(cookie[:32])
original = "admin=False;expi".encode()
new = "admin=True;expir".encode()
newiv = bytes(a ^ b ^ c for a, b, c in zip(iv, original, new)).hex()
print(newiv)
flag = requests.get(f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie[32:]}/{newiv}").json()
print(flag)
