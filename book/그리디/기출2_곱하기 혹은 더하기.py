from collections import Counter

s = '02984'
counter = Counter(s)
if counter[0] == len(s):
    print(0)
    exit(0)

ans = 1
for e in s:
    e = int(e)
    if e == 0:
        continue
    else:
        ans *= e
print(ans)