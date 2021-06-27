#프로그래머스 > 탐욕법 > 구명보트

people = [50,80,70,50]
limit = 100
cnt = 0
people.sort()
temp = 0
p = 0

#시도 1 -> 오답이 너무 많았다
# for i in range(len(people)):
#     temp+=people[i]
#     p+=1
#     if p==2:
#         p=0
#         continue
#     print(temp)
#     if temp >limit and temp!=people[i]:
#         cnt+=2
#         temp=0
#         p=0
#     elif temp <=limit and i ==len(people)-1:
#         cnt+=1
#     elif temp <=limit and temp!=people[i]:
#         cnt+=1
#         temp=0
#         p=0
#     elif temp <=limit and temp==people[i]:
#         continue


# 시도 2 여전히 오답이 많았다 -> 오름차순 정렬 후 맨 앞과 맨 뒤를 비교하기
# for i in range(len(people)):
#     # print(p,temp,cnt)
#     p+=1
#     temp+=people[i]
#     print(p,temp,cnt)
#     if p==2 and temp <=limit:
#         cnt+=1
#         temp=0
#         p=0
#     elif p==2 and temp>limit:
#         cnt+=2
#         temp=0
#         p=0
#     elif p==1 and temp >= limit:
#         cnt+=1
#         p=0
#         temp=0
#
#     elif p==1 and temp < limit:
#         if i!=len(people)-1:
#             continue
#         else:
#             cnt+=1
#
# print(cnt)

#시도 3 -> 맨앞과 맨뒤를 고려했지만 효율성 test 1번에서 시간 초과
# while people:
#     if len(people)>=2:
#         if people[0]+people[-1]<=limit:
#             cnt+=1
#             people.pop()
#             people.pop(0)
#         else:
#             cnt+=1
#             people.pop()
#     else:
#         cnt+=1
#         people.pop()
#
# print(people, cnt)


#시도 4-> 시간 문제 해결하기 위해 deque 사용
from collections import deque
dq = deque(people)
while dq:
    if len(dq)>=2:
        if dq[0]+dq[-1]<=limit:
            cnt+=1
            dq.pop()
            dq.popleft()
        else:
            cnt+=1
            dq.pop()
    else:
        cnt+=1
        dq.pop()
print(cnt)




#####################
# 참고하면 좋은 코드
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer # 전체 인원에서 짝지은 수 빼면 보트의 수