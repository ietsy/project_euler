def sum_divisors(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s += i
    return s

def makelist(n):
    L = []
    for i in range(1,n):
        L.append([i, sum_divisors(i)])
    s = []
    for i in L:
        if [i[1], i[0]] in L and [i[1], i[0]] not in s and i[0] != i[1]:
            s.append(i)
    return(s)

def flatten(L):
    return([item for sublist in L for item in sublist])

an = makelist(10000)
print(sum(flatten(an)))