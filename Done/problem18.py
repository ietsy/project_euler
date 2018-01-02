l = []
with open('18.txt') as f:
    for line in f:
        l.append([int(i) for i in line.rstrip('\n').split(" ")])
        
for i,j in [(i,j) for i in range(len(l)-2,-1,-1) for j in range(i+1)]:
    l[i][j] +=  max([l[i+1][j],l[i+1][j+1]])
    
print l[0][0]