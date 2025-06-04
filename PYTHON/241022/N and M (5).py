# N and M (5)
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


