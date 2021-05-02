n=int(input())
k=[]
for i in range(n):
  k.append(int(input()))

k.sort()

result=k[0]*n
num=0
for i in range(1,n):
  num=k[i]*(n-i)
  if num>result:
    result=num

print(result)
