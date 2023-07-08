
p = 28151

for x in range(1,p):
    if pow(x, (p-1)//2, p) == 1:
        continue
    check = False
    for y in range(1, p-1):
        if pow(x, y, p) == 1:
            check = True
            break
    if check:
        continue
    print(x)
    break