def solution(my_string, overwrite_string, s):
    answer = []
    for a in overwrite_string:
        answer.append(a)
    num = len(answer)

    ans = my_string[:int(s)] + overwrite_string + my_string[int(s)+num:]

    return ans