d = __import__('Diffie-Hellman.decrypt')
from pwn import *
import re

c = remote('socket.cryptohack.org', 13371)
c.recv()

alice = str(c.recv())
alice = '{' + re.split(r'[{}]', alice)[1] + '}'
c.send(alice.encode())
alice = eval(alice)

c.recv()
bob = str(c.recv())
bob = eval('{' + re.split(r'[{}]', bob)[1] + '}')
g = int(alice['g'], 16)
p = int(alice['p'], 16)
A = int(alice['A'], 16)
bob["B"] = "0x" + "{:02x}".format(pow(g, 2, p))
al =('{' + re.split(r'[{}]', str(bob))[1].replace("\'", "\"") + '}').encode()
c.send(al)
key = pow(A, 2 ,p)

c.recv()
eve = c.recv().decode()
eve = eval('{' + re.split(r'[{}]', eve)[1] + '}')
print(d.decrypt.decrypt_flag(key, eve['iv'], eve['encrypted_flag']))

c.close()