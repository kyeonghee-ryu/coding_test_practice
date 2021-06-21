import itertools


def solution(numbers):
    num = list( numbers )
    lis = []
    for i in range(1,len ( num ) + 1 ):
        temp = list (map(''.join,itertools.permutations( num, i)))
        lis.extend(temp)

    lis = list (set(lis))
    final_list = []
    for i in range(len(lis)):
        if lis[i][0] == '0':  # 맨 앞자리 0인 것 제외
            continue
        if lis[i] == '1':  # 1은 소수 아니므로 제외
            continue
        k = 0
        for j in range (2,round(eval(lis[i] )**0.5)+ 1 ):  # 소수인것만 찾기
            if eval(lis[i] )%j == 0:
                k = 1
                break
        if k == 0:
            final_list.append(eval(lis[i]))

    return len(final_list)

import itertools



##########################

#참고하면 좋은 코드
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


