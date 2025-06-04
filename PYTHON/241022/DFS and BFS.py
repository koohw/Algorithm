# DFS와 BFS
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

def dfs(now):
    ans_dfs.append(now)

    for next in arr[now]:
        if visited[next]: continue
        visited[next] = 1
        dfs(next)


def bfs(here):
    q = []
    q.append(here)
    ans_bfs.append(here)

    while q:
        now = q.pop(0)
        for next in arr[now]:
            if visited[next]: continue
            q.append(next)
            ans_bfs.append(next)
            visited[next] = 1


N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

visited = [0] * (N+1)
visited[V] = 1
ans_dfs = []
dfs(V)

visited = [0] * (N+1)
visited[V] = 1
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)