import sys
sys.stdin = open('input.txt','r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 유기농 배추
# 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접한 곳으로 지렁이가 이동 가능
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면
# 총 몇마리의 지렁이가 필요한지 알수 있음
# 0은 배추가 없는 땅, 1은 배추가 심어져 있는 땅
directions = [(-1,0),(0,-1),(1,0),(0,1)]   # 상하좌우

def find_baechu(y, x):
    q = []
    q.append((y, x))    # 현재 위치
    visited[y][x] = 1

    while q:
        y, x = q.pop(0)
        for dy, dx in directions:   # 현위치(지렁이)에서 배추가 상하좌우에 있는지 이동
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<M and field[ny][nx] == 1 and not visited[ny][nx]:    # 범위 내에 배추가 있다면 이동
                visited[ny][nx] = 1
                q.append((ny, nx))

T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split()) # M: 가로 N: 세로 K: 배추가 심어져 있는 위치의 개수
    field = [[0 for _ in range(M)] for _ in range(N)]

    for k in range(K):
        X, Y = map(int, input().split())    # 배추의 위치 X: 가로, Y: 세로
        field[Y][X] = 1

    visited = [[0 for _ in range(M)] for _ in range(N)]
    result = 0   # 필요한 지렁이 수

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                find_baechu(y, x)
                result += 1

    print(result)