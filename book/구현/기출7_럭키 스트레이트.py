#https://www.acmicpc.net/problem/18406

n = input()

mid = len(n)//2
left, right = map(int, n[:mid]), map(int, n[mid:])

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")