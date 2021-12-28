import sys
import math

input = sys.stdin.readline
n,r=map(int,input().split())

print(math.factorial(n)//(math.factorial(n-r)*math.factorial(r)))


