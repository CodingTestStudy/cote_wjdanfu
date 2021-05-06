from math import gcd          
n=int(input())
for i in range(n):
  a,b=map(int,input().split())
  print(a*b//gcd(a,b))          # gcd는 최대공약수 구해주는 함수
