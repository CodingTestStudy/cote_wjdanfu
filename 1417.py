
N=int(input())
k=[]
for i in range(N):
  k.append(int(input()))
result=0
dasom=k[0]

if N!=1:
  people=k[1:]
  people.sort()
  while people[-1]>=dasom:
    people[-1]-=1
    dasom+=1
    result+=1
    people.sort()
  

print(result)
