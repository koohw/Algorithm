# 최소 1가지 이상의 옷을 입음
# 옷의 조합 수 return
# 리스트의 마지막 항목은 종류를 나타냄.

from collections import Counter

def solution(clothes):
    
    counter = Counter([category for _, category in clothes])
    combinations = 1
    for count in counter.values():
        combinations *= (count + 1)
    
    return combinations - 1