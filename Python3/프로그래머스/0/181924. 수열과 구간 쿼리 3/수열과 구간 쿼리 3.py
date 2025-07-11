def solution(arr, queries):
    for i in queries:  # [0,3], [1,2], [1,4]
        tmp = arr[i[1]]  # tmp = 4
        arr[i[1]] = arr[i[0]]
        arr[i[0]] = tmp  # [3, 2, 1, 0, 4]

    return arr