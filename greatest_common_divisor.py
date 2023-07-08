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
def extendedEuclideanAlgo(a, b): #if its pa + sb = gcd(a,b), this returns p (or in other words it returns a^-1 for a * a^-1 = 1 mod b)
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

#print(extendedEuclideanAlgo(54, 888))


