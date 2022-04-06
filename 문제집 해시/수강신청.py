
import sys
from collections import defaultdict

input = sys.stdin.readline

a,b = map(int,input().split())

my_dict = defaultdict(int)

for i in range(b):
    m=(input())
    my_dict[m]=i

count = 0
my =(sorted(my_dict.items(), key=lambda x: x[1]))
# print(my)
for i in my:
    if count == a:
        break
    print(i[0])
    count+=1