# 모두 p -> 1111 * p
# 세개에서 p, 나머지 q -> (10 × p + q)**2
# 두개가 값은 값 p, 나머지 두개 같은 값 q -> (p + q) × abs(p - q)
# 두개가 같은 값 p, q, r -> q * r
# 모두 다른 값 -> 가장 작은 수만큼 얻음

def solution(a, b, c, d):
    answer = 0
    
    if a == b and b == c and c == d:
        return 1111 * a
    elif (a == b and b == c):
        return (10 * a + d)**2
    elif (a==b and b==d):
        return (10 * a + c)**2
    elif (a==c and c==d):
        return (10 * a + b)**2
    elif (b==c and c==d):
        return (10 * b + a)**2
    elif (a==b and c==d):
        return (a + c) * abs(a - c)
    elif (a==c and b==d) or (a==d and b==c):
        return (a + b) * abs(a - b)
    elif (a==b and c!=d):
        return c*d
    elif (a==c and b!=d):
        return b*d
    elif (b==c and a!=d):
        return a*d
    elif (b==d and a!=c):
        return a*c
    elif (a==d and b!=c):
        return b*c
    elif (c==d and a!=b):
        return a*b
    else:
        return min(a, b, c, d)
    
    return answer