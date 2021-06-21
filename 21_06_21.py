# 프로그래머스 > 탐욕법 > 체육복

n = 5
lost =[2,3,4]
reserve = [1,2,3]


def solution(n, lost, reserve):
    lost.sort ()
    reserve.sort ()

    reserve_new = list ( set ( reserve ) - set ( lost ) )
    lost_new = list ( set ( lost ) - set ( reserve ) )

    for i in reserve_new:
        if i - 1 in lost_new:
            lost_new.remove ( i - 1 )
            continue
        if i + 1 in lost_new:
            lost_new.remove ( i + 1 )
            continue
    return n - len ( lost_new )

print(solution(n,lost,reserve))