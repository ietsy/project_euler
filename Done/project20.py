def factorial(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s
    
def sumchar(n):
    s = str(n)
    l = []
    for char in s:
        l.append(int(char))
    return sum(l)

n = 100
print(n)
nf = factorial(n)
print(nf)
ns = sumchar(nf)
print(ns)
