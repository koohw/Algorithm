# 10/25
## 2178. 미로 탐색
```
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
```


# 10/24
## 1012. 유기농 배추
### 완성 코드
```buildoutcfg
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
    q.append((y, x))    # 현재 위치 추가하고 시작
    visited[y][x] = 1   # 현재 위치 방문 표시

    while q:
        y, x = q.pop(0)
        for dy, dx in directions:   # 현위치(지렁이)에서 배추가 상하좌우에 있는지 이동
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<M and field[ny][nx] == 1 and not visited[ny][nx]:    # 범위 내에 배추가 있고, 이동하지 않았던 곳이면 이동
                visited[ny][nx] = 1
                q.append((ny, nx))

T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split()) # M: 가로 N: 세로 K: 배추가 심어져 있는 위치의 개수
    field = [[0 for _ in range(M)] for _ in range(N)]   # 밭

    for k in range(K):
        X, Y = map(int, input().split())    # 배추의 위치 X: 가로, Y: 세로
        field[Y][X] = 1 # 배추가 있으면 1표시

    visited = [[0 for _ in range(M)] for _ in range(N)]
    result = 0   # 필요한 지렁이 수

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:  # 배추가 있고 방문하지않았으면
                find_baechu(y, x)                       # 현재 위치에서 함수 호출
                result += 1

    print(result)
```
### 로직
```buildoutcfg
1. 배추 밭 입력받기
2. (0, 0)부터 시작 -> bfs를 활용하여 배추가 있는 지 탐색
3. 현재 위치에서 상하좌우를 탐색했을 때 배추가 있으면(1이면) 이동하고, cnt + 1, 방문 표시
4. 현재 위치에서 상하좌우에 배추가 없으면 or 방문했을 경우 cnt 저장 후 초기화
5. cnt를 저장한 리스트 중에서 cnt가 1 이상인 것들(배추를 발견했을 때)의 갯수 세기
-> 문제점
1. ny, nx를 제대로 못처리함
2. else가 굳이 필요없음 
3. 상, 좌는 이미 탐색했을테니 하, 우만 탐색하면 visited배열을 안써도 되지 않을까 했는데 반례 존재..
4. 방향배열을 까먹은 이슈...
```
### 처음 구현 코드
```buildoutcfg
import sys
sys.stdin = open('input.txt','r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

directions = [(-1,0),(0,-1),(1,0),(0,1)]   # 상하좌우

def find_baechu(start):
    global cnt
    q = []
    q.append(start)

    while q:
        now = q.pop(0)
        for y in range(M):   # field[now]에 배추가 있는지 탐색
            for x in range(N):
                for dy, dx in directions:   # 현위치(지렁이)에서 배추가 상하좌우에 있는지 이동
                    ny, nx = y + dy, x + dx
                    if 0<=ny<M and 0<=nx<N and field[y][x] == 1:    # 범위 내에 배추가 있다면 이동
                        y, x = ny, nx
                        cnt += 1
                        q.append(field[y][x])
                else:
                    ans.append(cnt)
                    cnt = 0


T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split()) # M: 가로 N: 세로 K: 배추가 심어져 있는 위치의 개수
    field = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        X, Y = map(int, input().split())    # 배추의 위치 X: 가로, Y: 세로
        field[Y][X] = 1

    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    ans = []
    find_baechu(0)
    result = 0

    for a in ans:
        if a >= 1:
            result += 1
    print(result)
```

## 21736. 헌내기는 친구가 필요해
```buildoutcfg
# 캠퍼스 크기 N x M
# 상하좌우로 이동 -> 방향배열
# 캠퍼스 밖으로 이동할 수는 없음
# o는 빈공간, x는 벽, I는 도연이, P는 사람. I는 한번만 주어짐
# 첫째줄에 도연이가 만날 수 있는 사람 수 출력. 단, 아무도 만나지 못한 경우 TT 출력
# 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램

# 1. 도연이 위치 찾고 저장
# 2. 상하좌우로 이동하면서 P 찾기
# 3. P를 찾으면 cnt + 1
# 4. 더 이상 이동할 수 있는 곳이 없으면 종료 후 TT 출력
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

directions = [(-1,0),(1,0),(0,-1),(0,1)]   # 상하좌우
def find_friend(y, x):
    global cnt
    q = []
    q.append((y, x))
    visited[y][x] = 1

    while q:
        y, x = q.pop(0)
        for dx, dy in directions:
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<M and campus[ny][nx] != 'X' and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx))
                if campus[ny][nx] == 'P':
                    cnt += 1


N, M = map(int, input().split())    # 캠퍼스 크기 N x M
campus = [list(input().rstrip()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
start = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start_y, start_x = i, j

ans = []
cnt = 0
find_friend(start_y, start_x)  # 도연이 위치에서 탐색 시작
if cnt == 0:
    print('TT')
else:
    print(cnt)
```
### 로직
```buildoutcfg
1. 캠퍼스를 2차원 리스트로 입력받기
2. 도연이 위치 I를 찾으면 start_y, start_x에 각각 위치 저장
3. 도연이 위치에서 bfs 탐색 시작
4. 현재 위치에서 상하좌우 방향배열 탐색 시작
5. 범위 내에 있으며, 이동 불가능한 곳이 아니고, 방문한 곳이 아니면 이동
6. 이동한 곳이 P(사람)일 경우 cnt + 1
7. 탐색이 끝나면 출력 -> cnt가 0이면 TT 출력, 1이상이면 cnt 값 출력
```


# 10/22
## N과 M (2)
```
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
# 자연수 N과 M이 주어졌을 떄, 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순
# 중복되는 수열 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력
def nandm(now, cnt):
    if cnt == M:
        print(*lst)

    for next in range(now, N+1):
        lst.append(next)
        nandm(next+1, cnt+1)
        lst.pop()


N, M = map(int, input().split())
lst = []
cnt = 0
nandm(1, 0)
```
## N과 M (4)
```
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
# 자연수 N과 M이 주어졌을 떄, 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순
def nandm(now, cnt):
    # lst.append(now)
    if cnt == M:
        print(*lst)
        return

    for next in range(now, N+1):
        lst.append(next)
        nandm(next, cnt+1)
        lst.pop()


N, M = map(int, input().split())
lst = []
cnt = 0
nandm(1, 0)
```
## N과 M (5)
```
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
# 길이가 M인 수열을 모두 구하는 프로그램
# N개의 자연수 중에서 M개를 고른 수열
# 한줄에 하나씩 문제의 조건을 만족하는 수열 출력
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력
# 수열은 사전 순으로 증가하는 순서로 출력

def dfs(now, cnt):
    if cnt == M:
        print(*ans)
        return
    for next in range(now, N):
        if not v[next]:
            v[next] = 1
            ans.append(arr[next])
            dfs(now, cnt+1)
            ans.pop()
            v[next] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
v = [0] * N
dfs(0,0)
```
