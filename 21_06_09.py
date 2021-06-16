#백준 11653번) 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline
num = int(input())
final_num = num
div_list = []
for i in range(2,num+1):
    if num%i==0:
        final_num%=i
        div_list.append(i)
    else:
        continue

for i in div_list:
    while num%i==0:
        print(i)
        num/=i



# 프로그래머스 해시 > 위장

from itertools import combinations
clothes =[["yellowhat", "headgear"],
          ["bluesunglasses", "eyewear"],
          ["red_turban", "headgear"],
          ["green_glasses", "eyewear"],
          ["green_turban", "headgear"],
          ["stripe", "shirt"],
          ["yellow", "shirt"]]

def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    cloth = list ( dic.keys () )
    cnt = sum ( dic.values () )

    for i in range ( 1, len ( dic ) + 1 ):
        if i > 1:
            comb = list ( combinations ( cloth, i ) )
            # comb_count =1
            for j in range ( len ( comb ) ):
                comb_cnt = 1
                comb_lis = [dic[comb[j][k]] for k in range ( i )]
                for k in comb_lis:
                    comb_cnt *= k
                cnt += comb_cnt

    return cnt


