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