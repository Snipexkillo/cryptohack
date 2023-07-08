import requests

encr_flag = requests.get(f"https://aes.cryptohack.org/symmetry/encrypt_flag/").json()["ciphertext"]
iv = encr_flag[:32]
with0 = requests.get(f"https://aes.cryptohack.org/symmetry/encrypt/{(len(encr_flag)-32)*'0'}/{iv}/").json()["ciphertext"]
flag = bytes(a^b for a,b in zip(bytes.fromhex(with0), bytes.fromhex(encr_flag[32:])))
print(flag)