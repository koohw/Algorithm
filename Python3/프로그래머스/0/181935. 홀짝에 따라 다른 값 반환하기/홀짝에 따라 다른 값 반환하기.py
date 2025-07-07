# n의 홀수 -> n이하의 홀수인 모든 양의 정수의 합 Return
# n이 짝수 -> n이하의 모든 양의 정수의 제곱의 합 return

def solution(n):
    answer = 0
    
    if n % 2 == 0:
        for even in range(n+1):
            if even % 2 ==0:
                answer += even **2
    else:
        for odd in range(n+1):
            if odd % 2 != 0:
                answer += odd
            
    return answer