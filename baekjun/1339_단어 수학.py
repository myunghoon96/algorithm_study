# https://www.acmicpc.net/problem/1339
from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input().rstrip())
alphas = [input().rstrip() for _ in range(N)]

# print(N, alphas)
dic = defaultdict(int)
for alpha in alphas:
    for i in range(len(alpha)):
        position = 10**(len(alpha) - 1 - i)
        dic[alpha[i]] += position

# print(dic)
alpha_list = sorted(dic.values(), reverse=True)
ans = 0
num = 9
for e in alpha_list:
    ans += (num*e)
    num -= 1
print(ans)
# print(alpha_list)