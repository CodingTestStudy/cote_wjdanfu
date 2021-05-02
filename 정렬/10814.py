n=int(input())
k=[[str(x) for x in input().split()]for y in range(n)]
k.sort(key=lambda x:int(x[0]))
for i in range(len(k)):
  print(k[i][0],k[i][1])
