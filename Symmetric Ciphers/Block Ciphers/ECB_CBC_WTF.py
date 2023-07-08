import requests

ciphertext = requests.get(f"https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/").json()["ciphertext"]
flag = ""
url = f"https://aes.cryptohack.org/ecbcbcwtf/decrypt/"
for x in range(1, len(ciphertext)//32):
    flag += '{:032x}'.format((int(requests.get(f"{url}{ciphertext[32*x:32*(x+1)]}").json()["plaintext"], 16)^int(ciphertext[32*(x-1):32*x], 16)))

print(bytes.fromhex(flag))

