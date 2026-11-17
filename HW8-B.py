n = int(input())

runners = []

for i in range(n):
    name, time, penalty = input().split()

    time = int(time)
    penalty = int(penalty)

    total = time + penalty

    runners.append((name, time, penalty, total))

# 依照總秒數、原始秒數、姓名排序
runners = sorted(runners, key=lambda x: (x[3], x[1], x[0]))

# 輸出結果
for runner in runners:
    print(runner[0], runner[3])
