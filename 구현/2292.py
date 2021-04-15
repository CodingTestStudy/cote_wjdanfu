a= int(input())
result=1
start=1
i=1
while a>start:
    result+=1
    start+=6*i
    i+=1

print(result)
