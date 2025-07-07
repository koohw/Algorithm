# arr: 0~9. 연속적으로 나타나는 숫자 하나만 남기고 전부 제거
# 남은 수들을 반환할 때는 arr의 순서를 유지
def solution(arr):
    answer = []
    
    for a in range(len(arr)):
        if a == 0:
            answer.append(arr[0])
        if a > 0 and arr[a] != arr[a-1]:
            answer.append(arr[a])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer