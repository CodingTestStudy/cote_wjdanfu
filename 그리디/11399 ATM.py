h=int(input());

man = list(map(int,input().split()))

man.sort();
result=0
su=0
for i in range(h):
  su+=man[i]
  result+=su
print(result)

