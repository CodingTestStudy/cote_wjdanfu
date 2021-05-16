n=int(input())

for i in range(n):
  a,b=map(int,input().split())
  c=a
  for j in range(b-1):
    if c*a<=10:
      c=c*a
    else:
      c=(c*a)%10

if a==10:
  print(10)
else:
  print(c)
