# https://www.acmicpc.net/problem/17609

t = int(input())

for _ in range(t):
    sentence = input()

    if sentence == sentence[::-1]:
        print(0)
        continue

    l,r = 0, len(sentence)-1
    ans = 0
    while l < r:
        if sentence[l] == sentence[r]:
            l+=1
            r-=1
        else:
            if sentence[l+1:r+1]==sentence[l+1:r+1][::-1] or sentence[l:r] == sentence[l:r][::-1]:
                ans = 1
                break
            else:
                ans = 2
                break
                
    if ans == 1:
        print(1)
    elif ans ==2:
        print(2)
