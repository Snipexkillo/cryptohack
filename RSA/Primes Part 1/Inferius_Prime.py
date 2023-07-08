import primefac, math, algos
from Crypto.Util.number import long_to_bytes

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373


phi = math.prod([pr-1 for pr in primefac.primefac(n)])
d = algos.EEA(e, phi)

print(long_to_bytes(pow(ct, d, n)))