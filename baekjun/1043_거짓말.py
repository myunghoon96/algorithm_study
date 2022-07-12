# https://www.acmicpc.net/problem/1043
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
knows = list(map(int, sys.stdin.readline().split()))
parties = []
for _ in range(M):
    party = list(map(int, sys.stdin.readline().split()))
    parties.append(party)

know_person = [False] * (N+1)
know_party = [False] * (M)
q = deque()

if knows[0] == 0:
    print(M)
    exit(0)

for person in knows[1:]:
    q.append(person)
    know_person[person] = True

while q:
    cur_person = q.popleft()
    # print('cur_person ', cur_person)
    for idx, party in enumerate(parties):
        if know_party[idx]:
            continue

        if cur_person in party[1:]:
            for p in party[1:]:
                if not know_person[p]:
                    q.append(p)
                    know_person[p] = True
            know_party[idx] = True

# print(know_person)
# print(know_party)
print(know_party.count(False))



