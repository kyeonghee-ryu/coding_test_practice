#프로그래머스 > 완전탐색 > 카펫
def solution(brown, yellow):
    lis = []
    for i in range(1, round(yellow**0.5)+ 1 ):
        if yellow % i == 0:
            lis.append([i,yellow/i])
    result = []
    for l in lis:
        if (l[0]+ l[1]) * 2 + 4 == brown:
            result.extend([l[1]+2, l[0]+2])
            break

    return result

print(solution(10,2))


# 코드 줄이기

def solution(brown, yellow):
    lis = []
    for i in range(1, round(yellow**0.5)+ 1 ):
        if yellow % i == 0 and (i+yellow//i)*2+4==brown:
            return [yellow//i+2, i+2]

print(solution(10,2))