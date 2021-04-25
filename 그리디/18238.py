N= input()
K=0
if abs(ord('A')-ord(N[0]))>=13:
  K+=(26-(abs(ord('A')-ord(N[0]))))
else:
  K+=(abs(ord('A')-ord(N[0])))

for i in range(len(N)-1):
  if abs(ord(N[i])-ord(N[i+1]))>=13:
    K+=(26-(abs(ord(N[i+1])-ord(N[i]))))
  else:
    K+=(abs(ord(N[i+1])-ord(N[i])))

print(K)
