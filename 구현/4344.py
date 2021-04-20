N=int(input())

for _ in range(N):
  A=list(map(int,input().split()))
  result=0;
  average=0;
  add=0
  for i in range(1,A[0]+1):
    result+=A[i]
  average=(result/A[0])
  for i in range(1,A[0]+1):
    if A[i]>average:
     add+=1
  result = add/A[0]*100
  print(format(result,".3f"),end='%\n')
