
# 儲存所有輸入紀錄
records = []

# 輸入資料筆數
N = int(input())

for i in range(N):
    user, item = input().split()
    records.append((user, item))

# 輸入目標使用者及推薦數量
target, K = input().split()
K = int(K)

# 建立每位使用者購買商品的 dict
users = {}

for user, item in records:
    if user not in users:
        users[user] = set()
    users[user].add(item)

# 取得目標使用者購買的商品
target_items = users[target]

# 計算推薦商品分數
scores = {}

for user in users:
    # 排除目標使用者
    if user == target:
        continue

    # 判斷是否為相似使用者
    if users[user] & target_items:

        # 找出相似使用者買過但目標使用者沒買過的商品
        new_items = users[user] - target_items

        # 累計商品分數
        for item in new_items:
            if item not in scores:
                scores[item] = 0
            scores[item] += 1

# 依照分數由大到小、商品名稱由小到大排序
result = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

# 取前 K 名
R = min(K, len(result))

if R == 0:
    print(0)
else:
    print(R)
    for item, score in result[:R]:
        print(item, score)