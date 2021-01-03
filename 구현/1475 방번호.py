import math
room = list(map(int,str(input())))

set_num=[0]*10

for i in room:
  if i==9 or i==6:
    set_num[9]+=0.5
  else:
    set_num[i]+=1

print(int(math.ceil(max(set_num)))) # 올림하면 정수형으로 바뀌어서 굳이 int로 형변환 할 필요는 없음.

# 아이디어는 바로 생각났지만 파이썬 문법구현에 익숙해지자
