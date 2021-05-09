n=int(input())  #10
result=[]
i=1
while True:
  k=n+1 #11
  k*=i  #11 22 33 44 55 66 77 88 99
  if k>=n**2:
    break
  result.append(k)#11  22 33 
  i+=1

print(sum(result))
