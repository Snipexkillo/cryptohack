e = __import__("Structure of AES")


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    new = []
    for a in range(len(k)):
        temp = []
        for al in range(len(k[a])):
            temp.append(k[a][al] ^ s[a][al])
        new.append(temp)
    return new

print(e.matrix2bytes(add_round_key(state, round_key)))
