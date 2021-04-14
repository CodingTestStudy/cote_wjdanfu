namugy=[]

for _ in range(10):
  namugy.append(int(input())%42)

result=set(namugy)

print(len(result))
