import sys
from collections import defaultdict

input = sys.stdin.readline

start, mid, end = map(str,input().split())
start_h, start_m = start.split(":")
mid_h, mid_m = mid.split(":")
end_h, end_m = end.split(":")

start = int(start_h)*60+int(start_m)
mid = int(mid_h)*60+int(mid_m)
end = int(end_h)*60+int(end_m)

dic = defaultdict(str)

count = 0
while True: 
    try:
        k = input().strip()
        time, name = map(str,k.split())
        time_h, time_m = time.split(":")
        time = int(time_h)*60+int(time_m)
        if time <= start:
            dic[name] = 'enter'
            continue
        
        if mid <= time <= end:
            if dic[name] == 'enter':
                dic[name] = 'accept'
                count+=1
    except:
        break
print(count)