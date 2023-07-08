import algos as gcd
from Crypto.Util import number
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = (p-1) * (q-1)

print(gcd.extendedEuclideanAlgo(e, phi))
print(number.inverse(e, phi))