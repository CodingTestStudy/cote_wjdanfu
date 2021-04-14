a,b=map(str,input().split())

c = a[2]+a[1]+a[0]
d= b[2]+b[1]+b[0]

if int(c)>int(d):
  print(c)
else:
  print(d)
#역순 하는법
#num1, num2 = input().split()
#num1 = int(num1[::-1])  # [::-1] : 역순
#num2 = int(num2[::-1])
