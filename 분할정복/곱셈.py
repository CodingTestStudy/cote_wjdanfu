import sys
input=sys.stdin.readline

A,B,C=map(int,input().split())


def solve(a,b):
    if b==1:
        return a % C
    else:
        temp = solve(a,b//2)
    
    if b % 2 == 1:
        return temp * temp * a % C
    else:
        return temp * temp %C

print(solve(A,B))