n = 5
fears = [2,3,1,2,2]

fears.sort()
print(fears)

ans = 0
tmp_members = []
for fear in fears:
    tmp_members.append(fear)
    
    if len(tmp_members) >= max(tmp_members):
        ans += 1
        tmp_members = []
print(ans)