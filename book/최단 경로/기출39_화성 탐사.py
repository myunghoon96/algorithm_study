import heapq

T = 1

for _ in range(T):
    N = 3
    matrix = [
        [5, 5, 4],
        [3, 9, 1],
        [3, 2, 7],
    ]

    N = 5
    matrix = [
        [3,7,2,0,1],
        [2,8,0,9,1],
        [1,2,1,8,1],
        [9,8,9,2,0],
        [3,6,5,1,5],
    ]

    # N = 7
    # matrix = [
    #     [9,0,5,1,1,5,3],
    #     [4,1,2,1,6,5,3],
    #     [0,7,6,1,6,8,5],
    #     [1,1,7,8,3,2,3],
    #     [9,4,0,7,6,4,1],
    #     [5,8,3,2,4,8,3],
    #     [7,4,8,4,8,3,4],
    # ]


    distances = [[int(1e9)] * N for _ in range(N)]
    q = [(matrix[0][0], 0, 0)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        dist, x, y = heapq.heappop(q)

        if dist > distances[x][y]:
            continue
        distances[x][y] = dist

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N:
                heapq.heappush(q, (dist + matrix[xx][yy], xx, yy))
        
    print(distances[-1][-1])
