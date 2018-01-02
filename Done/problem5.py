def check(n, r):
    for i in range(1,r):
        if n%i != 0:
            return(False)
    return(True)
            
def main(r):
    i = r * r
    while True:
        if check(i, r):
            return(i)
        i += r

print(main(20))