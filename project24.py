import itertools

def permutations(s):
    l = []
    for char in str(s):
        l.append(char)
    l.sort()
    L = list(itertools.permutations(l))
    return L

L = permutations(1234567890)
print(L[1000000 -1])
print(''.join(L[1000000 -1]))