cur = 'a1'

# dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
# x, y = dic[cur[0]], int(cur[1])
x, y = int(ord(cur[0]))-ord('a')+1, int(cur[1])

ans = 0
moves = [(-2,-1), (-2, 1), (2,-1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

for move in moves:
    dx, dy = move
    xx = x+dx
    yy = y+dy
    if 1 <= xx <= 8 and 1 <= yy <= 8:
        print(xx, yy)
        ans += 1
print(ans)