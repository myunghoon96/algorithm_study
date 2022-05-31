# https://www.acmicpc.net/problem/11057
from collections import defaultdict

N = int(input())
count_dic = defaultdict(int)

for i in range(10):
    count_dic[i] = 1

for idx in range(1, N):
    new_count_dic = defaultdict(int)
    for num, cnt in count_dic.items():
        for i in range(num,10):
            new_count_dic[i] += cnt
    count_dic = new_count_dic

print(sum(count_dic.values())%10007)
