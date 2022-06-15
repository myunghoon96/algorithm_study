# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(int(10e6))
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    selected = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N + 1)
    cycle_students = []

    def dfs(cur_student, tmp_visited):
        global cycle_students

        visited[cur_student] = True
        tmp_visited.append(cur_student)

        next_student = selected[cur_student]

        if not visited[next_student]:
            dfs(next_student, tmp_visited)

        elif visited[next_student]:
            if next_student in tmp_visited:
                # print(cur_student, next_student, tmp_visited)
                next_student_idx = tmp_visited.index(next_student)
                cycle_students += tmp_visited[next_student_idx:]

    for cur_student in range(1, N+1):
        if not visited[cur_student]:
            dfs(cur_student, [])
    
    print(N - len(cycle_students))