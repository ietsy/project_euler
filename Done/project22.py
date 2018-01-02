f = open('p022_names.txt', 'r')  
names = f.read().split('","')
names[0] = "MARY"
names.sort()

def score(name, number):
    s = 0
    for char in name:
        if char == "A":
            s += 1
        elif char == "B":
            s += 2
        elif char == "C":
            s += 3
        elif char == "D":
            s += 4
        elif char == "E":
            s += 5
        elif char == "F":
            s += 6
        elif char == "G":
            s += 7
        elif char == "H":
            s += 8
        elif char == "I":
            s += 9
        elif char == "J":
            s += 10
        elif char == "K":
            s += 11
        elif char == "L":
            s += 12
        elif char == "M":
            s += 13
        elif char == "N":
            s += 14
        elif char == "O":
            s += 15
        elif char == "P":
            s += 16
        elif char == "Q":
            s += 17
        elif char == "R":
            s += 18
        elif char == "S":
            s += 19
        elif char == "T":
            s += 20
        elif char == "U":
            s += 21
        elif char == "V":
            s += 22
        elif char == "W":
            s += 23
        elif char == "X":
            s += 24
        elif char == "Y":
            s += 25
        elif char == "Z":
            s += 26
    return(s*number)

L = []
for i in range(len(names)):
    L.append(score(names[i], i+1))
print(sum(L))