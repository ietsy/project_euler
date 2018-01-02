def even(n):
    return(n/2)

def uneven(n):
    return(3*n+1)
    
def chain(n):
    l = [n]
    while n != 1:
        if n%2 == 0:
            n = even(n)
        else:
            n = uneven(n)
        l.append(n)
    return(l)

maxlengh = 0
maxnr = 0
for i in range(1,1000000):
    if len(chain(i)) > maxlengh:
        maxlengh = len(chain(i))
        maxnr = i
        print(maxnr, maxlengh)
        
print(maxnr, maxlengh)
