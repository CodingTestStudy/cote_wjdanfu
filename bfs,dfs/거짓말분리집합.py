import sys
input=sys.stdin.readline

N,M = map(int,input().split())

know=input().strip()
if know[0]=='0':
    print(M)
else:
    know=know[2:]
    know = list(map(int,know.split()))

party=[]
for i in range(M):
    dist=list(map(int,input().split()))
    party.append(dist[1:])
if know[0]=='0':
    exit(0)
know=set(know)


while know:
    find=know.pop()
    for i in range(len(party)):
        try:
            if find in party[i]:
                know=know.union(party[i])
                party.pop(i)
        except:
            pass

print(len(party))
