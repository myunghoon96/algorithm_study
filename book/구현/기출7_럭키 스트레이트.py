n = '123402'
n = '7755'

mid = len(n)//2
left, right = map(int, n[:mid]), map(int, n[mid:])

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")