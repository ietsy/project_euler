def checkpalindrome(n):
    m = str(n)
    for i in range(len(m)/2):
        if not m[i] == m[-(i+1)]:
            return(False)
    return(True)

def findallpalindrome(digit):
    m = int(digit * "9")
    l = []
    for i in range(m):
        i2 = m - i
        for j in range(m):
            j2 = m - j
            if checkpalindrome(i2*j2):
                l.append(i2*j2)
    return(l)

print(max(findallpalindrome(3)))