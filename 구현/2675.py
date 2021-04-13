a= int(input())
for _ in range(a):
  n,k=map(str,input().split())
  result=""
  for i in range(len(k)):
    result+=k[i]*int(n)
  print(result)
  
