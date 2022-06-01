# https://www.acmicpc.net/problem/1946
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    infos = [list(map(int, input().split())) for _ in range(N)]
    infos.sort()
    # print(infos)
    ans = 1
    interview_cutline = infos[0][1]
    for i in range(1, len(infos)):
        document, interview = infos[i]

        if interview < interview_cutline:
            # print(document, interview)
            ans += 1
            interview_cutline = interview
    print(ans)