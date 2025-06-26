# 순열
# nums 배열에서 n/2개 뽑음
# 중복 수 빼고 list 개수 셋을 때 가장 많은 수 return

def solution(nums):
    return min(len(set(nums)), len(nums)//2)