def next_Fibonacci(n_1, n_2):
    n = n_1 + n_2
    return(n)

l = [1, 1]
while len(str(l[-1]))<1000:
    l.append(next_Fibonacci(l[-1],l[-2]))
print(len(l), l[-1])