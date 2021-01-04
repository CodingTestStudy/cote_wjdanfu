n = int(input())

t = n
count = 0

while True:
    a = t // 10  # 주의 파이싼에서 몫만 나오는 나눗셈은 // 이다
    b = t % 10

    c = a + b
    tmp = b * 10 + c % 10
    t = tmp
    count += 1
    if tmp == n:
        break

print(count)

