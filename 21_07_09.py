# 백준 > BFS/DFS > 섬의개수(4963번)
def bfs(island):
    queue = deque()
    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [1,-1,0,0,1,-1,-1,1]
    cnt = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if visited[i][j]==False and island[i][j]==1:
                visited[i][j]=True
                queue.append(i)
                queue.append(j)
                while queue:
                    x = queue.popleft()
                    y = queue.popleft()
                    for k in range(8):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0<=nx<h and 0<=ny<w and island[nx][ny]==1 and visited[nx][ny]==False:
                            queue.append(nx)
                            queue.append(ny)
                            visited[nx][ny]=True
                cnt+=1
    print(cnt)



import sys
from collections import deque

w,h = map(int,sys.stdin.readline().split())
while (w!=0 and h!=0):

    island = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    bfs(island)

    w,h = map(int,sys.stdin.readline().split())

#dfs 참고 풀이
def dfs(y, x):
    graph[y][x] = 0
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < h) and (0 <= X < w) and graph[Y][X] == 1:
            dfs(Y, X)

while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)