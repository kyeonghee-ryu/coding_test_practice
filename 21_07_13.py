# 백준 > 유기농 배추(1012번)

def bfs(m,n,b):
    grid = [[0]*m for _ in range(n)]
    for i in range(len(b)):
        grid[b[i][1]][b[i][0]]=1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    cnt=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and grid[i][j]==1:
                visited[i][j]=1
                queue.append(i)
                queue.append(j)
                while queue:
                    x = queue.popleft()
                    y = queue.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]==1 and visited[nx][ny] == 0:
                            queue.append(nx)
                            queue.append(ny)
                            visited[nx][ny] = 1
                cnt+=1
    print(cnt)

from collections import deque
import sys
number = int(sys.stdin.readline())

for _ in range(number):
    m,n,k = map(int,sys.stdin.readline().split())
    b = []
    for _ in range(k):
        b.append(list(map(int,sys.stdin.readline().split())))
    bfs(m,n,b)