# 1018. 체스판 다시 칠하기
import sys
input = sys.stdin.readline

# 1. 배열을 8x8로 잘라서 탐색
# 2. 1) 흰색일 경우 상하좌우가 검은색인지 탐색
#    2) 검은색인 경우 상하좌우가 흰색인지 탐색
# 현재 위치에서 상하좌우가 같은 색일경우 바꾼 후 cnt + 1
# 8x8 배열에서의 탐색이 끝나면 cnt 리스트에 저장하고 다음 8x8 배열을 탐색 시작
# 모든 위치를 탐색했다면 종료 후 최소 cnt 반환

chess1 = ['WB' * 4, 'BW' * 4] * 4
chess2 = ['BW' * 4, 'WB' * 4] * 4

N, M = map(int, input().split())    # N x M
arr = [input().strip() for _ in range(N)]
ans = []
min_changes = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0

        for y in range(8):
            for x in range(8):
                if arr[i + y][j + x] != chess1[y][x]:
                    cnt1 += 1
                if arr[i + y][j + x] != chess2[y][x]:
                    cnt2 += 1

        min_changes = min(min_changes, cnt1, cnt2)

print(min_changes)

