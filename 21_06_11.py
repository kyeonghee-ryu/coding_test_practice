# 백준 11866번 요세푸스문제(분류)

# K = 3
# N = 7
# survive = [i+1 for i in range(N)]
# stack = []
# inter = K
# while len(survive)!=0:
#     if K<=len(survive):
#         stack.append(survive[K-1])
#         survive.remove(stack[-1])
#         K+=inter
#     else:
#         K = inter-len(survive)%3
#         stack.append(survive[K-1])
#         survive.remove ( stack[-1] )

#
# while len(survive)!=0:
#     print(K)
#     if K>len(survive):
#         K = inter-(survive[-1]-stack[-1])
#         print('k 수정',K)
#     else:
#         pass
#
#     stack.append(survive[K-1])
#     survive.remove(stack[-1])
#     K+=inter
#     print(stack)
# print(stack)
K = 3
N = 7
people = [i+1 for i in range(N)]
stack=[]
cnt = 0
while people: #사람이 한명남을때까지 반복
    print(people)
    print(stack)
    for i in people:
        print(cnt, i)
        cnt+=1 #1번병사 cnt=1, 2번병사 cnt=2
        if cnt==K: #3번병사 cnt=3 -> 리스트에서 제거
            stack.append(i)
            people.remove(i)
            cnt=1 # 카운트 다시 1로 리셋
        else:
            continue



#프로그래머스 > 스택 큐 > 프린터

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
# idx = [i for i in range(len(priorities))]
# cnt=0
# while location in idx:
#     print(priorities)
#     print(idx)
#     print(cnt)
#     if max(priorities)==priorities[0]:
#         cnt+=1
#         priorities.pop(0)
#         idx.pop(0)
#     else:
#         priorities.append(priorities[0])
#         del priorities[0]
#         idx.append(idx[0])
#         del idx[0]
#
# print(cnt)
#
#
