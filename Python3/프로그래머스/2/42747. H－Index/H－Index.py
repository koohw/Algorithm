def solution(citations):    # citations: 인용 횟수
    answer = 0
    citations.sort(reverse=True)  # 내림차순 정렬

    for c in range(len(citations)):
        if citations[c] >= c + 1:
            answer = c + 1
        else:
            break
        
    return answer