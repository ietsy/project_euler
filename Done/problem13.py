f = open('13.txt', 'r')
l = f.read().split('\n')

for i in range(len(l)):
    l[i] = int(l[i])

s = str(sum(l))
print(s[0:10])