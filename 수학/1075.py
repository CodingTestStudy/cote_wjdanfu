n=input()
n=n[0:len(n)-2]
k=int(input())
n+='00'

num=int(n)

while True:
  if num%k!=0:
    num+=1
  else:
    break
n=str(num)
print(n[-2:])
