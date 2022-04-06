import sys

n,X,Y = map(int,input().split())

k = 0
def zet(a,x,y):
    global k
    if x == X and y==Y:
        print(k)
        exit(0)
    if not (x <= X < x + a and y<= Y <y + a):
        k+=a**2
        return
    
    zet(a//2,x,y)
    zet(a//2,x, y + a//2)
    zet(a//2,x + a//2 ,y)
    zet(a//2,x + a//2 ,y + a//2)


zet(2**n,0,0)