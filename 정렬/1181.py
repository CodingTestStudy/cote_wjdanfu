n=int(input())
k=[]
for i in range(n):
  k.append(input())

result=set(k)

newresult=[]
for i in result:
  newresult.append([len(i),i])
newresult.sort()            # sort() 쓰면 첫번째 요소 정렬하고 같으면 두번쨰껄로 자동정렬함

for i in newresult:
  print(i[1])
