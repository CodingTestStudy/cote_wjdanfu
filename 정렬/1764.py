n,p=map(int,input().split())

N_list = [input() for i in range(n)]
P_list = [input() for i in range(p)]
duplicate = list(set(N_list) & set(P_list))


print(len(duplicate))
for i in sorted(duplicate):
  print(i)
