def solution(A, K):
    realK = 0
    lenA = len(A)
    result = [None]*lenA

    if lenA == 0:
        return A
    else:
        if lenA < K:
            realK = K%lenA
        else:
            realK = K

        for i in range(0, lenA):
            if i+realK < lenA:
                result[i+realK] = A[i]
            else:
                result[i+realK-lenA] = A[i]

        return result

#R = solution([3, 8, 9, 7, 6], 3)
#R = solution([0,0,0], 1)
#R = solution([1,2,3,4], 5)
R = solution([], 5)
print(R)
