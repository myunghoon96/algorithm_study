n = 5
ans  = 0

for hh in range(n+1):
    for mm in range(0, 60):
        for ss in range(0, 60):
            tmp_str = str(hh) + str(mm) + str(ss)
            if '3' in tmp_str:
                ans += 1

print(ans)