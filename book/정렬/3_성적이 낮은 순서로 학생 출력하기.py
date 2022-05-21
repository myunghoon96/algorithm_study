n = 2
grades = [['홍길동', 95], ['이순신', 27]]

grades.sort(key = lambda x : x[1])

ans = [e[0] for e in grades]
print(*ans)