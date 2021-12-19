import sys

input=sys.stdin.readline

a=input().strip()
inverse=[]
k=False
flag=0
for i in a:
    if (i=="<" and len(inverse)!=0) or (flag==len(a) and k ==False) or (i==" " and len(inverse)!=0 and k==False):
        print(''.join(inverse[::-1]).strip(),end="")
        inverse=[]
        if i==' ':
            print(" ",end="")
    if i=="<" or k==True:
        print(i,end="")
        k=True
        if i==">":
            k=False
    else:
        inverse.append(i)
    flag+=1
if len(inverse)!=0:
    print(''.join(inverse[::-1]).strip(),end="")