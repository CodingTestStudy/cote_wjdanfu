import sys
n = int(sys.stdin.readline())
length = int(sys.stdin.readline())

arr=sys.stdin.readline().strip()


count=0
pt=0
for i in range(1,length-1,2):
    if arr[i-1] == 'I' and arr[i]=='O' and arr[i+1]=='I':
        pt+=1
        if pt==n:
            pt-=1
            count+=1
    else:
        pt=0
print(count)