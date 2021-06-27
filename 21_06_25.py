#프로그래머스 > 깊이/너비 우선탐색 > 타겟넘버


numbers=[1,1,1,1,1]
target=3


def solution(numbers, target):
    cnt = 0
    for i in range(len(numbers)):
        ls = list(combinations(numbers,i+1))
        for j in range(len(ls)):
            temp = numbers.copy()
            plus = sum(ls[j])
            for k in ls[j]:
                temp.remove(k)
            minus = sum(temp)
            if plus-minus ==target:
                cnt+=1
    return cnt

from itertools import combinations


####################
# 참고하면 좋은 코드
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

