n=int(input())
price=[]
for _ in range(n):
  k=list(map(int,input().split()))
  k.sort()
  if sum(k)/k[0] == 4:
    price.append(50000+k[0]*5000)
  elif k[1]==k[2]==k[3] or k[0]==k[1]==k[2]:
    price.append(10000+k[1]*1000)
  elif k[0]==k[1] and k[2]==k[3]:
    price.append(2000+k[0]*500+k[2]*500)
  elif k[0]==k[1] or k[1]==k[2] or k[2]==k[3]:
    if k[0]==k[1]:
      price.append(1000+k[0]*100)
    elif k[1]==k[2]:
      price.append(1000+k[1]*100)
    elif k[2]==k[3]:
      price.append(1000+k[2]*100)
  elif len(k)==len(set(k)):
    price.append(k[3]*100)


print(max(price))
