n= input();

k=[]
for i in range(len(n)):
  k.append(int(n[i]))

k.sort(reverse=True)

for i in range(len(n)):
  print(k[i],end="")
