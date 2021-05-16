n=int(input())
k= list(map(int,input().split()))
k.sort()
if len(k)%2==1:
  print(k[len(k)//2]**2)
else:
  print(k[0]*k[-1])
