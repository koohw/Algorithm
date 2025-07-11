def solution(arr, queries):
    answer = []
    result = []

    for q in queries:  # [0, 4, 2], [0,3,2], [0,2,2]
        answer = arr[q[0]:q[1]+1]
        num = []
        for a in answer:
            if a > q[2]:
                num.append(a)
        if not num:
            result.append(-1)
        else:
            result.append(min(num))
    return result