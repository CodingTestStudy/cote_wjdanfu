def fibo(N):
    if N==0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 1
    else:
        return fibo(N-1)+fibo(N-2)

a = int(input())
print(fibo(a))