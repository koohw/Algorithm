# 2178. 미로탐색
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def search_maze(y, x):
    global cnt
    q = deque()
    q.append((1, y, x))
    visited[y][x] = 1

    while q:    # q가 비어있지 않을 동안 반복
        move, y, x = q.popleft()

        if y == N - 1 and x == M - 1:
            cnt = min(cnt, move)
            break

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<M and maze[ny][nx] and not visited[ny][nx]:
                q.append((move + 1, ny, nx))
                visited[ny][nx] = 1 # 방문 처리



N, M = map(int, input().split())    # N x M: 세로 x 가로
maze = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = float('inf')
search_maze(0, 0)
print(cnt)
