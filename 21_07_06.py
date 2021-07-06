# 백준 > 완전탐색 > 치킨배달 (15686번)

def solution(M,city):
    home = []
    chicken  = []
    for i in range(len(city)):
        for j in range(len(city)):
            if city[i][j]==1:
                home.append((i,j))
            elif city[i][j]==2:
                chicken.append((i,j))
    comb = list(combinations(chicken,M))

    min_distance =[]

    for i in range(len(comb)):
        total_distance = 0
        for j in range(len(home)):
            min_home_sum = math.inf
            for k in range(len(comb[i])):
                each_sum = abs(home[j][0]-comb[i][k][0])+abs(home[j][1]-comb[i][k][1])
                if each_sum<min_home_sum:
                    min_home_sum = each_sum
            total_distance+=min_home_sum
        min_distance.append(total_distance)


    return min(min_distance)

import sys
from itertools import combinations
import math
N,M=map(int,sys.stdin.readline().split())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
print(solution(M,city))


