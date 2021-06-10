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

clothes =[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
dic = {}
for i in clothes:
    if i[1] in dic:
        dic[i[1]] += 1
    else:
        dic[i[1]] = 1

res = len(clothes)
if len(dic)!=1:
    temp =
    for cloth in list(dic.keys()):
        if dic[cloth]!=1:

else:
    pass

print(list(dic.keys()))