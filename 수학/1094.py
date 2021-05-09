n=int(input())

b=format(n,'b')
result=0
for i in range(len(b)):
  if b[i]=='1':
    result+=1


print(result)
