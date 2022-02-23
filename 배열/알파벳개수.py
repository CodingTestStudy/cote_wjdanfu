c = input()

freq = [0]*26

for i in c:
    freq[ord(i)-97]+=1
for i in range(len(freq)):
    print(freq[i],end=" ")