# [s, e], tmp = my_string[s], my_string[s] = my_string[e], my_string[e] = tmp
def solution(my_string, queries):
    answer = ''
    my_list = list(map(str, my_string))
    
    for query in queries:
        my_list[query[0]:query[1]+1] = reversed(my_list[query[0]:query[1]+1])
        
    for s in my_list:
        answer += s
    return answer