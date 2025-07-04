def solution(n, lost, reserve):
    answer = []
    
    common = set(lost) & set(reserve)
    lost = sorted(list(set(lost) - common))
    reserve = sorted(list(set(reserve) - common))

    for num in range(1, n + 1):
        if num not in lost:
            answer.append(num)

    for r in reserve:   # 빌려주는 사람
        if r - 1 in lost:
            answer.append(r-1)
            lost.remove(r-1)
        elif r + 1 in lost:
            answer.append(r+1)
            lost.remove(r+1)

    return len(set(answer))