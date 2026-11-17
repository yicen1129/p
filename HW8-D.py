n = int(input())

stock = {}

# 輸入初始商品庫存
for i in range(n):
    item, qty = input().split()
    stock[item] = int(qty)

q = int(input())

success = 0
failed = 0

# 處理進貨與購買
for i in range(q):
    command, item, qty = input().split()
    qty = int(qty)

    if command == "ADD":
        stock[item] = stock.get(item, 0) + qty

    elif command == "BUY":
        if item in stock and stock[item] >= qty:
            stock[item] -= qty
            success += qty
        else:
            failed += 1

# 輸出成功售出總數與被拒絕的購買筆數
print(success, failed)

# 依商品名稱排序輸出
for item in sorted(stock):
    print(item, stock[item])
