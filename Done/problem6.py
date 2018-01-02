def sumofsquares(n):
    s = 0
    for i in range(n+1):
        s += i * i
    return s
    
def squareofsum(n):
    return sum(range(n+1)) * sum(range(n+1))
    
print(squareofsum(100) - sumofsquares(100))