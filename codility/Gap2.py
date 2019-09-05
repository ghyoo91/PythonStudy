import math

def solution(N):
    result = 0
    flag = 0
    count = 0

    while N >= 1:
        tmp = N%2
        if tmp == 1:
            if flag == 0:
                flag = 1
            else:
                if result < count:
                    result = count
                count = 0
        else:
            if flag == 1:
                count = count+1
        N = math.floor(N/2)

    return result

A = solution(1041)
