x= list(map(int,input().split()))

if x[0]*x[1]/x[2]>x[0]/x[1]*x[2]:
  print(int(x[0]*x[1]/x[2]))
else:
  print(int(x[0]/x[1]*x[2]))
