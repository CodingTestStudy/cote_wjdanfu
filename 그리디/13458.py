N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())

result=0
for i in A:
  i-=B
  result+=1
  if i<0:
    continue
  if i%C==0:
    result+=i//C
  if i%C!=0:
    result+=(i//C)+1

print(result)

#
