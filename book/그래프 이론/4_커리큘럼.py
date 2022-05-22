from collections import deque, defaultdict
import copy

n = 5
infos = [
    [10,-1],
    [10,1,-1],
    [4,1,-1],
    [4,3,1,-1],
    [3,3,-1]
]

indegree = [0]*(n+1)
cost = [-1] * (n+1)

next_dic = defaultdict(list)
for idx, info in enumerate(infos):
    lecture = idx+1
    time = info[0]
    cost[lecture] = time
    pre_lectures = info[1:-1]
    for pre_lecture in pre_lectures:
        next_dic[pre_lecture].append(lecture)
    indegree[lecture] = len(pre_lectures)

# print(cost)
ans = copy.deepcopy(cost)
q = deque([])

for lecture in range(1, n+1):
    if indegree[lecture] == 0:
        q.append(lecture)

while q:
    lec = q.popleft()

    for next_lec in next_dic[lec]:
        indegree[next_lec] -= 1
        ans[next_lec] = max(ans[next_lec] , ans[lec] + cost[next_lec])
        if indegree[next_lec] == 0:
            q.append(next_lec)
            

for e in ans[1:]:
    print(e)