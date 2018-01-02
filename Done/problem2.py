def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)

limit = 4000000
l = [0, 1, 1]
while l[-1] < limit:
    l.append(Fibonacci(len(l)))
print(l)
answer = 0
for i in range(len(l)):
    if l[i]%2 == 0:
        answer += l[i]
print(answer)