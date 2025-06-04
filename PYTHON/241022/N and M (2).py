# N과 M (2)
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