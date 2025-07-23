def solution(sizes):
    answer = 0
    x = []
    y = []
    
    for size in sizes:   # size[0]:가로, size[1]:세로
        if size[0] > size[1]:
            x.append(size[0])
            y.append(size[1])
        else:
            x.append(size[1])
            y.append(size[0])
    
            
    return max(x) * max(y)