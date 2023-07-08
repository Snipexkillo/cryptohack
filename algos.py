def gcd(a,b): #Euclidean algo
    while a!= b:
        if (a>b):
            a -= b
        elif(a<b):
            b -= a
    return a

def gcd2(a,b): #faster Euclidean algo
    while True:
        if(a>b):
            a = a%b
        elif(b>a):
            b = b%a
        if(a == 0 or b == 0):
            break
    if a == 0:
        return b
    return a

def EEA(a, b): #extended Euclidean Algo
               #if its pa + sb = gcd(a,b), this returns p (or in other words it returns a^-1 for a * a^-1 = 1 mod b)
               #http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
               #used to make it so that it returns the value for a
    temp = a
    a = b
    b = temp
    #setting up our variables and starting the algo
    quotient2 = a//b #contains the quotient 2 back from the current loc
    temp = b
    b = a%b
    a = temp
    quotient1 = a//b #contains the quotient 1 back from the current loc
    p2 = 0          #contains the p-value 2 back from the current loc
    p1 = 1          #contains the p-value 1 back from the current loc
    #running the algo
    while True:
        #Euclidean algo part
        temp = b
        b = a % b
        a = temp

        #Extended Euclidean algo part
        pcur = (p2 - p1 * quotient2)
        if (a == 0 or b == 0):
            break
        p2 = p1
        p1 = pcur
        quotient2 = quotient1
        quotient1 = a//b
    return pcur

def Tonneli_Shanks(a, p): #finds r for r^2 = a (mod p)
                          # use only when p = 1 (mod 4), use r = a^((p+1)//4) for p = 3 (mod 4)
    S = 0
    Q = p - 1

    quadnonres = 0
    while Q % 2 == 0:
        S += 1
        Q = Q // 2
    M = S
    for i in range(p):
        print(i)
        if pow(i, (p - 1) // 2, p) == p - 1:
            quadnonres = i
            break
    t = pow(a, Q, p)  # n^Q
    c = pow(quadnonres, Q, p)
    Root = pow(a, (Q + 1) // 2, p)
    b2 = 1
    i = 0
    while t != 1:
        count = 0
        while True:

            if pow(t, pow(2, count), p) == 1:
                break
            count += 1

        print(type(pow(2, M - count - 1)))
        if isinstance(pow(2, M - count - 1), float):
            print(pow(2, M - count - 1))
            print(t)
        b = pow(c, pow(2, M - count - 1), p)
        M = count
        c = pow(b, 2, p)
        t = c * t % p
        Root = Root * b % p
    return Root

def rootn(x, n): # calculates nth root of x using
    high = 1
    while pow(high, n) < x:
        high = pow(high, 2)
    low = high//2

    while low<high:
        mid = (low + high)//2
        if low < mid and pow(mid, n) < x:
            low = mid
        elif high > mid and pow(mid, n) > x:
            high = mid
        else:
            return mid
    return mid + 1
