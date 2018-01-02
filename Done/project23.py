def list_abundant(m):
    abundant = []
    for i in range(12,m):
        s = 0
        for j in range(1,i/2+1):
            if i%j == 0:
                s+=j
        if s>i:
            abundant.append(i)
    return(abundant)

def check_if_sum(n, abundants):
    for i in abundants:
        if i < n and n - i in abundants:
            return True
    return False

m = 28123 
L= list_abundant(m)
print(L)
s = []
last = 0
for i in range(1, m+1):
    if not check_if_sum(i, L):
        percentage = 100 * i/(m+1)
        if percentage%10 == 0 and percentage != last:
            last = percentage
            print(percentage, "% done")
        s.append(i)
print(s)
print(sum(s))