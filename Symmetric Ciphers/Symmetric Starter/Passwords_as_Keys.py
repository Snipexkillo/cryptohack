from Crypto.Cipher import AES
import hashlib

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    #key = bytes.fromhex(password_hash)

    cipher = AES.new(password_hash, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return bytes.fromhex(decrypted.hex())


ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for w in words:
    key = hashlib.md5(w.encode()).digest()
    al = decrypt(ciphertext, key)
    print(str(al))
    if 'crypto' in str(al):
        print(w)
        print(hashlib.md5(w.encode()).digest().hex())
        break

