N = 10

dp = [0] * N
dp[0] = 1

idx2, idx3, idx5 = 0, 0, 0
nxt2, nxt3, nxt5 = 2, 3, 5

for i in range(1, N):
    dp[i] = min(nxt2, nxt3, nxt5)
    print('i ', i)
    print('dp ', dp)
    print('idx2, idx3, idx5 ', idx2, idx3, idx5)
    print('nxt2, nxt3, nxt5 ', nxt2, nxt3, nxt5)


    if dp[i] == nxt2:
        idx2 += 1
        nxt2 = dp[idx2] * 2

    if dp[i] == nxt3:
        idx3 += 1
        nxt3 = dp[idx3] * 3
    
    if dp[i] == nxt5:
        idx5 += 1
        nxt5 = dp[idx5] * 5

print(dp)     