n = int(input())

records = set()
students = set()

# 讀取紀錄並去除重複資料
for i in range(n):
    student, booth = input().split()

    records.add((student, booth))
    students.add(student)

# 計算每位學生獲得的章數
count = {}

for student, booth in records:
    count[student] = count.get(student, 0) + 1

# 使用 list 儲存排行榜
ranking = []

for student in students:
    ranking.append((student, count[student]))

# 依章數由大到小，姓名由小到大排序
ranking.sort(key=lambda x: (-x[1], x[0]))

# 輸出有效紀錄總數
print(len(records))

# 輸出排行榜
for student, total in ranking:
    print(student, total)
