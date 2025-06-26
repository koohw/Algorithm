# participant: 완주한 선수들이 이름이 담긴 배열
# completion: 완주x 선수들 이름
# solution: completion return

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    return participant[-1]

