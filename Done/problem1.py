def main():
    m = int(raw_input("Give max natural number: "))
    l = []
    for i in range(m):
        if i%3 == 0:
            l.append(i)
        elif i%5 == 0:
            l.append(i)
    print(l)
    print(sum(l))
main()