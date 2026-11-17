n, m = map(int, input().split())

A = set(input().split())
B = set(input().split())

# 交集：兩個社團都有參加
result1 = sorted(A & B)

# 聯集：至少參加一個社團
result2 = sorted(A | B)

# 只有 A 社團
result3 = sorted(A - B)

# 只有 B 社團
result4 = sorted(B - A)

# 輸出結果
for result in [result1, result2, result3, result4]:
    if len(result) == 0:
        print("NONE")
    else:
        print(" ".join(result))
