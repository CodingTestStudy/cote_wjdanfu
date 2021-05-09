k=[]

m=int(input())
n=int(input())
x=m
while x>=m and x<=n:
  y= x**0.5
  if int(y)==y:
    k.append(x)
  x+=1

if len(k)!=0:
  print(sum(k))
  print(min(k))
else:
  print(-1)
