# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    answer = -1

    def dfs(depth, remain_energy, visit):
        nonlocal answer
        answer = max(answer, len(visit))

        if depth == len(dungeons):
            return

        for i, dungeon in enumerate(dungeons):
            if i in visit:
                continue

            need, cost = dungeon
            if remain_energy >= need:
                dfs(depth + 1, remain_energy - cost, visit + [i])

        return

    dfs(0, k, [])

    return answer
