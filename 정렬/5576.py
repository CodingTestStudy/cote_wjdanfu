w=[]
k=[]
for i in range(10):
  k.append(int(input()))
for i in range(10):
  w.append(int(input()))
k.sort()
w.sort()
print(k[-1]+k[-2]+k[-3],w[-1]+w[-2]+w[-3])
